import os
import polars as pl

# Set up the path to the datasets directory relative to this script
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load raw transactions with datetime parsing
# try_parse_dates is deprecated in Polars, but left here for older versions
# For newer Polars, remove try_parse_dates and parse dates explicitly later
tx = pl.read_csv(f"{datasets_dir}/transactions.csv", try_parse_dates=True)
# Read the transaction CSV file into a Polars DataFrame

# Print the number of loaded records for initial verification
print(f"Loaded records: {tx.shape[0]}")

# Remove any records with null values and filter out negative transaction amounts
# This ensures only valid, positive transactions are kept
tx_clean = tx.drop_nulls().filter(pl.col('amount') > 0)

# If the 'date' column is a string, parse it into a Datetime type and round amounts
if tx_clean['date'].dtype == pl.String:
    tx_clean = tx_clean.with_columns([
        pl.col('amount').round(2).alias('amount'),  # Round transaction amounts to 2 decimal places
        pl.col('date').str.strptime(pl.Datetime, format='%Y-%m-%dT%H:%M:%S%.f').alias('date')  # Parse date strings to Datetime
    ])
else:
    # If already Datetime, just round amounts
    tx_clean = tx_clean.with_columns([
        pl.col('amount').round(2).alias('amount')
    ])

# Print the number of cleaned records and show the first few rows for verification
print(f"Cleaned records: {tx_clean.shape[0]}")
print(tx_clean.head())

# Save the cleaned transactions to a new CSV file for downstream use
# This is the output after cleaning and type conversion
tx_clean.write_csv(f"{datasets_dir}/cleaned_transactions.csv")
# Write the cleaned DataFrame to CSV