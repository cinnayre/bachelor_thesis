# Bachelor Thesis — Repository

**Project:** Repository of code and analyses for a Bachelor thesis.

**Status:** Final code and analysis scripts used to produce the results in the thesis.

---

## Overview ✅

This repository contains the code, notebooks, and scripts used to compute project- and commit-level software metrics for a bachelor thesis. It is organised to allow reproduction of the data preparation, metric calculation, and visualization steps used in the study.

## Contents 🔧

- `main.py` — entry point for creating dataframes workflows.
- `dataframe_utils.py`, `util.py` — utility modules.
- `metrics_calculation/` — modules that compute project and commit level metrics.
- `visualization/` — plotting utilities and Jupyter notebooks for figures.
- `output/` — generated datasets and interim results (CSV files).
- `*.ipynb` — analysis notebooks (exploratory analysis and plots).
- `helpers/project_config.py` contains paths and constants

## Requirements ⚙️

- Python 3.8+ (recommended)
- Typical data-science packages: pandas, numpy, matplotlib, seaborn 

## Usage ▶️

1. Prepare the dataset and place input files in `output/` or an agreed data folder.
2. Run `python main.py` to execute the main pipeline (or run notebooks interactively for analysis and figures).
3. Check `output/interim_results/` for generated CSVs and `visualization/plots/` for figures.

> Note: Some scripts expect cleaned/normalized datasets to be present in `output/` — see notebooks for step-by-step processing.

