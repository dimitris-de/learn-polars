"""
06_misc_methods.py
Demonstrates hash_rows, fold, estimated_size, glimpse, approx_n_unique, null_count, n_chunks.

This script demonstrates various miscellaneous DataFrame and Series methods in Polars. Each operation is explained for educational clarity.
"""
import polars as pl
import numpy as np

# Create an example DataFrame with numeric, float (with nulls), and string columns
df = pl.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [1.0, None, 3.0, None],
    "c": ["x", "y", "z", "x"]
})

# hash_rows: Compute a hash for each row (useful for deduplication or data integrity checks)
# This operation generates a unique hash value for each row, which can be used to identify duplicate rows.
print("Hash rows:", df.hash_rows())

# fold: Combine multiple columns into a single value per row (here, sum of 'a' and 'b')
# pl.fold applies a function across columns row-wise, allowing for custom aggregation operations.
# In this case, we sum the values of columns 'a' and 'b' for each row.
df_fold = df.with_columns([
    pl.fold(acc=0, function=lambda acc, x: acc + x, exprs=[pl.col("a"), pl.col("b")]).alias("sum_a_b")
])
print("\nFolded DataFrame:")
print(df_fold)

# estimated_size: Estimate the memory usage of the DataFrame in bytes
# This method provides an estimate of the memory required to store the DataFrame, which can be useful for optimizing performance.
print("\nEstimated size (bytes):", df.estimated_size())

# glimpse: Print a concise summary of the DataFrame (structure, types, head)
# The glimpse method provides a quick overview of the DataFrame's structure, including column names, data types, and a preview of the data.
print("\nGlimpse:")
df.glimpse()

# approx_n_unique: Estimate the number of unique values in a Series (efficient for large data)
# This method uses a probabilistic approach to estimate the number of unique values in a Series, which can be more efficient than exact methods for large datasets.
print("\nApproximate n_unique in 'c':", df["c"].approx_n_unique())

# null_count: Count the number of nulls in each column
# This method returns a Series with the count of null values in each column, which can be useful for data quality checks.
print("\nNull count:", df.null_count())

# n_chunks: Show the number of memory chunks in the DataFrame (relevant for performance tuning)
# The number of chunks can impact performance, as it affects how data is stored and accessed in memory.
print("\nNumber of chunks:", df.n_chunks)
