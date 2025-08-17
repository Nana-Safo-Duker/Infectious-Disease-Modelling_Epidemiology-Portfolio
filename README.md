# Malaria Transmission Model in Madagascar

A comprehensive epidemiological modeling study examining the effectiveness of Insecticide-Treated Nets (ITNs) in malaria control programs in Madagascar with particular focus on the impact of insecticide resistance over time.

## 📋 Table of Contents

- [Overview](#overview)
- [Model Description](#model-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)
- [Authors](#Authors)
- [Contact](#contact)
- [Acknowledgments](#Acknowledgments)
- [References](#References)
- [Changelog](#Changelog)

## Overview

This project implements a modified SIR (Susceptible-Infected-Recovered) epidemiological model to simulate malaria transmission dynamics in Madagascar. The model incorporates:

- **Human population dynamics** (S, I, R compartments)
- **Vector population dynamics** (S, I compartments)
- **ITN effects** with time-dependent efficacy
- **Insecticide resistance** modeling
- **Seasonal variation** in vector mortality

### Research Question

*How does insecticide resistance affect the long-term effectiveness of Insecticide-Treated Nets (ITNs) in malaria control programs in Madagascar?*

## 🧮 Model Description

### Mathematical Formulation

The model consists of five differential equations:

**Human Compartments:**
```
dSh/dt = -βv→h Sh (Nv/Nh) (Iv/Nv) (1/4) + α Rh
dIh/dt = βv→h Sh (Nv/Nh) (Iv/Nv) (1/4) - γh Ih
dRh/dt = γh Ih - α Rh
```

**Vector Compartments:**
```
dSv/dt = r Nv (1 - Nv/K) - βh→v Sv (Ih/Nh) (1/4) - (1 + sin(2πt/365))/5 d Sv
dIv/dt = βh→v Sv (Ih/Nh) (1/4) - (1 + sin(2πt/365))/5 d Iv
```

**ITN Effectiveness Decay:**
```
E(t) = E₀ exp(-r_res × t/365)
```

### Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| R₀ | 2.0 | Basic reproduction number |
| Infectious Period | 14 days | Average duration of malaria infection |
| ITN Coverage | 80% | Population coverage of ITNs |
| Initial ITN Efficacy | 90% | Initial effectiveness of ITNs |
| Resistance Rate | 10%/year | Annual rate of resistance development |

## ✨ Features

- **Four Simulation Scenarios:**
  - No ITNs (baseline)
  - ITNs with no resistance
  - ITNs with low resistance (5%/year)
  - ITNs with high resistance (10%/year)

- **Comprehensive Analysis:**
  - Population dynamics over 5 years
  - ITN efficacy degradation modeling
  - Statistical comparison of scenarios
  - Model validation and sensitivity analysis

- **Professional Visualizations:**
  - Time series plots for human and vector infections
  - ITN efficacy decay curves
  - Summary statistics tables

## 🚀 Installation

### Prerequisites

- R (version 4.0 or higher)
- RStudio (recommended)

### Required R Packages

```r
install.packages(c(
  "tidyverse",
  "deSolve", 
  "ggplot2",
  "dplyr",
  "knitr"
))
```

### Quick Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/malaria-transmission-model-madagascar.git
cd malaria-transmission-model-madagascar
```

2. Open the project in RStudio or your preferred R environment

3. Install dependencies (if not already installed):
```r
source("install_dependencies.R")  # Optional helper script
```

## 📊 Usage

### Running the Analysis

#### Option 1: Jupyter Notebook (Recommended)
```bash
# Open the R-based Jupyter notebook
jupyter notebook Malaria-Transmission-Model-Madagascar.ipynb
```

#### Option 2: R Script
```r
# Run the complete analysis
source("Malaria-Transmission-Model-Madagascar.r")
```

#### Option 3: Interactive R Session
```r
# Load libraries
library(tidyverse)
library(deSolve)

# Run simulations
source("Malaria-Transmission-Model-Madagascar.r")

# View results
View(all_results)
View(summary_stats)
```

### Customizing Parameters

Modify the parameters in the notebook or script:

```r
# Example: Change ITN coverage
itn_coverage <- 0.9  # 90% coverage instead of 80%

# Example: Adjust resistance rate
resistance_rate <- 0.15  # 15% per year instead of 10%
```

## 📈 Results

### Key Findings

1. **ITN Effectiveness**: ITNs provide significant malaria reduction even with resistance
2. **Resistance Impact**: High resistance reduces effectiveness by ~15-20 percentage points
3. **Long-term Efficacy**: After 5 years, ITN efficacy drops to ~55% with high resistance
4. **Policy Implications**: ITNs remain cost-effective even with moderate resistance

### Sample Output

The analysis generates:
- **Visualizations**: Time series plots showing infection dynamics
- **Summary Statistics**: Peak infections, mean infections, and reduction percentages
- **CSV Files**: `malaria_simulation_results.csv` and `malaria_summary_statistics.csv`

### Example Results Table

| Scenario | Peak Infected Humans | Reduction (%) | Mean Infected Humans |
|----------|---------------------|---------------|---------------------|
| No ITNs | 45,230 | - | 12,450 |
| ITNs (No Resistance) | 8,920 | 80.3% | 2,340 |
| ITNs (Low Resistance) | 12,150 | 73.1% | 3,180 |
| ITNs (High Resistance) | 18,670 | 58.7% | 4,920 |

## 📁 File Structure

```
malaria-transmission-model-madagascar/
├── README.md                                    # This file
├── Malaria-Transmission-Model-Madagascar.ipynb  # Main R-based Jupyter notebook
├── Malaria-Transmission-Model-Madagascar.r      # R script version
├── malaria_simulation_results.csv               # Complete simulation data
├── malaria_summary_statistics.csv              # Summary statistics
├── output.png                                   # Sample visualization
├── output_1.png                                 # ITN efficacy plot
└── install_dependencies.R                       # Optional dependency installer
```

## 🔧 Technical Details

### Model Validation

The model includes comprehensive validation:
- **Population Conservation**: Human population remains constant
- **Data Quality Checks**: No negative or infinite values
- **Reproduction Numbers**: R₀ calculations for different scenarios

### Computational Requirements

- **Memory**: ~50MB for full simulation
- **Runtime**: <30 seconds on modern hardware
- **Output Size**: ~1.5MB CSV files

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow R style guidelines
- Add comments for complex calculations
- Include unit tests for new functions
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Citation

If you use this model in your research, please cite:

```bibtex
@software{malaria-transmission-model-madagascar,
  title={Malaria Transmission Model in Madagascar: ITN Effectiveness and Resistance},
  author={Diop, Mouhamadou Fadel and Anane, Agnes Achiamaa and Maina, Grace Njoki and Duker, Nana Safo},
  year={2025},
  url={https://medium.com/@freshsafoduker300/simulating-and-fitting-malaria-transmission-model-in-madagascar-impact-of-insecticide-treated-nets-fd9c10d4cda4},
  note={Epidemiological modeling of malaria transmission with ITN effects}
}
}

```
## Authors

Safo et al. (2025)
Authors:

- **Nana Safo Duker**

- **Mouhamadou Fadel Diop**

- **Agnes Achiamaa Anane**

- **Grace Njoki Maina**

Citation Format (APA):

Safo, M. F., Anane, A. A., Maina, G. N., & Duker, N. S. (2025). Malaria Transmission Model: Simulation and Resistance Analysis in Madagascar (Version 1.1.0). 

GitHub Repository. https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar

url={https://medium.com/@freshsafoduker300/simulating-and-fitting-malaria-transmission-model-in-madagascar-impact-of-insecticide-treated-nets-fd9c10d4cda4}

...

## 📞 Contact

- **Author**: Nana Safo Duker 
- **Email**: freshsafoduker3@gmail.com 
- **GitHub**: https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar

## 🙏 Acknowledgments

- Madagascar Ministry of Health for epidemiological data
- WHO Global Malaria Programme for ITN effectiveness guidelines
- R community for excellent epidemiological modeling packages
- Funding Support

This work was conducted as part of the Disease Modelling for Pandemic Preparedness and Response Modular Certificate Course under the
German-West African Centre for Global Health and Pandemic Prevention (G-WAC) at Kwame Nkrumah University of Science and Technology (KNUST), Kumasi, Ghana.

We gratefully acknowledge the support, mentorship, and collaborative environment provided by G-WAC and its partners, which made this research and modeling project possible.

## 📖 References

1. World Health Organization. (2023). *World Malaria Report 2023*. Geneva: WHO.
2. Bhatt, S., et al. (2015). The effect of malaria control on Plasmodium falciparum in Africa between 2000 and 2015. *Nature*, 526(7572), 207-211.
3. Ranson, H., et al. (2016). Insecticide resistance in African Anopheles mosquitoes: a worsening situation that needs urgent action. *Trends in Parasitology*, 32(3), 187-196.

---


## Changelog
### Version 1.1.0 — October 2025

### Status: Active Development

### Updates

🧠 Improved Jupyter Notebook (.ipynb) with enhanced malaria transmission simulations and plots.

📊 Optimized R script (.R) for cleaner model fitting, reproducibility, and faster computation.

🧾 Refined documentation and added clearer explanations for model assumptions.

🧹 Repository cleanup — removed unused folders, temp files, and configuration clutter.

### Previous Version

Version 1.0.0 — September 2025

🔰 Initial release featuring deterministic malaria model and ITN resistance simulations.

