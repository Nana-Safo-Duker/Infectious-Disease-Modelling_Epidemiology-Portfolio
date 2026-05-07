# Individual Commit Messages Reference

This document shows what individual commit messages would be appropriate for each file/folder if they were committed separately.

---

## 📁 Project Structure Folders

### `src/`
```bash
git commit -m "feat: Add Python source code directory

Create src/ package for Python implementation of malaria model.
Implements modular architecture with separate modules for model,
visualization, and utilities."
```

### `tests/`
```bash
git commit -m "test: Add comprehensive test suite

Create tests/ directory with pytest-based unit tests.
Includes 25+ test cases covering model validation,
parameter handling, and numerical accuracy."
```

### `docs/`
```bash
git commit -m "docs: Add documentation directory

Create docs/ folder for comprehensive technical documentation
including model description and installation guides."
```

### `notebooks/`
```bash
git commit -m "refactor: Reorganize notebooks into dedicated directory

Move Jupyter notebook to notebooks/ folder for better organization.
Improves project structure and separates interactive analysis files."
```

### `scripts/`
```bash
git commit -m "refactor: Reorganize R scripts into dedicated directory

Move R implementation to scripts/ folder for better organization.
Separates scripting files from source code and notebooks."
```

### `data/`
```bash
git commit -m "feat: Add data directory structure

Create data/ folder for epidemiological input files.
Includes README with data format specifications and sources."
```

### `output/`
```bash
git commit -m "feat: Add output directory for results

Create output/ folder for generated visualizations, CSV files,
and analysis reports. Includes documentation of output formats."
```

### `.github/workflows/`
```bash
git commit -m "ci: Add GitHub Actions workflow directory

Create .github/workflows/ for CI/CD pipeline.
Enables automated testing and code quality checks."
```

---

## 🐍 Python Source Files

### `src/__init__.py`
```bash
git commit -m "feat: Initialize Python package structure

Add __init__.py to make src/ a proper Python package.
Exports main classes: MalariaModel, MalariaVisualizer, 
ModelParameters, and SimulationResults."
```

### `src/malaria_model.py`
```bash
git commit -m "feat: Implement core malaria transmission model

Add MalariaModel class with SIR-SI dynamics for humans and vectors.
Features:
- ODE-based transmission model
- ITN effects with resistance
- Multiple scenario simulations
- Parameter validation
- Effective R0 calculations

~400 lines with comprehensive docstrings and type hints."
```

### `src/visualization.py`
```bash
git commit -m "feat: Add professional visualization tools

Implement MalariaVisualizer class for publication-quality plots.
Features:
- Human and vector infection time series
- ITN efficacy decay curves
- Comprehensive dashboard layouts
- Customizable color schemes
- Multiple export formats (PNG, PDF)

~350 lines with matplotlib/seaborn integration."
```

### `src/utils.py`
```bash
git commit -m "feat: Add utility functions and helpers

Implement SimulationResults class and utility functions.
Features:
- Results container with export methods
- Model validation functions
- R0 calculations
- Summary statistics generation
- Report generation
- Data quality checks

~350 lines supporting main model operations."
```

---

## 🧪 Test Files

### `tests/__init__.py`
```bash
git commit -m "test: Initialize test package

Add __init__.py to make tests/ a proper Python package."
```

### `tests/test_malaria_model.py`
```bash
git commit -m "test: Add comprehensive model test suite

Implement 25+ test cases covering:
- Parameter initialization and validation
- Model dynamics and ODE solving
- Population conservation
- ITN efficacy decay
- Effective R0 calculations
- Edge cases and boundary conditions
- Multi-scenario simulations

~300 lines with pytest framework."
```

---

## 📚 Documentation Files

### `README.md` (modified)
```bash
git commit -m "docs: Enhance README with comprehensive documentation

Major improvements:
- Add badges (license, Python, R versions)
- Expand installation instructions
- Add Python API examples
- Include project structure diagram
- Add quick start guide
- Enhance citation information
- Add contributing section
- Update with v1.1.0 features

Increases from ~300 to ~600 lines."
```

### `QUICKSTART.md`
```bash
git commit -m "docs: Add quick start guide for new users

Create 5-minute tutorial covering:
- Rapid installation (30 seconds)
- First simulation run (1 minute)
- Parameter customization
- Result interpretation
- Next steps and resources

Designed for immediate productivity."
```

### `CHANGELOG.md`
```bash
git commit -m "docs: Add comprehensive changelog

Document version history following Keep a Changelog format.
Includes:
- v1.1.0 new features and improvements
- v1.0.0 initial release notes
- Migration guide from v1.0.0 to v1.1.0
- Version comparison table"
```

