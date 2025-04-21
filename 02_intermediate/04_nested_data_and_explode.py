import os
import polars as pl
import json

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Create a nested JSON-like structure for portfolio holdings
nested_data = [
    {"client_id": "C0001", "portfolios": [
        {"port_id": "P1", "holdings": ["A0001", "A0002"]},
        {"port_id": "P2", "holdings": ["A0003"]}
    ]},
    {"client_id": "C0002", "portfolios": [
        {"port_id": "P3", "holdings": ["A0001", "A0004"]}
    ]}
]

# Write to file for demonstration purposes
with open(f"{datasets_dir}/nested.json", "w") as f:
    json.dump(nested_data, f, indent=2)

# 1. Create DataFrame from nested data
df = pl.DataFrame(nested_data)
print("Original nested DataFrame:")
print(df)

# 2. Explode the portfolios column (list of struct)
exploded = df.explode("portfolios")
print("\nExploded portfolios:")
print(exploded)

# 3. Extract struct fields from portfolios column
extracted = exploded.with_columns([
    pl.col("portfolios").struct.field("port_id").alias("portfolio_id"),
    pl.col("portfolios").struct.field("holdings").alias("holdings")
])
print("\nExtracted struct fields:")
print(extracted)

# 4. Further explode the holdings array
fully_exploded = extracted.explode("holdings")
print("\nFully exploded holdings:")
print(fully_exploded)

# 5. Drop the original portfolios column
final = fully_exploded.drop("portfolios")
print("\nFinal clean result:")
print(final)

# 6. Demonstrate "melt" operation (wide to long format)
# Create a wide dataframe with asset values
wide_df = pl.DataFrame({
    "client_id": ["C0001", "C0002", "C0003"],
    "equity_val": [10000, 15000, 8000],
    "bond_val": [5000, 7000, 12000],
    "commodity_val": [2000, 0, 3000]
})

print("\nWide format dataframe:")
print(wide_df)

# Melt to convert to long format
melted = wide_df.unpivot(
    index=["client_id"],
    on=["equity_val", "bond_val", "commodity_val"],
    variable_name="asset_class",
    value_name="value"
)

print("\nMelted to long format:")
print(melted)

# Explode portfolios to rows
df_exploded = extracted
exploded = df_exploded.group_by(["client_id", "portfolio_id"]).agg([
    pl.col("holdings").explode().alias("exploded_holdings")
])
print("Exploded portfolios:")
print(exploded)

# Save results
final.write_csv(f"{datasets_dir}/exploded_holdings.csv")
melted.write_csv(f"{datasets_dir}/melted_assets.csv")