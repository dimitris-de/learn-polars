"""
05_export_methods.py
Demonstrates DataFrame export methods: to_arrow, to_numpy, to_dict, to_struct.

This script demonstrates how to export Polars DataFrames to various formats. Each operation is explained for clarity.
"""
import polars as pl
import numpy as np

# Create an example DataFrame with different types of columns
# This allows demonstration of export to different formats
df = pl.DataFrame({
    "a": [1, 2, 3],
    "b": [4.0, 5.0, 6.0],
    "c": ["x", "y", "z"]
})

# to_arrow: Convert DataFrame to a PyArrow Table
# Useful for interoperability with libraries that use Arrow format
arrow_tbl = df.to_arrow()
print("Arrow Table:", arrow_tbl)

# to_numpy: Convert DataFrame to a NumPy array (only numeric columns)
# Useful for machine learning or numerical operations
np_arr = df.to_numpy()
print("\nNumPy array:\n", np_arr)

# to_dict: Convert DataFrame to a dictionary
# Useful for serialization, debugging, or conversion to other formats
as_dict = df.to_dict()
print("\nDict:\n", as_dict)

# to_struct: Convert DataFrame to a Series of struct type
# Each row becomes a struct, useful for nested data or certain APIs
struct_col = df.to_struct()
print("\nStruct Series:\n", struct_col)
