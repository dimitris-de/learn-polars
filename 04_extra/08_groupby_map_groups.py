"""
08_groupby_map_groups.py
Demonstrates groupby with apply for custom group-wise operations.

This script demonstrates how to use groupby and aggregation methods in Polars to perform group-wise computations. Each step is explained for clarity.
"""
import polars as pl

# Create a DataFrame with a group column and a value column
# This DataFrame will be used to demonstrate groupby and aggregation operations
df = pl.DataFrame({
    "group": ["A", "A", "B", "B"],  # Group labels
    "value": [1, 2, 3, 4]  # Values to be aggregated
})

# Perform groupby on the 'group' column and aggregate values
# Here, we calculate the sum and mean of the 'value' column for each group
# groupby returns a lazy groupby object, and agg applies the aggregations
# The result will be a new DataFrame with the aggregated values
result = df.group_by("group").agg([
    # Calculate the sum of the 'value' column for each group
    pl.col("value").sum().alias("sum"),  
    # Calculate the mean of the 'value' column for each group
    pl.col("value").mean().alias("mean")
])
# Print the resulting DataFrame
print(result)