### `CONTRIBUTING.md`
```bash
git commit -m "docs: Add contributing guidelines

Comprehensive guide for contributors covering:
- Code of conduct
- Development setup
- Coding standards (Python and R)
- Testing requirements
- Documentation standards
- Pull request process
- Code review guidelines

~400 lines encouraging open collaboration."
```

### `docs/model_description.md`
```bash
git commit -m "docs: Add detailed model documentation

Technical documentation covering:
- Mathematical formulation with equations
- Parameter descriptions and ranges
- Implementation details
- Model assumptions and limitations
- Validation methods
- Sensitivity analysis
- References and citations

~500 lines for researchers and advanced users."
```

### `docs/INSTALLATION.md`
```bash
git commit -m "docs: Add comprehensive installation guide

Step-by-step installation instructions for:
- Python (pip and conda)
- R and RStudio
- Platform-specific setup (Windows, macOS, Linux)
- Troubleshooting common issues
- Verification steps
- Environment configuration

~400 lines covering all installation scenarios."
```

### `PROJECT_SUMMARY.md`
```bash
git commit -m "docs: Add project reorganization summary

Document complete restructuring effort including:
- Project statistics
- New structure overview
- Key features implemented
- Improvements over v1.0.0
- Quality metrics
- Educational value
- Impact statement

Comprehensive reference for v1.1.0 release."
```

### `GIT_COMMANDS.md`
```bash
git commit -m "docs: Add Git workflow guide

Reference guide for Git operations including:
- Recommended workflow
- Commit and push instructions
- Branch management
- Release creation
- Repository settings
- Verification steps
- Troubleshooting

Helps maintainers manage repository."
```

---

## 🔧 Configuration Files

### `.gitignore`
```bash
git commit -m "chore: Add comprehensive .gitignore

Ignore patterns for:
- Python artifacts (__pycache__, *.pyc)
- Virtual environments (venv/, env/)
- Jupyter checkpoints
- R artifacts (.RData, .Rhistory)
- IDE files (.vscode/, .idea/)
- OS files (.DS_Store, Thumbs.db)
- Build artifacts

Keeps repository clean and focused."
```

### `.gitattributes`
```bash
git commit -m "chore: Configure Git attributes for cross-platform compatibility

Set up line ending normalization and file handling:
- Normalize line endings to LF for source files
- Configure binary file handling
- Set up Jupyter notebook diff driver
- Define export-ignore patterns
- Ensure consistent behavior across Windows, macOS, Linux"
```

### `requirements.txt`
```bash
git commit -m "feat: Add Python dependencies file

Define project dependencies:
- Core: numpy, scipy, pandas
- Visualization: matplotlib, seaborn
- Notebook: jupyter, ipykernel
- Development: pytest, black, flake8
- Data: openpyxl

Enables pip install -r requirements.txt for easy setup."
```

### `environment.yml`
```bash
git commit -m "feat: Add Conda environment specification

Create environment.yml for conda users including:
- Python 3.8+ and scientific stack
- R and tidyverse packages
- Development tools
- Cross-platform compatibility
- Both conda and pip dependencies

Enables: conda env create -f environment.yml"
```

### `setup.py`
```bash
git commit -m "feat: Add package setup configuration

Implement setup.py for pip installation:
- Package metadata and description
- Dependency management
- Entry points for CLI
- Classifier tags
- Development extras
- Project URLs

Enables: pip install -e ."
```

### `Makefile`
```bash
git commit -m "chore: Add Makefile for development tasks

Common commands for developers:
- make install: Install dependencies
- make test: Run test suite
- make lint: Code quality checks
- make format: Auto-format code
- make clean: Remove build artifacts
- make run: Execute main script

Simplifies development workflow."
```

### `LICENSE`
```bash
git commit -m "chore: Add MIT License

Add MIT License granting permission to use, modify, and
distribute the software. Includes copyright notice for
Safo et al. (2025) authors."
```

### `.github/workflows/ci.yml`
```bash
git commit -m "ci: Add GitHub Actions CI/CD pipeline

Automated testing workflow:
- Matrix testing (Python 3.8-3.11, OS: Ubuntu/Windows/macOS)
- Run pytest with coverage
- Code linting with flake8 and black
- Codecov integration
- Runs on push and pull requests

Ensures code quality and compatibility."
```

---

## 📁 Directory README Files

### `data/README.md`
```bash
git commit -m "docs: Add data directory documentation

Document data directory structure and usage:
- Expected file formats
- Data sources (WHO, Madagascar Ministry of Health)
- CSV format specifications
- Privacy and gitignore notes
- Examples of population, ITN, and vector data"
```

