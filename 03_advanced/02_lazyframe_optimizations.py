
import os
import polars as pl
import time
import matplotlib.pyplot as plt

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load our datasets lazily
tx_lazy = pl.scan_csv(f"{datasets_dir}/transactions.csv")
clients_lazy = pl.scan_csv(f"{datasets_dir}/clients.csv")
assets_lazy = pl.scan_parquet(f"{datasets_dir}/assets.parquet")

# 1. PREDICATE PUSHDOWN
# =====================
print("DEMONSTRATION OF PREDICATE PUSHDOWN OPTIMIZATION")
# Without predicate pushdown (filtering after join)
start = time.time()
result1 = (
    tx_lazy
    .join(assets_lazy, on="asset_id")
    .filter(pl.col("amount") > 5000)
    .select(["transaction_id", "client_id", "asset_type"])
)
print(result1.collect().head())
time1 = time.time() - start
print(f"Time without explicit pushdown: {time1:.4f}s")

# With predicate pushdown (filtering before join)
start = time.time()
result2 = (
    tx_lazy
    .filter(pl.col("amount") > 5000)
    .join(assets_lazy, on="asset_id")
    .select(["transaction_id", "client_id", "asset_type"])
)
print(result2.collect().head())
time2 = time.time() - start
print(f"Time with explicit pushdown: {time2:.4f}s")
print(f"Speedup: {time1/time2:.2f}x")

# 2. PROJECTION PUSHDOWN
# =====================
print("\nDEMONSTRATION OF PROJECTION PUSHDOWN OPTIMIZATION")
# Without explicit projection (selecting columns after operations)
start = time.time()
result3 = (
    tx_lazy
    .join(clients_lazy, on="client_id")
    .join(assets_lazy, on="asset_id")
    .select(["transaction_id", "name", "asset_type"])
)
print(result3.collect().head())
time3 = time.time() - start
print(f"Time without explicit projection: {time3:.4f}s")

# With explicit projection (selecting columns before operations)
start = time.time()
result4 = (
    tx_lazy
    .select(["transaction_id", "client_id", "asset_id"])
    .join(
        clients_lazy.select(["client_id", "name"]), 
        on="client_id"
    )
    .join(
        assets_lazy.select(["asset_id", "asset_type"]), 
        on="asset_id"
    )
    .select(["transaction_id", "name", "asset_type"])
)
print(result4.collect().head())
time4 = time.time() - start
print(f"Time with explicit projection: {time4:.4f}s")
print(f"Speedup: {time3/time4:.2f}x")

# 3. COMMON SUBEXPRESSION ELIMINATION
# ==================================
print("\nDEMONSTRATION OF COMMON SUBEXPRESSION ELIMINATION")
# Cache intermediate results for reuse
start = time.time()
filtered_tx = tx_lazy.filter(pl.col("amount") > 1000)
result5 = filtered_tx.select(pl.sum("amount"))
count5 = filtered_tx.select(pl.len())
print(f"Sum: {result5.collect()[0,0]}, Count: {count5.collect()[0,0]}")
time5 = time.time() - start
print(f"Time with caching: {time5:.4f}s")

# Without caching
start = time.time()
result6 = tx_lazy.filter(pl.col("amount") > 1000).select(pl.sum("amount"))
count6 = tx_lazy.filter(pl.col("amount") > 1000).select(pl.len())
print(f"Sum: {result6.collect()[0,0]}, Count: {count6.collect()[0,0]}")
time6 = time.time() - start
print(f"Time without caching: {time6:.4f}s")
print(f"Speedup: {time6/time5:.2f}x")

# 4. QUERY OPTIMIZATION PLAN
# =========================
print("\nQUERY OPTIMIZATION PLAN")
complex_query = (
    tx_lazy
    .join(clients_lazy, on="client_id")
    .filter(pl.col("amount") > 1000)
    .group_by("client_id")
    .agg([
        pl.sum("amount").alias("total_amount"),
        pl.len().alias("transaction_count")
    ])
    .sort("total_amount", descending=True)
    .limit(5)
)

# Print the query optimization plan
print(complex_query.explain())