"""
10_df_manipulation_methods.py
Demonstrates insert_column, drop_in_place, extend, clone, clear.

This script demonstrates common DataFrame manipulation methods in Polars. Each operation is explained for educational clarity.
"""
import polars as pl

# insert_column: Insert a new column at a specific position in the DataFrame
# Here, we insert a Series 'b' at position 1 (second column)
df = pl.DataFrame({"a": [1, 2, 3]})
df.insert_column(1, pl.Series("b", [4, 5, 6]))
print("After insert_column:")
print(df)

# drop_in_place: Remove a column by name and return it as a Series
# This is useful when you want to both remove and inspect a column
removed = df.drop_in_place("a")
print("\nRemoved column 'a':", removed)
print("DataFrame after drop_in_place:")
print(df)

# extend: Append the rows of another DataFrame to this one (in-place)
# The columns must match by name and type
other = pl.DataFrame({"b": [7, 8]})
df.extend(other)
print("\nAfter extend:")
print(df)

# clone: Create a deep copy of the DataFrame
# Changes to the clone will not affect the original
df_clone = df.clone()
print("\nCloned DataFrame:")
print(df_clone)

# clear: Remove all rows from the DataFrame (in-place)
df.clear()
print("\nAfter clear (should be empty):")
print(df)
