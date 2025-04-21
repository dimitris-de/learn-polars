import os
import polars as pl
import matplotlib.pyplot as plt

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load cleaned transactions, assets, and benchmarks
tx = pl.read_csv(f"{datasets_dir}/cleaned_transactions.csv")
assets = pl.read_parquet(f"{datasets_dir}/assets.parquet")
benchmarks = pl.read_csv(f"{datasets_dir}/benchmarks.csv")

# Join transactions with assets
df = tx.join(assets, on="asset_id", how="inner")

# Compute trade value = amount * price
df = df.with_columns([
    (pl.col("amount") * pl.col("price")).alias("trade_value")
])

# ATTRIBUTION BY ASSET TYPE
# =========================
asset_type_attr = (
    df.group_by("asset_type")
      .agg([
          pl.sum("trade_value").alias("total_value"),
          pl.count().alias("num_trades")
      ])
)

# Calculate percentage attribution
total = asset_type_attr["total_value"].sum()
asset_type_attr = asset_type_attr.with_columns([
    (pl.col("total_value") / total * 100).alias("pct_attribution")
])

print("Return attribution by asset type:")
print(asset_type_attr)

# ATTRIBUTION BY REGION
# ====================
region_attr = (
    df.group_by("region")
      .agg([
          pl.sum("trade_value").alias("total_value"),
          pl.count().alias("num_trades")
      ])
)

# Calculate percentage attribution
region_attr = region_attr.with_columns([
    (pl.col("total_value") / total * 100).alias("pct_attribution")
])

print("\nReturn attribution by region:")
print(region_attr)

# Save results
asset_type_attr.write_csv(f"{datasets_dir}/asset_type_attribution.csv")
region_attr.write_csv(f"{datasets_dir}/region_attribution.csv")