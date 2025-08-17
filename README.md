# Infectious Disease Modelling & Epidemiology Portfolio

Multi-project laboratory of AI/ML workflows for infectious disease analytics created by Nana Safo-Duker. Each folder is a self-contained project combining epidemiological reasoning, statistical testing, and machine learning to support outbreak understanding, surveillance planning, and public-health decision support.

This README provides the cross-project narrative for the repository: what is included, how to run it reproducibly, and how each project contributes to a broader computational epidemiology portfolio.

## Table of Contents

- [About](#about)
- [Portfolio Overview](#portfolio-overview)
- [Repository Layout](#repository-layout)
- [Technology Stack](#technology-stack)
- [Shared Setup Workflow](#shared-setup-workflow)
- [Workflow Blueprint](#workflow-blueprint)
- [Project Capsules](#project-capsules)
- [Data Sources and Governance](#data-sources-and-governance)
- [Reproducibility and Validation](#reproducibility-and-validation)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Contact](#contact)

## About

This repository is a comprehensive AI/ML epidemiology portfolio built to demonstrate practical, reproducible infectious-disease analytics across multiple public-health scenarios. The projects connect statistical epidemiology, machine learning, and interpretable modeling to support outbreak forecasting, transmission pattern analysis, and surveillance strategy development.

**Description:** Multi-project infectious disease analytics portfolio spanning Bayesian outbreak prediction, malaria and vector-borne disease modeling, respiratory surveillance, digital epidemiology, explainable AI workflows, and spatiotemporal epidemic modeling.

**Repository:** [Infectious-Disease-Modelling_Epidemiology-Portfolio](https://github.com/Nana-Safo-Duker/Infectious-Disease-Modelling_Epidemiology-Portfolio)

**Website:** [https://nana-safo-duker.github.io/](https://nana-safo-duker.github.io/)

**Mission:** Build transparent, reusable computational workflows that can be adapted for infectious disease research, education, and decision-support prototyping.

**Topics:** infectious disease modeling, epidemiology, public health AI, outbreak forecasting, malaria analytics, respiratory surveillance, Bayesian inference, explainable AI, spatiotemporal modeling, transmission modeling, bioinformatics.

## Portfolio Overview

- **Disciplines represented:** outbreak prediction, vector-borne disease analytics, digital surveillance, epidemiological statistics, explainable ML, and climate-informed malaria forecasting.
- **Languages and runtimes:** Python 3.10+, R 4.x, Jupyter Notebooks (`.ipynb`), script-based pipelines (`.py`, `.R`).
- **Method families:** descriptive statistics, inferential testing (t-tests), feature-based ML pipelines, deterministic synthetic data scaffolds for reproducibility.
- **Deliverables per project:** repository files (`.gitattributes`, `.gitignore`, `LICENSE`, `requirements.txt`), runnable notebook, Python pipeline, R pipeline, project README.
- **Operational structure:** independent project folders that can be run in isolation while preserving a consistent portfolio pattern.

## Repository Layout

```text
Infectious-Disease-Modelling_Epidemiology-Portfolio/
├── Bayesian ML outbreak prediction/
├── Deep learning for malaria parasite detection/
├── Deep learning vector diseases/
├── Digital epidemiology ML/
├── Explainable AI epidemiology/
├── Malaria-Transmission-Model-Madagascar/
├── ML infectious disease review/
├── Predicting malaria outbreaks using ML and climate data/
├── Respiratory AI surveillance/
├── Spatiotemporal epidemic ML/
├── TB transmission ML modeling/
└── README.md
```

For the 10 newly scaffolded folders, each project follows a consistent pattern:

- `README.md` for project-specific context and quickstart.
- `analysis_pipeline.py` for Python-based workflow execution.
- `analysis_pipeline.R` for R-based workflow execution.
- `detailed_review_notebook.ipynb` for notebook walkthrough.
- `requirements.txt` for Python dependencies.
- `.gitattributes`, `.gitignore`, and `LICENSE` for repository hygiene.

## Technology Stack

| Layer | Tooling | Role in This Portfolio |
|---|---|---|
| Programming | Python, R | Parallel analytics implementations across projects |
| Data science libraries | `numpy`, `pandas`, `scipy`, `dplyr`, `ggplot2`, `readr` | Data handling, statistical testing, visualization |
| Notebooks | Jupyter Notebook | Reproducible, narrative analysis execution |
| Project packaging | `requirements.txt`, repository scaffolding files | Deterministic setup and clean version control behavior |
| Output artifacts | CSV summaries and generated figures in `outputs/` | Reproducible statistics and visual diagnostics |

## Shared Setup Workflow

Clone once, then run any project folder independently.

```bash
git clone https://github.com/Nana-Safo-Duker/Infectious-Disease-Modelling_Epidemiology-Portfolio.git
cd Infectious-Disease-Modelling_Epidemiology-Portfolio
```

### Python setup (per project)

```bash
cd "<project-folder>"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python analysis_pipeline.py
```

### R setup (per project)

```r
source("analysis_pipeline.R")
```

### Notebook execution

```bash
jupyter notebook
```

Open `detailed_review_notebook.ipynb` inside the chosen project folder and run all cells.

## Workflow Blueprint

1. **Select a disease focus** from the project capsules below.
2. **Provision environment** (Python and/or R) inside that project folder.
3. **Run the notebook** to inspect workflow assumptions and outputs.
4. **Run scripts** (`analysis_pipeline.py` and `analysis_pipeline.R`) for automated reproduction.
5. **Review outputs** (summary statistics, test results, and visualizations) for interpretation and reporting.
6. **Replace synthetic inputs** with approved real-world epidemiology data before production-level conclusions.

## Project Capsules

### 1) Bayesian ML outbreak prediction
- **Focus:** Bayesian-inspired outbreak risk modeling and uncertainty-aware interpretation.
- **Utility:** supports probabilistic reasoning for surveillance and early-warning discussions.
- **Assets:** `analysis_pipeline.py`, `analysis_pipeline.R`, `detailed_review_notebook.ipynb`, project README.

### 2) Deep learning for malaria parasite detection
- **Focus:** malaria parasite detection concepts and model-oriented analytics framing.
- **Utility:** supports microscopy-adjacent AI workflows and classification experimentation.
- **Assets:** mirrored Python and R pipelines with notebook narrative.

### 3) Deep learning vector diseases
- **Focus:** vector-borne disease prediction patterns and ML workflow templates.
- **Utility:** supports risk scoring and trend interpretation in vector disease contexts.
- **Assets:** reproducible scripts and notebook with aligned project scaffolding.

### 4) Digital epidemiology ML
- **Focus:** digital-signal informed epidemiology and computational surveillance framing.
- **Utility:** supports modern surveillance strategy prototyping with data-driven indicators.
- **Assets:** cross-language scripts, notebook, and setup files.

### 5) Explainable AI epidemiology
- **Focus:** interpretability-first infectious disease modeling.
- **Utility:** improves communication of model behavior for policy and clinical stakeholders.
- **Assets:** reproducible scripts and notebook emphasizing interpretable analytical flow.

### 6) ML infectious disease review
- **Focus:** broad machine learning review workflow for infectious disease analytics.
- **Utility:** supports comparative evaluation of methods and reproducible review pipelines.
- **Assets:** complete repository-ready project package.

### 7) Predicting malaria outbreaks using ML and climate data
- **Focus:** climate-informed malaria outbreak forecasting.
- **Utility:** supports environmental covariate integration for outbreak preparedness.
- **Assets:** full Python/R/notebook stack with reproducibility files.

### 8) Respiratory AI surveillance
- **Focus:** respiratory disease surveillance modeling patterns.
- **Utility:** supports early signal detection and trend interpretation in respiratory outbreaks.
- **Assets:** consistent project scaffold for reproducible experiments.

### 9) Spatiotemporal epidemic ML
- **Focus:** spatial and temporal epidemic dynamics in ML pipelines.
- **Utility:** supports geographically-aware disease analytics and trend projection.
- **Assets:** reproducible scripts/notebook and repository support files.

### 10) TB transmission ML modeling
- **Focus:** tuberculosis transmission modeling via ML and statistical workflows.
- **Utility:** supports transmission pattern analysis and intervention planning exploration.
- **Assets:** full project scaffold aligned with repository standards.

### 11) Malaria-Transmission-Model-Madagascar
- **Focus:** dedicated malaria transmission project context already in this repository.
- **Utility:** complements the newer folders with a location-specific epidemiological case.
- **Assets:** existing project files maintained as part of the portfolio narrative.

## Data Sources and Governance

- All provided datasets and generated outputs should be treated as educational/research scaffolds unless explicitly documented otherwise.
- Replace placeholders and synthetic files with properly licensed, de-identified, or institution-approved data before real-world use.
- Do not commit sensitive health information, credentials, or API secrets.
- Use environment/config files for local secrets and ensure they are ignored via `.gitignore`.
- Follow institutional and legal requirements (IRB, HIPAA, GDPR, and local policy) for clinical or personally identifiable data.

## Reproducibility and Validation

- Random seeds are fixed in scripts where appropriate to support deterministic synthetic examples.
- Python and R parity enables cross-language result checks.
- CSV outputs from both pipelines provide basic regression anchors for reruns.
- Notebook plus script execution supports both exploratory and batch-style validation paths.
- Recommended next step: add CI notebook smoke tests and script checks via GitHub Actions.

## Contributing

1. Create a feature branch:
   ```bash
   git checkout -b feature/<feature-name>
   ```
2. Limit scope to one project folder per change when possible.
3. Update both the affected project `README.md` and this root `README.md` for structural updates.
4. Validate by running relevant scripts/notebooks and checking generated outputs.
5. Open a pull request summarizing methods, data assumptions, and evaluation evidence.

## Roadmap

- Expand each project from scaffold-level outputs to richer disease-specific datasets and model evaluations.
- Add explicit citations and dataset provenance documentation per project.
- Introduce shared utility modules for reusable preprocessing and evaluation logic.
- Add automated testing and linting for Python and R workflows.
- Publish versioned releases grouped by disease theme (malaria, respiratory, TB, outbreak forecasting).

## Contact

Questions, collaborations, or demonstration requests are welcome:

- Portfolio site: [https://nana-safo-duker.github.io/](https://nana-safo-duker.github.io/)
- Repository issues: open an issue in this repo for bugs, ideas, or enhancement requests.

**Last Updated**: August 2025
