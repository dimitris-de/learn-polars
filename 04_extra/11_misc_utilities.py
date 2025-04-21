"""
11_misc_utilities.py
Demonstrates is_empty, is_duplicated, is_unique, sample, shuffle, reverse, rechunk, explode, shrink_to_fit.

This script demonstrates various utility functions for Polars DataFrames and Series. Each operation is explained for educational clarity.
"""
import polars as pl

# Create a sample DataFrame for demonstration purposes
df = pl.DataFrame({
    "a": [1, 2, 2, 4],  # Sample column with duplicate values
    "b": ["x", "y", "y", "z"]  # Sample column with duplicate values
})

# Check if the DataFrame has no rows
# is_empty returns a boolean indicating whether the DataFrame is empty
print("Is empty:", df.is_empty())

# Create a boolean mask indicating which values in a Series are duplicates
# is_duplicated returns a boolean Series where True indicates a duplicate value
print("Is duplicated:", df["a"].is_duplicated())

# Create a boolean mask indicating which values in a Series are unique
# is_unique returns a boolean Series where True indicates a unique value
print("Is unique:", df["a"].is_unique())

# Randomly sample a number of rows from the DataFrame
# sample returns a new DataFrame with the sampled rows
# seed is used for reproducibility
print("Sample 2 rows:")
print(df.sample(2, seed=42))

# Shuffle the rows of the DataFrame (random order, deterministic with seed)
# For Polars <0.19.0, use sample(n=df.height, with_replacement=False)
print("\nShuffled:")
print(df.sample(n=df.height, with_replacement=False, seed=42))

# Reverse the order of rows
# reverse returns a new DataFrame with the rows in reverse order
print("\nReversed:")
print(df.reverse())

# Merge memory chunks for optimal performance (rarely needed for small DataFrames)
# rechunk returns a new DataFrame with the memory chunks merged
print("\nRechunked:")
print(df.rechunk())

# Expand list values in a column into separate rows
# explode returns a new DataFrame with the list values expanded
df2 = pl.DataFrame({"a": [[1, 2], [3, 4]], "b": ["x", "y"]})
print("\nExploded:")
print(df2.explode("a"))

# Reduce memory usage by freeing unused capacity
# shrink_to_fit returns the original DataFrame with reduced memory usage
print("\nShrink to fit:")
df.shrink_to_fit()
print(df)
