import os
import polars as pl
import numpy as np
import matplotlib.pyplot as plt

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load cleaned transactions and assets
tx = pl.read_csv(f"{datasets_dir}/cleaned_transactions.csv")
assets = pl.read_parquet(f"{datasets_dir}/assets.parquet")

# Join to get price info
df = tx.join(assets, on="asset_id", how="inner")

# Compute trade value = amount * price
df = df.with_columns((pl.col("amount") * pl.col("price")).alias("trade_value"))

# Ensure 'date' column is parsed as Datetime before extracting date part
if df['date'].dtype != pl.Datetime:
    df = df.with_columns(
        pl.col('date').str.strptime(pl.Datetime, format='%Y-%m-%dT%H:%M:%S%.f').alias('date')
    )
# Add a 'trade_date' column (extract date part from datetime)
df = df.with_columns(
    pl.col("date").dt.date().alias("trade_date")
)

# Aggregate daily total trade value
daily_perf = (
    df.group_by("trade_date")
      .agg([
          pl.sum("trade_value").alias("daily_trade_value"),
          pl.count().alias("num_trades")
      ])
      .sort("trade_date")
)

print("Daily performance sample:")
print(daily_perf.head())

# Calculate cumulative performance
daily_perf = daily_perf.with_columns([
    pl.cum_sum("daily_trade_value").alias("cumulative_value")
])

# Calculate daily returns
daily_perf = daily_perf.with_columns([
    (pl.col("daily_trade_value") / pl.col("cumulative_value").shift(1) * 100)
    .alias("daily_return_pct")
])

# Print performance metrics
avg_daily_return = daily_perf["daily_return_pct"].mean()
std_daily_return = daily_perf["daily_return_pct"].std()
sharpe = avg_daily_return / std_daily_return * np.sqrt(252)  # Annualized Sharpe

print(f"\nPortfolio Performance Metrics:")
print(f"Average Daily Return: {avg_daily_return:.2f}%")
print(f"Daily Volatility: {std_daily_return:.2f}%")
print(f"Annualized Sharpe Ratio: {sharpe:.2f}")

# Save results
daily_perf.write_csv(f"{datasets_dir}/portfolio_performance.csv")