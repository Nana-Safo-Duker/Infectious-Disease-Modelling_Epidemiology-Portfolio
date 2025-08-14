# Output Directory

This directory contains all simulation outputs, visualizations, and reports.

## Generated Files

When you run `main.py` or the notebooks, the following files are automatically generated:

### Data Files
- `malaria_simulation_results.csv` - Complete time series data for all scenarios
- `malaria_summary_statistics.csv` - Summary statistics comparing scenarios
- `model_parameters.json` - Model configuration and parameters used

### Visualizations
- `human_infections.png` - Time series of human infections across scenarios
- `vector_infections.png` - Time series of vector infections across scenarios
- `itn_efficacy.png` - ITN efficacy decay over time
- `comprehensive_dashboard.png` - Combined dashboard with all key metrics

### Reports
- `analysis_report.txt` - Detailed text report with findings and recommendations

## File Formats

- **CSV files**: Can be opened in Excel, Python (pandas), R, etc.
- **PNG files**: High-resolution (300 DPI) images suitable for publications
- **JSON files**: Structured parameter data for reproducibility
- **TXT files**: Human-readable analysis reports

## Usage

```python
# Load results in Python
import pandas as pd

results = pd.read_csv('output/malaria_simulation_results.csv')
summary = pd.read_csv('output/malaria_summary_statistics.csv')
```

```r
# Load results in R
results <- read.csv('output/malaria_simulation_results.csv')
summary <- read.csv('output/malaria_summary_statistics.csv')
```

## Notes

- Output files are regenerated each time you run the simulation
- Backup important results before re-running
- Large CSV files can be opened efficiently with pandas or data.table

