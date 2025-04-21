import os
import polars as pl
import numpy as np
import matplotlib.pyplot as plt

# Locate datasets directory
datasets_dir = os.path.abspath(os.path.join(__file__, '..', '..', 'datasets'))

# Load benchmark returns for our analysis
benchmarks = pl.read_csv(f"{datasets_dir}/benchmarks.csv")
benchmarks = benchmarks.with_columns([
    pl.col("date").str.strptime(pl.Datetime, format="%Y-%m-%dT%H:%M:%S%.f").alias("date")
])

# 1. PORTFOLIO CONSTRUCTION WITH MULTIPLE ASSETS
# ==============================================
# Create a synthetic portfolio with 3 assets and random weights
np.random.seed(42)  # For reproducibility
portfolio_value = 1000000  # $1M portfolio

# Simulate 3 assets with correlation to benchmark
asset_returns = benchmarks.select([
    pl.col("date"),
    (pl.col("benchmark_return") * 1.2 + np.random.normal(0, 0.001, benchmarks.height))
    .alias("asset1_return"),
    (pl.col("benchmark_return") * 0.8 + np.random.normal(0, 0.002, benchmarks.height))
    .alias("asset2_return"),
    (pl.col("benchmark_return") * 0.5 + np.random.normal(0, 0.003, benchmarks.height))
    .alias("asset3_return")
])

# Portfolio weights
weights = np.array([0.5, 0.3, 0.2])  # 50% in asset1, 30% in asset2, 20% in asset3

# Calculate portfolio returns
portfolio_returns = asset_returns.with_columns([
    (weights[0] * pl.col("asset1_return") + 
     weights[1] * pl.col("asset2_return") + 
     weights[2] * pl.col("asset3_return")).alias("portfolio_return")
])

# Convert returns to dollar change
portfolio_returns = portfolio_returns.with_columns([
    (pl.col("portfolio_return") * portfolio_value).alias("dollar_change")
])


# 2. VALUE AT RISK (VaR) CALCULATION
# =================================
# Historical VaR at 95% confidence level (5% worst case)
var_95 = portfolio_returns.select([
    pl.col("dollar_change").quantile(0.05).alias("VaR_95")
])[0, 0]

print(f"1-day Value at Risk (95% confidence): ${-var_95:.2f}")

# VaR at 99% confidence level (1% worst case)
var_99 = portfolio_returns.select([
    pl.col("dollar_change").quantile(0.01).alias("VaR_99")
])[0, 0]

print(f"1-day Value at Risk (99% confidence): ${-var_99:.2f}")

# Group by asset type for VaR attribution
returns = pl.concat([
    portfolio_returns.with_columns([
        pl.lit("asset1").alias("asset_type"),
        pl.col("asset1_return").alias("return")
    ]),
    portfolio_returns.with_columns([
        pl.lit("asset2").alias("asset_type"),
        pl.col("asset2_return").alias("return")
    ]),
    portfolio_returns.with_columns([
        pl.lit("asset3").alias("asset_type"),
        pl.col("asset3_return").alias("return")
    ])
], how="vertical")

var_by_type = returns.group_by("asset_type").agg([
    pl.col("return").std().alias("std_return"),
    pl.col("return").mean().alias("mean_return")
])
print("VaR by Asset Type:")
print(var_by_type)


# 3. STRESS TESTING
# ================
# Define stress scenarios
stress_scenarios = [
    ("Market Crash", -0.07),           # -7% daily return
    ("Tech Bubble", -0.04),            # -4% daily return
    ("Interest Rate Shock", -0.025),   # -2.5% daily return
    ("Normal Volatility", -0.01)       # -1% daily return
]

# Apply stress scenarios
stress_results = []
for scenario, shock in stress_scenarios:
    dollar_impact = shock * portfolio_value
    stress_results.append({"scenario": scenario, "return": shock, "dollar_impact": dollar_impact})

# Convert to Polars DataFrame
stress_df = pl.DataFrame(stress_results)
print("\nStress Test Results:")
print(stress_df)

# Save results
portfolio_returns.write_csv(f"{datasets_dir}/portfolio_returns.csv")
stress_df.write_csv(f"{datasets_dir}/stress_test_results.csv")