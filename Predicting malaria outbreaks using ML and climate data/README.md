# Predicting malaria outbreaks using ML and climate data

This folder contains a complete, reproducible scaffold for reviewing a research paper in infectious disease AI/ML, following `Guidelines_Research_Paper_Review.txt`.

## Included Files
- `Guidelines_Research_Paper_Review.txt`
- `Scientific_Blog_Post.md`
- `.gitattributes`
- `.gitignore`
- `LICENSE`
- `requirements.txt`
- `analysis_pipeline.py`
- `analysis_pipeline.R`
- `detailed_review_notebook.ipynb`

## Research Focus
- Topic: Predicting malaria outbreaks using ML and climate data
- Primary paper/source: https://www.researchgate.net/publication/378298118_Predicting_malaria_prevalence_with_machine_learning_models_using_satellite-based_climate_information

## Python Quickstart
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python analysis_pipeline.py
```

## R Quickstart
```r
source("analysis_pipeline.R")
```

## Reproducibility Notes
- Random seeds are fixed for deterministic synthetic examples.
- Replace synthetic inputs with real study data when available.
