# Deep learning for malaria parasite detection

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
- Topic: Deep learning for malaria parasite detection
- Primary paper/source: https://www.researchgate.net/publication/388530278_Deep_learning-based_malaria_parasite_detection_convolutional_neural_networks_model_for_accurate_species_identification_of_Plasmodium_falciparum_and_Plasmodium_vivax

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
