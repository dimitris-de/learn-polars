"""
07_advanced_joins.py
Demonstrates join_asof and join_where.

This script demonstrates advanced join methods in Polars: join_asof for time series (ordered) joins and join_where for conditional joins. Each operation is explained for educational clarity.
"""
import polars as pl

# join_asof example (time series join)
# Create two DataFrames with a common 'time' column
# join_asof matches each row from the left DataFrame to the closest row (by 'time') in the right DataFrame without going over
# This is useful for time series data where exact matches may not exist
df_left = pl.DataFrame({
    "time": [1, 2, 3, 4],
    "value": [10, 20, 30, 40]
})
df_right = pl.DataFrame({
    "time": [1, 2, 3, 4],
    "event": ["A", "B", "C", "D"]
})
# Perform an asof join on the 'time' column
# The result will contain all columns from both DataFrames, matched by the 'time' column
joined_asof = df_left.join_asof(df_right, on="time")
print("ASOF join:")
print(joined_asof)

# join_where example (conditional join)
# Create two DataFrames with a common column 'a'
df_a = pl.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
df_b = pl.DataFrame({"a": [2, 3, 4], "c": [200, 300, 400]})
# join_where allows joining on arbitrary conditions, not just equality of columns
# Here, we join on equality of column 'a' between the two DataFrames
# The condition is specified using Polars' expression syntax
joined_where = df_a.join_where(
    df_b,
    pl.col("a") == pl.col("a"),  # join on equality of column 'a'
)
print("\nWHERE join:")
print(joined_where)
