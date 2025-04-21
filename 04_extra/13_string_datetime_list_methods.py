"""
13_string_datetime_list_methods.py
Demonstrates advanced string, datetime, categorical, and list methods.

This script demonstrates how to use advanced methods for string, datetime, categorical, and list columns in Polars. Each operation is explained for educational clarity.
"""
import polars as pl
import datetime

# String methods: Perform vectorized string operations on Series
# Create a DataFrame with a string column
df_str = pl.DataFrame({"s": ["foo", "Bar", "baz qux"]})
# Convert all strings to uppercase using the to_uppercase method
# This operation is case-sensitive and converts all characters to uppercase
print("Upper:", df_str["s"].str.to_uppercase())
# Check if each string contains the substring 'ba' using the contains method
# This operation returns a boolean mask indicating whether each string contains 'ba'
print("Contains 'ba':", df_str["s"].str.contains("ba"))
# Extract the first word from each string using a regex pattern with the extract method
# The regex pattern '\\w+' matches one or more word characters (equivalent to [a-zA-Z0-9_])
# The second argument 0 specifies that we want to extract the first match
print("Extract word:", df_str["s"].str.extract(r"\\w+", 0))

# Datetime methods: Extract components from datetime columns
# Create a DataFrame with a datetime column using the date_range function
# The date_range function generates a range of dates from '2024-01-01' to '2024-01-05' with a daily interval
# Use eager=True to get a Series instead of an Expr
df_dt = pl.DataFrame({"d": pl.date_range(start=datetime.date(2024, 1, 1), end=datetime.date(2024, 1, 5), interval="1d", eager=True)})
# Extract the year from each date using the year method
# This operation returns a Series of integers representing the year of each date
print("Year:", df_dt["d"].dt.year())
# Extract the weekday (0=Monday, 6=Sunday) from each date using the weekday method
# This operation returns a Series of integers representing the weekday of each date
print("Weekday:", df_dt["d"].dt.weekday())

# Categorical methods: Work with categorical (factor-like) columns
# Create a DataFrame with a categorical column
# The cast method is used to convert the column to categorical type
df_cat = pl.DataFrame({"c": ["a", "b", "a"]}).with_columns(pl.col("c").cast(pl.Categorical))
# print("Set ordered:", df_cat["c"].cat.set_ordered(True))  # Removed: not supported in Polars
# Get the list of categories using the get_categories method
# This operation returns a list of unique categories in the categorical column
print("Get categories:", df_cat["c"].cat.get_categories())

# List methods: Operate on columns of lists
# Create a DataFrame with a list column
df_list = pl.DataFrame({"l": [[1, 2], [3], []]})
# Get the length of each list using the len method
# This operation returns a Series of integers representing the length of each list
print("List lengths:", df_list["l"].list.len())
# Check if each list contains the value 2 using the contains method
# This operation returns a boolean mask indicating whether each list contains 2
print("List contains 2:", df_list["l"].list.contains(2))
# Safely get index 0 from each list using a list comprehension
print("List get index 0:", [x[0] if x else None for x in df_list["l"].to_list()])  # Robust for all Polars versions
