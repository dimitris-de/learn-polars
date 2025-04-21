"""
01_schema_and_dtypes.py
Demonstrates DataFrame and Series meta-information: schema, dtypes, shape, columns, flags.

This script shows how to inspect the structure and metadata of Polars DataFrames and Series. Each print statement is explained so a junior engineer can understand what is being checked and why.
"""
import polars as pl

# Create an example DataFrame with three columns of different types
# 'a' is integer, 'b' is float, 'c' is string
# This variety helps demonstrate how Polars handles different dtypes
# and how schema and dtypes reflect this.
df = pl.DataFrame({
    "a": [1, 2, 3],
    "b": [4.0, 5.0, 6.0],
    "c": ["x", "y", "z"]
})

# Print the schema, which shows the column names and their data types
print("Schema:", df.schema)  # Useful for quickly understanding the structure of the DataFrame

# Print the list of data types for all columns
print("Dtypes:", df.dtypes)  # Shows the type of each column, important for debugging and validation

# Print the shape (number of rows, number of columns)
print("Shape:", df.shape)  # Helps you verify the size of your data

# Print the column names
print("Columns:", df.columns)  # Useful for referencing columns programmatically

# Print DataFrame flags (advanced usage, shows internal settings)
print("Flags:", df.flags)  # Rarely needed, but can help with debugging advanced scenarios

# Series meta-info section
# Extract a single column as a Series to demonstrate Series-level properties
s = df["b"]

# Print the data type of the Series
print("Series dtype:", s.dtype)  # Shows what kind of data is in the Series

# Print the shape of the Series (number of elements,)
print("Series shape:", s.shape)  # Useful for confirming the length of the Series

# Print the name of the Series (will match the column name)
print("Series name:", s.name)  # Helpful when working with multiple Series objects
