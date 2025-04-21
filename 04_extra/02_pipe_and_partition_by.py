"""
02_pipe_and_partition_by.py
Demonstrates DataFrame.pipe and DataFrame.partition_by.

This script shows how to use the pipe method for functional programming and partition_by for splitting data by groups. Each step is explained for clarity.
"""
import polars as pl

# Define a function that adds one to column 'a' in a DataFrame
# This demonstrates how you can write custom functions and use them with pipe for clean, functional data processing
# Pipe is useful for chaining transformations in a readable way
def add_one(df: pl.DataFrame) -> pl.DataFrame:
    # pl.col("a") selects column 'a', adds 1, and renames it to 'a_plus_one'
    return df.with_columns((pl.col("a") + 1).alias("a_plus_one"))

# Create a simple DataFrame to demonstrate the methods
df = pl.DataFrame({"a": [1, 2, 3, 4], "b": ["x", "y", "x", "y"]})

# Use pipe to apply the add_one function to the DataFrame
# This is equivalent to: add_one(df), but enables method chaining
# Good for readability and composability in data pipelines
df2 = df.pipe(add_one)
print("After pipe:")
print(df2)

# Partition the DataFrame by the values in column 'b'
# partition_by splits the DataFrame into a list of DataFrames, one for each unique value in 'b'
# This is useful for group-wise processing when you want to operate on each group separately
partitions = df.partition_by("b")
print("\nPartitions:")
for part in partitions:
    print(part)
