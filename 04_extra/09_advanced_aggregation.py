"""
09_advanced_aggregation.py
Demonstrates advanced aggregation: quantile, product, std, var, mean_horizontal, sum_horizontal, min_horizontal, max_horizontal.

This script demonstrates advanced aggregation operations in Polars. Each operation is explained for educational clarity.
"""
import polars as pl

# Create a sample DataFrame with three columns 'a', 'b', 'c' and four rows.
df = pl.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [5, 6, 7, 8],
    "c": [9, 10, 11, 12]
})

# Compute the 0.5 quantile (median) of column 'a'. 
# The quantile operation returns a value below which a given percentage of the data falls.
print("Quantile (0.5) for column 'a':", df["a"].quantile(0.5))

# Compute the product of all values in column 'a'. 
# The product operation returns the result of multiplying all values in the column.
print("Product of column 'a':", df["a"].product())

# Compute the standard deviation and variance of column 'a'. 
# The standard deviation measures the amount of variation or dispersion of a set of values.
# The variance measures the average of the squared differences from the Mean.
print("Std of column 'a':", df["a"].std())
print("Var of column 'a':", df["a"].var())

# The following operations compute aggregations across columns for each row (i.e., horizontally).
# mean_horizontal: Compute the mean of all values in each row.
# sum_horizontal: Compute the sum of all values in each row.
# min_horizontal: Compute the minimum of all values in each row.
# max_horizontal: Compute the maximum of all values in each row.
print("Mean horizontal:", df.mean_horizontal())
print("Sum horizontal:", df.sum_horizontal())
print("Min horizontal:", df.min_horizontal())
print("Max horizontal:", df.max_horizontal())