### `output/README.md`
```bash
git commit -m "docs: Add output directory documentation

Document generated output files:
- CSV files (simulation results, summary statistics)
- Visualizations (PNG plots at 300 DPI)
- Reports (text analysis reports)
- JSON (model parameters)
- Usage examples for loading results in Python/R"
```

---

## 🎯 Main Execution Scripts

### `main.py`
```bash
git commit -m "feat: Add main execution script for complete pipeline

Implement comprehensive analysis pipeline:
- Parameter initialization
- Multi-scenario simulations (4 scenarios)
- Summary statistics calculation
- Model validation
- Visualization generation
- Report creation
- Results export (CSV, JSON, PNG)

~300 lines orchestrating full analysis workflow.
Provides professional output and progress feedback."
```

### `example_usage.py`
```bash
git commit -m "feat: Add quick start example script

Create beginner-friendly example demonstrating:
- Basic parameter setup
- Single scenario simulation
- Multi-scenario comparison
- Simple visualization
- Key findings interpretation

~150 lines designed for 5-minute introduction.
Generates example outputs without overwhelming new users."
```

---

## 📓 Reorganized Files

### `notebooks/Malaria-Transmission-Model-Madagascar.ipynb`
```bash
git commit -m "refactor: Move Jupyter notebook to notebooks directory

Reorganize notebook location from root to notebooks/.
Improves project structure by grouping interactive
analysis files in dedicated folder.

File remains unchanged, only location updated."
```

### `scripts/Malaria-Transmission-Model-Madagascar.r`
```bash
git commit -m "refactor: Move R script to scripts directory

Reorganize R implementation from root to scripts/.
Improves project structure by separating scripts
from source code and documentation.

File remains unchanged, only location updated."
```

---

## 📊 Combined Commit Message (What Was Actually Used)

```bash
git commit -m "feat: Major project reorganization v1.1.0

- Add comprehensive Python implementation with OOP design
- Create modular source structure (src/, tests/, docs/)
- Add complete test suite with pytest
- Enhance documentation (README, CONTRIBUTING, INSTALLATION)
- Add development tools (Makefile, CI/CD, setup.py)
- Reorganize R and Jupyter notebooks into dedicated directories
- Add example scripts and quick start guide
- Implement advanced visualization tools
- Add validation and utility functions

Version: 1.1.0

Changes:
- 28 files changed
- 4,164 insertions(+)
- 159 deletions(-)

This commit represents a major upgrade from v1.0.0 to v1.1.0,
transforming the repository into a production-ready, professionally
organized epidemiological modeling project."
```

---

## 💡 Commit Message Best Practices

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types Used
- **feat**: New features
- **fix**: Bug fixes
- **docs**: Documentation changes
- **style**: Code style (formatting, no logic change)
- **refactor**: Code restructuring
- **test**: Test additions/changes
- **chore**: Maintenance tasks
- **ci**: CI/CD changes

### Examples by Category

**Feature Addition:**
```bash
git commit -m "feat(model): add ITN resistance decay function

Implement exponential decay of ITN efficacy over time.
Formula: E(t) = E0 * exp(-r * t/365)
where E0 is initial efficacy and r is resistance rate."
```

**Bug Fix:**
```bash
git commit -m "fix(model): correct population conservation in vector dynamics

Fix issue where vector population wasn't properly conserved
due to incorrect logistic growth term. Now maintains
stable equilibrium at carrying capacity K."
```

**Documentation:**
```bash
git commit -m "docs(api): add docstrings to MalariaModel class

Add comprehensive NumPy-style docstrings to all public methods.
Includes parameter descriptions, return values, and examples."
```

**Testing:**
```bash
git commit -m "test(model): add edge case tests for zero initial infections

Test model behavior when starting with zero infected individuals.
Ensures model remains stable and doesn't produce NaN values."
```

**Refactoring:**
```bash
git commit -m "refactor(viz): extract color scheme to class variable

Move color palette definition from methods to class-level constant.
Improves maintainability and allows easy customization."
```

---

## 🎯 Summary Statistics

| Category | Files | Commit Messages |
|----------|-------|----------------|
| **Source Code** | 4 | feat |
| **Tests** | 2 | test |
| **Documentation** | 8 | docs |
| **Configuration** | 8 | chore/feat/ci |
| **Scripts** | 2 | feat |
| **Reorganized** | 2 | refactor |
| **Directories** | 8 | feat/refactor |
| **Total** | 34 | 34 individual messages |

---

**Note**: While all files were committed together in the actual repository,
this document serves as a reference for understanding each component's purpose
and how individual commits would be structured for granular change tracking.

---

**Created**: October 28, 2025  
**Version**: 1.1.0  
**Purpose**: Documentation and reference for commit message best practices

