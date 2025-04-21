import os
import polars as pl

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load cleaned transactions, clients, and assets
tx = pl.read_csv(f"{datasets_dir}/cleaned_transactions.csv")
clients = pl.read_csv(f"{datasets_dir}/clients.csv")
assets = pl.read_parquet(f"{datasets_dir}/assets.parquet")

# Join transactions with client and asset metadata
df = (
    tx.join(clients, on="client_id", how="inner")
      .join(assets, on="asset_id", how="inner")
)
print(f"Joined records: {df.height}")

# Filter high-value transactions > 15000
high = df.filter(pl.col("amount") > 15000)
print("High-value sample:")
print(high.head())

# Select key columns and sort by date
result = df.select([
    "transaction_id", "client_id", "name", "asset_type", "amount", "date"
]).sort("date")
print("Sorted sample:")
print(result.head())

# Save joined output
result.write_csv(f"{datasets_dir}/joined_transactions.csv")