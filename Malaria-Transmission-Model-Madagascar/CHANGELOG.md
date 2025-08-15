# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Spatial heterogeneity modeling
- Age-stratified populations
- Multiple intervention scenarios
- Climate-driven transmission dynamics
- Stochastic model variant
- Web-based visualization dashboard

## [1.1.0] - 2025-10-28

### Added
- **Python Implementation**
  - Complete object-oriented Python implementation (`src/` directory)
  - `MalariaModel` class with comprehensive functionality
  - `MalariaVisualizer` class for professional visualizations
  - Utility functions for analysis and validation
  - Type hints and comprehensive docstrings
  
- **Project Structure**
  - Well-organized directory structure
  - Separation of source code, scripts, notebooks, and documentation
  - Dedicated directories for data, output, tests, and docs
  
- **Testing**
  - Comprehensive test suite with pytest
  - Unit tests for model components
  - Validation tests for numerical accuracy
  - Edge case and boundary condition tests
  - Test coverage reporting
  
- **Documentation**
  - Comprehensive README.md with badges and examples
  - Detailed model description in `docs/model_description.md`
  - Installation guide in `docs/INSTALLATION.md`
  - Contributing guidelines in `CONTRIBUTING.md`
  - API documentation via docstrings
  
- **Development Tools**
  - `requirements.txt` for pip dependencies
  - `environment.yml` for conda users
  - `setup.py` for package installation
  - `.gitignore` for version control
  - `.gitattributes` for cross-platform compatibility
  - Makefile for common development tasks
  - GitHub Actions CI/CD workflow
  
- **Examples and Scripts**
  - `main.py` - Full simulation pipeline
  - `example_usage.py` - Quick start example
  - Enhanced R script with better documentation
  - Improved Jupyter notebook with detailed explanations
  
- **Features**
  - Four simulation scenarios (no ITN, no resistance, low resistance, high resistance)
  - Advanced visualization options (multiple plot types, dashboard)
  - Summary statistics and comparative analysis
  - Model validation and quality checks
  - CSV and JSON export functionality
  - Automated report generation

### Changed
- Enhanced R script with improved code structure and comments
- Updated Jupyter notebook with comprehensive markdown explanations
- Reorganized file structure for better maintainability
- Improved parameter naming and organization
- Enhanced plotting aesthetics and color schemes

### Fixed
- Population conservation validation
- Numerical stability improvements
- Edge case handling in calculations

## [1.0.0] - 2025-09-15

### Added
- Initial release of malaria transmission model
- Basic SIR-SI model implementation in R
- ITN effects modeling
- Insecticide resistance simulation
- Four comparison scenarios
- Basic visualizations
- Jupyter notebook implementation (R kernel)
- Summary statistics calculation

### Features
- Human compartment dynamics (S, I, R)
- Vector compartment dynamics (S, I)
- Time-dependent ITN efficacy
- Seasonal vector mortality variation
- Logistic vector population growth
- Parameter customization

### Documentation
- Basic README with project overview
- Model equations documentation
- Installation instructions
- Usage examples

## Version History Summary

| Version | Release Date | Key Features |
|---------|--------------|--------------|
| 1.1.0 | 2025-10-28 | Python implementation, comprehensive testing, enhanced docs |
| 1.0.0 | 2025-09-15 | Initial R implementation, basic modeling |

## Migration Guide

### From 1.0.0 to 1.1.0

#### Python Users (New!)

```python
# Old: N/A (Python version didn't exist)

# New: Use Python implementation
from src.malaria_model import MalariaModel, ModelParameters

params = ModelParameters()
model = MalariaModel(params)
results = model.run_simulation()
```

#### R Users

```r
# Old: Direct script execution
source("Malaria-Transmission-Model-Madagascar.r")

# New: Enhanced script in scripts directory
source("scripts/Malaria-Transmission-Model-Madagascar.r")

# Note: R code remains backward compatible
```

#### File Structure Changes

```
Old structure:
├── Malaria-Transmission-Model-Madagascar.ipynb
├── Malaria-Transmission-Model-Madagascar.r
└── README.md

New structure:
├── src/                    # Python source code
├── scripts/                # R and other scripts
├── notebooks/              # Jupyter notebooks
├── tests/                  # Test suite
├── docs/                   # Documentation
├── data/                   # Data directory
├── output/                 # Generated outputs
├── main.py                 # Main Python script
├── example_usage.py        # Quick example
└── README.md              # Enhanced documentation
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## Authors

- **Nana Safo Duker** - Lead Author
- **Mouhamadou Fadel Diop**
- **Agnes Achiamaa Anane**
- **Grace Njoki Maina**

## Acknowledgments

This work was conducted as part of the Disease Modelling for Pandemic Preparedness and Response Modular Certificate Course under the German-West African Centre for Global Health and Pandemic Prevention (G-WAC) at Kwame Nkrumah University of Science and Technology (KNUST), Kumasi, Ghana.

---

[Unreleased]: https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/releases/tag/v1.0.0

