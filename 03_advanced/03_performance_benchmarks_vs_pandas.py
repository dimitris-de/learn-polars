import os
import polars as pl
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

def benchmark(name, polars_fn, pandas_fn, repeat=5):
    """Run benchmark comparing polars vs pandas performance"""
    
    # Warm up
    polars_fn()
    pandas_fn()
    
    # Benchmark Polars
    polars_times = []
    for _ in range(repeat):
        start = time.time()
        polars_fn()
        polars_times.append(time.time() - start)
    
    # Benchmark Pandas
    pandas_times = []
    for _ in range(repeat):
        start = time.time()
        pandas_fn()
        pandas_times.append(time.time() - start)
    
    # Calculate average times
    polars_avg = sum(polars_times) / repeat
    pandas_avg = sum(pandas_times) / repeat
    speedup = pandas_avg / polars_avg
    
    print(f"\n{name} Benchmark:")
    print(f"Polars: {polars_avg:.4f}s")
    print(f"Pandas: {pandas_avg:.4f}s")
    print(f"Speedup: {speedup:.2f}x")
    
    return {
        "name": name,
        "polars_time": polars_avg,
        "pandas_time": pandas_avg,
        "speedup": speedup
    }

# BENCHMARK 1: DATA LOADING
# ========================
def polars_load():
    df = pl.read_csv(f"{datasets_dir}/transactions.csv")
    return df

def pandas_load():
    df = pd.read_csv(f"{datasets_dir}/transactions.csv")
    return df

load_result = benchmark("Data Loading", polars_load, pandas_load)

# BENCHMARK 2: FILTERING
# =====================
# Load data for filtering benchmark
polars_df = pl.read_csv(f"{datasets_dir}/transactions.csv")
pandas_df = pd.read_csv(f"{datasets_dir}/transactions.csv")

def polars_filter():
    return polars_df.filter(pl.col("amount") > 5000)

def pandas_filter():
    return pandas_df[pandas_df["amount"] > 5000]

filter_result = benchmark("Filtering", polars_filter, pandas_filter)

# BENCHMARK 3: GROUPBY & AGGREGATION
# =================================
def polars_groupby():
    return polars_df.group_by("client_id").agg(pl.sum("amount").alias("total_amount"))

def pandas_groupby():
    return pandas_df.groupby("client_id")["amount"].sum().reset_index()

groupby_result = benchmark("GroupBy & Aggregation", polars_groupby, pandas_groupby)

# Show groupby results
group_res = polars_groupby()
print(f"\nUnique groups: {group_res.shape[0]} clients")

# BENCHMARK 4: JOIN OPERATION
# ==========================
clients_pl = pl.read_csv(f"{datasets_dir}/clients.csv")
clients_pd = pd.read_csv(f"{datasets_dir}/clients.csv")

def polars_join():
    return polars_df.join(clients_pl, on="client_id")

def pandas_join():
    return pandas_df.merge(clients_pd, on="client_id")

join_result = benchmark("Join Operation", polars_join, pandas_join)

# VISUALIZATION OF RESULTS
# =======================
results = [load_result, filter_result, groupby_result, join_result]

names = [r["name"] for r in results]
polars_times = [r["polars_time"] for r in results]
pandas_times = [r["pandas_time"] for r in results]
speedups = [r["speedup"] for r in results]

# Create table of results
results_df = pl.DataFrame({
    "operation": names,
    "polars_time": polars_times,
    "pandas_time": pandas_times,
    "speedup": speedups
})

print("\nBenchmark Results Summary:")
print(results_df)

# Save results
results_df.write_csv(f"{datasets_dir}/benchmark_results.csv")