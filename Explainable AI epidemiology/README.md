# Explainable AI epidemiology

A comprehensive AI/ML epidemiology project focused on **Explainable AI epidemiology**. This folder provides reproducible implementations in both Python and R, plus a detailed notebook workflow for exploratory analysis, statistical validation, and transparent reporting.

## Table of Contents
- [Overview](#overview)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data and Methodology](#data-and-methodology)
- [Modeling and Evaluation](#modeling-and-evaluation)
- [Outputs](#outputs)
- [Reproducibility](#reproducibility)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## Overview
This project is part of the Infectious Disease Modelling and Epidemiology Portfolio and is designed to demonstrate practical machine learning workflows for infectious disease intelligence. It combines descriptive statistics, inferential analysis, and predictive modeling scaffolds to support surveillance and decision-focused analytics.

**Research Focus:** Explainable AI epidemiology  
**Primary paper/source:** https://www.researchgate.net/publication/398850526_AI_Epidemiology_achieving_explainable_AI_through_expert_oversight_patterns

## Objectives
- Build a clear and reproducible analysis workflow for Explainable AI epidemiology.
- Provide dual-language implementation parity (Python and R).
- Generate interpretable outputs for epidemiology reporting.
- Support educational, research, and portfolio demonstration use cases.

## Key Features
- **Dual implementation:** Python (`analysis_pipeline.py`) and R (`analysis_pipeline.R`).
- **Notebook workflow:** `detailed_review_notebook.ipynb` for step-by-step analysis.
- **Statistical testing scaffold:** summary statistics and group-comparison testing.
- **Deterministic examples:** fixed random seeds for reproducible synthetic runs.
- **Repository hygiene:** `.gitignore`, `.gitattributes`, `LICENSE`, and dependency file.

## Project Structure
```text
.
├── README.md
├── Guidelines_Research_Paper_Review.txt
├── Scientific_Blog_Post.md
├── analysis_pipeline.py
├── analysis_pipeline.R
├── detailed_review_notebook.ipynb
├── requirements.txt
├── .gitignore
├── .gitattributes
├── LICENSE
└── outputs/                           # Created after execution
    ├── summary_statistics.csv
    ├── t_test_result.csv
    ├── summary_statistics_r.csv
    ├── t_test_result_r.csv
    └── signal_plot_r.png
```

## Installation
### Python setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### R setup
Install required R libraries if needed:
```r
install.packages(c("dplyr", "ggplot2", "readr"))
```

### Notebook setup (optional)
```bash
pip install jupyter
jupyter notebook
```

## Usage
### Run Python pipeline
```bash
python analysis_pipeline.py
```

### Run R pipeline
```bash
Rscript analysis_pipeline.R
```

### Run notebook
Open `detailed_review_notebook.ipynb` and execute all cells from top to bottom.

## Data and Methodology
- If `data/dataset.csv` exists, the pipelines ingest it directly.
- If data is unavailable, synthetic data is generated for demonstration.
- Core workflow:
  1. Data loading and basic quality checks.
  2. Descriptive summary statistics.
  3. Group-based inferential testing (Welch t-test scaffold).
  4. Export of reproducible result artifacts.

> Note: Replace synthetic inputs with properly licensed and validated epidemiology datasets before drawing operational conclusions.

## Modeling and Evaluation
This scaffold emphasizes reproducible epidemiology analytics and reporting primitives:
- Distribution summaries and exploratory diagnostics.
- Group-level significance testing.
- Cross-language (Python/R) result consistency checks.
- Re-runnable outputs for comparative reruns.

Recommended extension paths:
- Add time-series forecasting models (ARIMA, Prophet, LSTM, temporal transformers).
- Add geospatial features and county/district-level covariates.
- Add model explainability methods (SHAP, permutation importance, partial dependence).
- Add robust validation (rolling windows, temporal CV, calibration metrics).

## Outputs
After execution, expected artifacts include:
- `outputs/summary_statistics.csv`
- `outputs/t_test_result.csv`
- `outputs/summary_statistics_r.csv`
- `outputs/t_test_result_r.csv`
- `outputs/signal_plot_r.png`

These files can be used for documentation, quick QA checks, and side-by-side rerun comparisons.

## Reproducibility
- Fixed random seeds are used for deterministic synthetic examples.
- Python and R pipelines mirror the same logical workflow.
- README + notebook + scripts provide both narrative and executable reproducibility.
- Keep dependency versions current in `requirements.txt` and R package declarations.

## Contributing
Contributions are welcome.

1. Create a feature branch:
   ```bash
   git checkout -b feature/<feature-name>
   ```
2. Keep changes scoped to this folder where possible.
3. Update this README when methods or outputs change.
4. Validate by running Python and R pipelines.
5. Open a pull request with a concise summary of methods and results.

## License
This project is released under the MIT License. See `LICENSE` for details.

## References
1. Primary paper/source: https://www.researchgate.net/publication/398850526_AI_Epidemiology_achieving_explainable_AI_through_expert_oversight_patterns
2. Add additional peer-reviewed references relevant to Explainable AI epidemiology.
3. Include dataset citations and license terms when integrating external data.

## Disclaimer
This project is for research, learning, and portfolio demonstration. It is not a clinical decision-support system and should not be used for medical decision-making without domain validation, governance review, and regulatory compliance.
