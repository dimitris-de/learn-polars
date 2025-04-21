"""
12_concat_and_append.py
Demonstrates horizontal and vertical concatenation and append.

This script demonstrates how to concatenate and append DataFrames in Polars. Each operation is explained for educational clarity.
"""
import polars as pl

# Vertical concatenation: Stack DataFrames on top of each other (row-wise)
# Create two sample DataFrames with the same columns
df1 = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
df2 = pl.DataFrame({"a": [5, 6], "b": [7, 8]})
# Use pl.concat to stack df1 and df2 vertically, resulting in a new DataFrame
vertical = pl.concat([df1, df2], how="vertical")
print("Vertical concat:")
print(vertical)

# Horizontal concatenation: Combine DataFrames side by side (column-wise)
# Create a new DataFrame with a different set of columns
df3 = pl.DataFrame({"c": [9, 10, 11, 12]})
# Use pl.concat to combine vertical and df3 horizontally, resulting in a new DataFrame
horizontal = pl.concat([vertical, df3], how="horizontal")
print("\nHorizontal concat:")
print(horizontal)

# Append (in-place): Add rows of one DataFrame to another (modifies the original DataFrame)
# Create a copy of df1 to avoid modifying the original DataFrame
df1_appended = df1.clone()  # Use clone to avoid modifying the original
# Use extend to add rows of df2 to df1_appended, modifying df1_appended in-place
df1_appended.extend(df2)
print("\nAppended:")
print(df1_appended)
