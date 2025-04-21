"""
14_flags_and_properties.py
Demonstrates DataFrame and Series flags and properties not yet shown.

This script demonstrates how to inspect various flags and properties of Polars DataFrames and Series. Each operation is explained for educational clarity.
"""
import polars as pl

# Create a sample DataFrame with two columns 'a' and 'b'
df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

# DataFrame flags: Show internal settings and optimization flags
# The flags attribute provides information about the internal settings and optimization flags of the DataFrame.
print("DataFrame flags:", df.flags)

# DataFrame columns: List of column names
# The columns attribute returns a list of column names in the DataFrame.
print("DataFrame columns:", df.columns)

# DataFrame shape: Tuple of (number of rows, number of columns)
# The shape attribute returns a tuple containing the number of rows and columns in the DataFrame.
print("DataFrame shape:", df.shape)

# DataFrame height: Number of rows
# The height attribute returns the number of rows in the DataFrame.
print("DataFrame height:", df.height)

# DataFrame width: Number of columns
# The width attribute returns the number of columns in the DataFrame.
print("DataFrame width:", df.width)

# DataFrame is_empty: Boolean indicating if DataFrame has no rows
# The is_empty attribute returns a boolean indicating whether the DataFrame has no rows.
print("DataFrame is_empty:", df.is_empty())

# Series properties and flags
# Select a Series from the DataFrame (in this case, column 'a')
s = df["a"]

# Series flags: Show internal settings for the Series
# The flags attribute provides information about the internal settings and optimization flags of the Series.
print("\nSeries flags:", s.flags)

# Series dtype: Data type of the Series
# The dtype attribute returns the data type of the Series.
print("Series dtype:", s.dtype)

# Series shape: Tuple with the number of elements
# The shape attribute returns a tuple containing the number of elements in the Series.
print("Series shape:", s.shape)

# Series n_chunks: Number of memory chunks (affects performance)
# The n_chunks attribute returns the number of memory chunks in the Series, which can affect performance.
print("Series n_chunks:", s.n_chunks)

# Series is_sorted: Boolean indicating if Series is sorted
# The is_sorted method returns a boolean indicating whether the Series is sorted.
print("Series is_sorted:", s.is_sorted())

# Series is_null: Boolean mask for null values
# The is_null method returns a boolean mask indicating which values in the Series are null.
print("Series is_null:", s.is_null())

# Series is_not_null: Boolean mask for non-null values
# The is_not_null method returns a boolean mask indicating which values in the Series are not null.
print("Series is_not_null:", s.is_not_null())
