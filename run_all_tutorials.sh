#!/bin/bash
set -e

# Activate virtual environment
if [ ! -d ".venv" ]; then
  echo "Virtual environment not found! Please create it first."
  exit 1
fi
source .venv/bin/activate

echo "Generating datasets..."
python datasets/generate_datasets.py

echo "Running basic tutorials..."
python 01_basics/01_data_cleaning.py
python 01_basics/02_joining_and_filtering.py
python 01_basics/03_lazy_vs_eager.py

echo "Running intermediate tutorials..."
python 02_intermediate/01_time_series_and_rolling.py
python 02_intermediate/02_portfolio_performance.py
python 02_intermediate/03_return_attribution.py
python 02_intermediate/04_nested_data_and_explode.py

echo "Running advanced tutorials..."
python 03_advanced/01_var_and_stress_testing.py
python 03_advanced/02_lazyframe_optimizations.py
python 03_advanced/03_performance_benchmarks_vs_pandas.py

echo "Converting and executing Jupyter notebooks..."
jupyter nbconvert --execute --to notebook --inplace 01_basics/*.ipynb
jupyter nbconvert --execute --to notebook --inplace 02_intermediate/*.ipynb
jupyter nbconvert --execute --to notebook --inplace 03_advanced/*.ipynb
jupyter nbconvert --execute --to notebook --inplace 04_extra/*.ipynb

# Run all scripts in 04_Extra
for script in ./04_Extra/*.py; do
    echo "Running $script"
    python "$script"
done

echo "All tutorials completed successfully!"