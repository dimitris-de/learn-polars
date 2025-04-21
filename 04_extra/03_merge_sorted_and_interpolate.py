"""
03_merge_sorted_and_interpolate.py
Demonstrates DataFrame.merge_sorted and DataFrame.interpolate.

This script demonstrates how to merge two sorted DataFrames and how to interpolate missing values. Each step is explained for clarity.
"""
import polars as pl

# Example: merge_sorted
# Create two DataFrames that are already sorted by column 'a'.
# This is important because merge_sorted assumes both DataFrames are sorted.
left = pl.DataFrame({"a": [1, 3, 5], "b": [10, 30, 50]})
right = pl.DataFrame({"a": [2, 4, 6], "b": [20, 40, 60]})

# Merge the two DataFrames while preserving the order of 'a'.
# This is useful for time series or ordered data where you want to keep the sort order.
merged = left.merge_sorted(right, key="a")
print("Merge sorted:")
print(merged)

# Example: interpolate
# DataFrame with missing values (None)
df = pl.DataFrame({"x": [1, 2, 3, 4, 5], "y": [10.0, None, 30.0, None, 50.0]})
# Interpolate fills in missing values in 'y' using linear interpolation.
# This is useful for handling gaps in time series or continuous data.
interpolated = df.with_columns(pl.col("y").interpolate().alias("y_interp"))
print("\nInterpolated:")
print(interpolated)
