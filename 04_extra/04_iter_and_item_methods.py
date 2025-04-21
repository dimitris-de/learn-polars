"""
04_iter_and_item_methods.py
Demonstrates DataFrame item, iter_columns, iter_rows, iter_slices.

This script shows how to access individual items, columns, rows, and slices in a DataFrame. Each part is explained for clarity.
"""
import polars as pl

# Create a simple DataFrame with three columns
# This will be used to demonstrate various iteration and access methods
df = pl.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
})

# item: get a single value by row index and column name
# This is useful when you need a specific cell's value
print("Item (row 1, col 'b'):", df.item(1, "b"))

# iter_columns: iterate over all columns as Series
# Useful for applying operations to each column
print("\nColumns:")
for col in df.iter_columns():
    print(col)

# iter_rows: iterate over all rows as tuples
# Useful for row-wise processing or exporting data
print("\nRows:")
for row in df.iter_rows():
    print(row)

# iter_slices: iterate over DataFrame in chunks (slices) of n_rows
# Useful for batch processing or memory-efficient operations
print("\nSlices:")
for sl in df.iter_slices(n_rows=2):
    print(sl)
