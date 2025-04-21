import os
import polars as pl
import matplotlib.pyplot as plt

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load benchmark returns
benchmarks = pl.read_csv(f"{datasets_dir}/benchmarks.csv")

# Parse date column to Datetime
benchmarks = benchmarks.with_columns([
    pl.col('date').str.strptime(pl.Datetime, format='%Y-%m-%dT%H:%M:%S%.f').alias('date')
])

# Sort by date
benchmarks = benchmarks.sort('date')

# 7-day rolling mean and 30-day rolling std
rolling_stats = benchmarks.with_columns([
    pl.col('benchmark_return').rolling_mean(window_size=7).alias('rolling_mean_7d'),
    pl.col('benchmark_return').rolling_std(window_size=30).alias('rolling_std_30d')
])

print(rolling_stats.tail())

# Calculate exponentially weighted moving average (EWMA)
rolling_stats = rolling_stats.with_columns([
    pl.col('benchmark_return').ewm_mean(alpha=0.2).alias('ewma_alpha_0.2')
])

# Save rolling stats
rolling_stats.write_parquet(f"{datasets_dir}/rolling_benchmarks.parquet")