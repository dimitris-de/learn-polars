# Polars Learning Path

Welcome to the **Polars Learning Path**, a comprehensive, hands‑on curriculum for data engineers and analysts to master the [Polars](https://www.pola.rs) library using realistic finance (wealth‑management) use‑cases.

## 🎯 Who is this for?

- Data engineers and analysts new to Polars
- Financial‑domain professionals looking to leverage Polars for large‑scale data processing
- Anyone seeking performance improvements and modern best practices over pandas

## 🚀 Roadmap & Structure

This repository is organized into progressive modules, each with Python scripts and Jupyter notebooks:

1. **Beginner** (`01_basics/`): Core data cleaning, transformations, joining, and lazy vs eager comparisons.  
2. **Intermediate** (`02_intermediate/`): Time‑series processing, rolling statistics, portfolio performance, return attribution, and nested‑data handling.  
3. **Advanced** (`03_advanced/`): VaR & stress testing, `LazyFrame` optimisations, pandas vs Polars benchmarks.  
4. **Extra Topics** (`04_Extra/`):  
   - Covers advanced and niche Polars features not in the main tutorials.  
   - Includes DataFrame/Series meta‑info, advanced selection, Arrow/NumPy export, and more.  
   - Demonstrates robust handling of lists, categoricals, and datetimes, with up‑to‑date API usage and compatibility fixes.  
   - Each topic is explained with runnable scripts and companion notebooks.

---

## 📡 One‑click Cloud Notebooks (Binder & Colab)

Sometimes you just want to try the notebooks without cloning anything locally. The two easiest ways are **Binder** (no account required) and **Google Colab** (requires a Google account, but gives you free GPUs).

### 2. Launch with Binder (zero sign‑in sandbox)

| | |
|---|---|
| **What it is** | mybinder.org builds a Docker image from this repo and gives you a temporary JupyterLab session. |
| **Who it’s for** | Learners who want to experiment quickly or follow a workshop/tutorial. |
| **Limitations** | The server is ephemeral (it vanishes when the browser tab closes) and has modest CPU/RAM quotas. |

#### How to use it

1. Click the badge below (or the identical badge at the top of every notebook):

   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dimitris-de/learn-polars/HEAD?urlpath=lab/tree/)

2. Wait ~30–60 seconds while Binder builds the image the first time (subsequent launches are faster).
3. When JupyterLab opens, navigate to any `*.ipynb` file and start running cells.

> **Badge for your own forks**  
> Replace with your actual GitHub username (or org) in the URL above and paste the markdown into your README.

### 3. Open in Google Colab (free GPUs/TPUs)

| | |
|---|---|
| **What it is** | Colab opens a ***copy*** of the notebook in your Google Drive (changes don’t touch this repo unless you explicitly save back). |
| **Who it’s for** | Users needing GPU/TPU acceleration or longer‑running kernels. |
| **Limitations** | Requires a Google account; sessions time out after 12 hours of idle time. |

#### How to use it

1. Click the **Open in Colab** badge next to the notebook you want:

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dimitris-de/learn-polars/blob/main/01_basics/01_dataframe_basics.ipynb)

   > Change the path in the link (`01_basics/01_dataframe_basics.ipynb`) to the notebook you’re interested in.
2. Colab will ask to **save a copy to Drive** (accepted by default).  
3. Choose **Runtime → Run all** or run cells individually.
4. To keep your results, the notebook auto‑saves in your Google Drive. If you want to contribute back, use **File → Save a copy to GitHub**.

---

## 🧹 Clear All Notebook Outputs (One Command)

> **Keep notebooks clean before sharing or committing!**  
> Remove all cell outputs from every notebook in the project (without deleting code or text) by running:
>
> ```bash
> find . -type f -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace --to notebook {} +
> ```
>
> This is safe: it only clears outputs and execution counts, making version control and collaboration easier.

---

## 🧑‍💻 Features & Best Practices

- **Robust, Up‑to‑date Polars Usage:**  
  All code is compatible with the latest Polars API (2025), including safe list/categorical/datetime operations.  
- **Finance‑focused Examples:** realistic data from wealth‑management scenarios.  
- **Code Quality & Linting:** notebooks and scripts are validated and linted.  
- **Troubleshooting & Debugging:** common Polars pitfalls explained inline.

## 👩‍💻 Beginner‑Friendly Instructions

### Opening and Running Notebooks Locally

1. **Install Jupyter:**

   ```bash
   pip install notebook
   ```

2. **Start Jupyter Notebook:**

   ```bash
   cd learn-polars
   jupyter notebook
   ```

3. In the browser page that opens, click any `.ipynb` file to explore.  
4. **Run All Cells:** `Cell → Run All`.

*(Prefer JupyterLab? Run `jupyter lab` instead.)*

### Clearing All Notebook Outputs (Safe for Version Control)

```bash
find . -type f -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace --to notebook {} +
```

*(Clears outputs only; never deletes code or markdown.)*

### Tips for Non‑Technical Users

- Only a few commands are needed (see above).
- No extra software beyond Python and Jupyter.
- If you get stuck, open an **Issue** in the repo.

## 📂 Getting Started Locally

### Creating and Using a Python Virtual Environment

```bash
cd learn-polars
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

When finished:

```bash
deactivate
```

### Prerequisites

1. Python 3.8+
2. Git clone of this repository

### Running the Tutorials Locally

```bash
# Interactive
jupyter lab   # or  jupyter notebook

# Or run scripts directly
python 01_basics/01_dataframe_basics.py
```

## 🤝 Contributing & Feedback

Contributions, bug reports, and suggestions are welcome! Please open an Issue or submit a pull request.

---

**Happy learning and analysing with Polars!**

