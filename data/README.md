# Data Directory

This directory is for storing input data files for the malaria transmission model.

## Structure

```
data/
├── README.md           # This file
├── raw/                # Raw data files (optional)
└── processed/          # Processed data files (optional)
```

## Data Files

Currently, the model uses synthetic initial conditions. If you have real epidemiological data for Madagascar, place them here.

### Expected Data Format

If you want to use real data, CSV files should have the following structure:

**Population Data** (`population_data.csv`):
- `region`: Geographic region
- `population`: Total population
- `initial_infected`: Initial number of infected individuals

**ITN Coverage Data** (`itn_coverage.csv`):
- `year`: Year
- `coverage`: ITN coverage percentage (0-1)
- `efficacy`: Measured ITN efficacy (0-1)

**Vector Data** (`vector_data.csv`):
- `location`: Sample location
- `vector_density`: Measured vector density
- `resistance_level`: Insecticide resistance level

## Data Sources

For real data, consider:
- Madagascar Ministry of Health
- WHO Global Malaria Programme
- PMI (President's Malaria Initiative)
- DHS (Demographic and Health Surveys)

## Notes

- All data files are gitignored by default for privacy
- Add `!data/your_file.csv` to `.gitignore` to include specific files
- Ensure data is properly anonymized before sharing

