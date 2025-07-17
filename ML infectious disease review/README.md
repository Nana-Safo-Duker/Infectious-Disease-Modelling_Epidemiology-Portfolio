# ML infectious disease review

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
- Topic: ML infectious disease review
- Primary paper/source: https://www.researchgate.net/publication/391426782_AI_and_Machine_Learning_for_Early_Detection_of_Infectious_Diseases_in_the_US_Opportunities_and_Challenges

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
