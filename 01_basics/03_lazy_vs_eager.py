import os
import polars as pl
import time

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Eager execution
print("--- EAGER EXECUTION ---")
start = time.time()
df = pl.read_csv(f"{datasets_dir}/transactions.csv")
eager_result = df.filter(pl.col("amount") > 0).select(pl.sum("amount"))
eager_time = time.time() - start
print(f"Eager sum: {eager_result[0,0]}, time: {eager_time:.4f}s")

# Lazy execution
print("--- LAZY EXECUTION ---")
start = time.time()
lazy_df = pl.scan_csv(f"{datasets_dir}/transactions.csv")
lazy_result = (
    lazy_df
    .filter(pl.col("amount") > 0)
    .select(pl.sum("amount"))
    .collect()
)
lazy_time = time.time() - start
print(f"Lazy sum: {lazy_result[0,0]}, time: {lazy_time:.4f}s")

# Performance comparison
print(f"\nLazy vs Eager speedup: {eager_time/lazy_time:.2f}x")