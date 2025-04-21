# datasets/generate_datasets.py

import os
import polars as pl
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(__file__)

def generate_transactions(n=1000):
    client_ids = [f"C{i:04d}" for i in range(100)]
    asset_ids = [f"A{i:04d}" for i in range(50)]
    df = pl.DataFrame({
        "transaction_id": [f"T{i:06d}" for i in range(n)],
        "client_id": np.random.choice(client_ids, size=n),
        "asset_id": np.random.choice(asset_ids, size=n),
        "amount": np.round(np.random.normal(10000, 5000, size=n),2),
        "date": pd.date_range("2020-01-01", periods=n, freq="h")
    })
    df.write_csv(os.path.join(BASE_DIR, "transactions.csv"))

def generate_clients(n=100):
    df = pl.DataFrame({
        "client_id": [f"C{i:04d}" for i in range(n)],
        "name": [f"Client {i}" for i in range(n)],
        "join_date": pd.date_range("2018-01-01", periods=n, freq="D")
    })
    df.write_csv(os.path.join(BASE_DIR, "clients.csv"))

def generate_assets(n=50):
    df = pl.DataFrame({
        "asset_id": [f"A{i:04d}" for i in range(n)],
        "asset_type": np.random.choice(["Equity","Bond","Commodity"], size=n),
        "region": np.random.choice(["US","EU","APAC"], size=n),
        "price": np.round(np.random.normal(100, 20, size=n),2)
    })
    df.write_parquet(os.path.join(BASE_DIR, "assets.parquet"))

def generate_benchmarks(n=365):
    dates = pd.date_range("2020-01-01", periods=n, freq="D")
    df = pl.DataFrame({
        "date": dates,
        "benchmark_return": np.round(np.random.normal(0.0005, 0.002, size=n),6)
    })
    df.write_csv(os.path.join(BASE_DIR, "benchmarks.csv"))

if __name__ == "__main__":
    generate_transactions()
    generate_clients()
    generate_assets()
    generate_benchmarks()
    print("Dummy datasets generated in 'datasets/' folder.")
