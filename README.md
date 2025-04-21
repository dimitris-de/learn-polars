# Polars Learning Path

Welcome to the **Polars Learning Path**, a comprehensive, hands-on curriculum for data engineers and analysts to master the [Polars](https://www.pola.rs) library using realistic finance (wealth management) use cases.

## 🎯 Who is this for?

- Data engineers and analysts new to Polars
- Financial domain professionals looking to leverage Polars for large-scale data processing
- Anyone seeking performance improvements and modern best practices over pandas

## 🚀 Roadmap & Structure

This repository is organized into progressive modules, each with Python scripts and Jupyter notebooks:

1. **Beginner** (`01_basics/`): Core data cleaning, transformations, joining, and lazy vs eager comparisons.
2. **Intermediate** (`02_intermediate/`): Time series processing, rolling statistics, portfolio performance, return attribution, and nested data.
3. **Advanced** (`03_advanced/`): VaR & stress testing, LazyFrame optimizations, pandas vs Polars benchmarks.
4. **Extra Topics** (`04_Extra/`):
   - Covers advanced and niche Polars features not in the main tutorials.
   - Includes DataFrame/Series meta-info, advanced selection, Arrow/NumPy export, and more.
   - Demonstrates robust handling of lists, categoricals, and datetimes, with up-to-date API usage and compatibility fixes.
   - Each topic is explained with runnable scripts and companion notebooks.

---

## 🧹 Clear All Notebook Outputs (One Command)

> **Keep your notebooks clean before sharing or committing!**
> 
> Remove all cell outputs from every notebook in the project (without deleting your code or text) by running:
>
> ```bash
> find . -type f -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace --to notebook {} +
> ```
>
> This is safe: it only clears outputs and execution counts, making version control and collaboration easier.

---

## 🧑‍💻 Features & Best Practices

- **Robust, Up-to-date Polars Usage:**
  - All code is compatible with the latest Polars API (as of 2025), including safe list/categorical/datetime operations.
  - Deprecated methods are replaced and edge cases (e.g., empty lists, missing categories) are handled gracefully.
- **Finance-focused Examples:**
  - All scenarios use realistic finance data (wealth management, portfolios, transactions, risk analysis).
- **Code Quality & Linting:**
  - Markdown and Python code are linted for clarity and consistency.
  - Notebooks and scripts are regularly validated for reproducibility.
- **Troubleshooting & Debugging:**
  - Common Polars errors are explained and resolved in context.
  - Inline comments and markdown cells clarify complex operations.

## 👩‍💻 Beginner-Friendly Instructions

### Opening and Running Notebooks

1. **Install Jupyter** (if you haven't already):
   - Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux).
   - Run:

     ```bash
     pip install notebook
     ```

2. **Start Jupyter Notebook:**
   - In the terminal, navigate to the project folder (e.g., `cd polars-in-finance`).
   - Run:

     ```bash
     jupyter notebook
     ```

   - This will open a web page. Click on any `.ipynb` file (notebook) to open and run it.
3. **Run All Cells:**
   - In the notebook, click `Cell` > `Run All` to execute all code and see the results.

### Clearing All Notebook Outputs (Safe for Version Control)

To remove all code outputs (but keep your code and text) from every notebook in the project, run this command in your project folder:

```bash
find . -type f -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace --to notebook {} +
```

- **What does this do?**
  - It clears all cell outputs and execution counts, making notebooks cleaner for sharing or version control.
  - **It does NOT delete any code or text!**
- **Why do this?**
  - Keeps the repository tidy and avoids large, unnecessary diffs in Git.

### Tips for Non-Technical Users

- You only need to use a few simple commands (shown above).
- No need to install extra software beyond Python and Jupyter.
- If you get stuck, search for error messages or ask for help in the repo's Issues section.

## 📂 Getting Started

### Creating and Using a Python Virtual Environment

It is best practice to use a virtual environment for Python projects. This keeps your dependencies isolated and avoids conflicts with other projects.

1. **Open a terminal and navigate to your project folder:**

   ```bash
   cd polars-in-finance
   ```

2. **Create a virtual environment named `.venv`:**

   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **On Mac/Linux:**

     ```bash
     source .venv/bin/activate
     ```

   - **On Windows:**

     ```bash
     .venv\Scripts\activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **When finished, deactivate the environment:**

   ```bash
   deactivate
   ```

### Prerequisites

1. Python 3.8+
2. Clone this repository to your local machine

### Installation

```bash
# Install all dependencies
pip install -r requirements.txt
```

### Running the Tutorials

- Launch JupyterLab or Jupyter Notebook to explore `.ipynb` files interactively.
- Or run the Python scripts directly for quick demonstrations:

  ```bash
  python 01_basics/01_dataframe_basics.py
  ```

- The `04_Extra/` folder contains additional scripts and notebooks for advanced Polars features.

## 🤝 Contributing & Feedback

Contributions, bug reports, and suggestions are welcome! Please open an issue or submit a pull request.

---

**Happy learning and analyzing with Polars!**
