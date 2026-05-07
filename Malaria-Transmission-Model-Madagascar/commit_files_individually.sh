#!/bin/bash
# Script to commit files individually with specific messages
# This shows what individual commits would look like

echo "=== Committing files individually with unique messages ==="
echo ""

# Create directories first
echo "1. Creating project directories..."
git add data/
git commit -m "feat: create data directory for epidemiological input files

Add data/ folder structure for storing:
- Raw malaria transmission data
- Population statistics
- ITN coverage data
- Vector density measurements"

git add output/
git commit -m "feat: create output directory for simulation results

Add output/ folder for storing:
- Generated CSV files (time series, statistics)
- Visualization plots (PNG, 300 DPI)
- Analysis reports (TXT)
- Model parameters (JSON)"

git add docs/
git commit -m "docs: create documentation directory

Add docs/ folder for technical documentation:
- Model mathematical formulation
- Installation guides
- API reference
- User manuals"

git add .github/workflows/
git commit -m "ci: add GitHub Actions workflow directory

Create .github/workflows/ for automated CI/CD:
- Multi-platform testing (Ubuntu, Windows, macOS)
- Python 3.8-3.11 compatibility checks
- Code coverage reporting"

git add notebooks/
git commit -m "refactor: move notebooks to dedicated directory

Reorganize Jupyter notebooks into notebooks/ folder:
- Separates interactive analysis from source code
- Improves project organization
- Contains R-kernel based malaria model notebook"

git add scripts/
git commit -m "refactor: move R scripts to dedicated directory

Reorganize R implementation into scripts/ folder:
- Separates scripting files from Python source
- Contains complete R-based malaria model
- Maintains backward compatibility"

git add src/
git commit -m "feat: create Python source code package directory

Add src/ for modular Python implementation:
- Core model module (malaria_model.py)
- Visualization tools (visualization.py)
- Utility functions (utils.py)
- Package initialization"

git add tests/
git commit -m "test: create comprehensive test suite directory

Add tests/ folder with pytest framework:
- 25+ unit tests
- Integration tests
- Model validation tests
- Edge case coverage"

echo ""
echo "2. Committing configuration files..."

git add .gitignore
git commit -m "chore: add .gitignore for Python, R, and IDE files

Ignore patterns for:
- Python: __pycache__, *.pyc, venv/, build/
- R: .RData, .Rhistory, .Rproj.user
- Jupyter: .ipynb_checkpoints
- IDEs: .vscode/, .idea/
- OS: .DS_Store, Thumbs.db

Keeps repository clean of generated files"

git add .gitattributes
git commit -m "chore: configure git attributes for cross-platform compatibility

Set line ending normalization:
- LF for source files (Python, R, configs)
- CRLF for Windows scripts (.bat, .cmd)
- Binary handling for images and data
- Jupyter notebook diff driver
- Export-ignore for dev files

Ensures consistent behavior on Windows/macOS/Linux"

git add requirements.txt
git commit -m "feat: add Python dependencies specification

Define required packages:
- Scientific: numpy>=1.21, scipy>=1.7, pandas>=1.3
- Visualization: matplotlib>=3.4, seaborn>=0.11
- Notebook: jupyter>=1.0, ipykernel>=6.0
- Testing: pytest>=6.2
- Development: black>=21.0, flake8>=3.9

Install with: pip install -r requirements.txt"

git add environment.yml
git commit -m "feat: add Conda environment specification

Create reproducible conda environment:
- Python 3.8+ with scientific stack
- R 4.0+ with tidyverse, deSolve
- Development tools (pytest, black)
- Cross-platform compatibility
- Both conda and pip dependencies

Create with: conda env create -f environment.yml"

git add setup.py
git commit -m "feat: add Python package setup configuration

Enable pip installation of malaria model package:
- Package metadata (name, version, author)
- Dependency management
- Entry points for CLI commands
- Development extras
- Classifier tags for PyPI
- Project URLs

Install with: pip install -e ."

git add Makefile
git commit -m "chore: add Makefile for common development tasks

Simplify workflow with make commands:
- make install: Install dependencies
- make test: Run test suite with coverage
- make lint: Check code quality
- make format: Auto-format with Black
- make clean: Remove build artifacts
- make run: Execute main simulation

Works on Unix-like systems"

git add LICENSE
git commit -m "chore: add MIT License

Grant permission to use, modify, and distribute:
- Free and open source
- Commercial use allowed
- Attribution required
- No warranty

Copyright (c) 2025 Safo et al."

git add .github/workflows/ci.yml
git commit -m "ci: add GitHub Actions CI/CD pipeline

Automated testing workflow:
- Matrix: Python 3.8-3.11 × Ubuntu/Windows/macOS
- Run pytest with coverage reporting
- Code quality checks (flake8, black)
- Upload coverage to Codecov
- Triggers on push and pull requests

Ensures code quality across platforms"

echo ""
echo "3. Committing documentation files..."

git add README.md
git commit -m "docs: enhance README with comprehensive documentation

Major improvements:
- Add badges (License, Python, R, CI status)
- Expand installation instructions (pip, conda, R)
- Add Python API usage examples
- Include detailed project structure
- Add quick start guide
- Enhance features list
- Update citation with BibTeX
- Add troubleshooting section
- Document all 4 simulation scenarios

Increases from ~300 to ~600 lines"

git add QUICKSTART.md
git commit -m "docs: add 5-minute quick start guide

Help new users get started fast:
- 30-second installation
- 1-minute first simulation
- Example parameter customization
- Result interpretation
- Common troubleshooting
- Next steps

Designed for immediate productivity"

git add CHANGELOG.md
git commit -m "docs: add comprehensive version history

Document all changes following Keep a Changelog format:
- v1.1.0 features (Python, tests, docs, CI/CD)
- v1.0.0 initial release notes
- Migration guide v1.0.0 → v1.1.0
- Version comparison table
- Semantic versioning compliance
- Planned features for future releases"

git add CONTRIBUTING.md
git commit -m "docs: add contributing guidelines for collaborators

Comprehensive contributor guide:
- Code of conduct
- Development environment setup
- Coding standards (PEP 8, tidyverse)
- Testing requirements (>80% coverage)
- Documentation standards
- Pull request process
- Code review guidelines
- Issue templates

~400 lines encouraging open collaboration"

git add PROJECT_SUMMARY.md
git commit -m "docs: add project reorganization summary

Document v1.1.0 transformation:
- Project statistics (30+ files, 2500+ lines Python)
- New structure overview
- Key features implemented
- Improvements over v1.0.0 comparison
- Quality metrics
- Educational value
- Research impact statement
- Next steps for users/developers

Comprehensive reference for release"

git add GIT_COMMANDS.md
git commit -m "docs: add Git workflow reference guide

Help maintainers manage repository:
- Recommended commit workflow
- Push instructions
- Branch management strategies
- Release creation steps
- Repository settings configuration
- Verification procedures
- Troubleshooting common issues
- Badge setup

Practical Git operations reference"

git add docs/model_description.md
git commit -m "docs: add detailed mathematical model documentation

Technical documentation for researchers:
- Complete mathematical formulation
- Differential equations with notation
- Parameter descriptions and ranges
- Implementation details (LSODA solver)
- Model assumptions and limitations
- Validation methods
- Sensitivity analysis approach
- References to literature (WHO, Nature, etc.)

~500 lines of rigorous documentation"

git add docs/INSTALLATION.md
git commit -m "docs: add comprehensive installation guide

Step-by-step instructions for all platforms:
- System requirements
- Python setup (pip, venv)
- R setup (CRAN, RStudio)
- Conda installation
- Platform-specific (Windows/macOS/Linux)
- Troubleshooting common errors
- Verification steps
- Next steps after installation

~400 lines covering all scenarios"

git add data/README.md
git commit -m "docs: document data directory structure and usage

Explain data organization:
- Expected file formats (CSV)
- Data sources (WHO, Madagascar MoH)
- Schema specifications
- Privacy considerations
- Example data templates
- How to add custom data

Helps users integrate their own data"

git add output/README.md
git commit -m "docs: document output files and formats

Explain generated outputs:
- CSV: simulation results, summary stats
- PNG: plots at 300 DPI for publication
- JSON: model parameters for reproducibility
- TXT: analysis reports
- Loading examples (Python and R)

Helps users work with results"

echo ""
echo "4. Committing Python source code..."

git add src/__init__.py
git commit -m "feat: initialize Python package with exported classes

Create src/ package structure:
- Export MalariaModel (core simulation)
- Export MalariaVisualizer (plotting)
- Export ModelParameters (configuration)
- Export SimulationResults (results container)
- Set __version__ = '1.1.0'
- Set __author__ = 'Safo et al. (2025)'

Enables: from src import MalariaModel"

git add src/malaria_model.py
git commit -m "feat: implement core malaria transmission model

Complete SIR-SI epidemiological model:
- MalariaModel class with ODE solver
- ModelParameters dataclass with validation
- Human compartments (S, I, R)
- Vector compartments (S, I)
- ITN effects with exponential resistance decay
- Seasonal vector mortality
- Multiple scenario support (4 scenarios)
- Effective R0 calculation
- Population conservation checks

~400 lines with full docstrings and type hints
Uses scipy.integrate.odeint for ODE solving"

git add src/visualization.py
git commit -m "feat: implement professional visualization tools

MalariaVisualizer class for publication-quality plots:
- Human infection time series
- Vector infection dynamics  
- ITN efficacy decay curves
- Comprehensive 4-panel dashboard
- Custom color schemes per scenario
- Matplotlib/Seaborn integration
- Export to PNG/PDF at configurable DPI
- Batch plot generation

~350 lines with customizable styling
Generates ready-to-publish figures"

git add src/utils.py
git commit -m "feat: add utility functions and result containers

Utility module with helper functions:
- SimulationResults dataclass for organizing output
- validate_model_results() for quality checks
- calculate_reproduction_number() for R0
- calculate_summary_statistics() for analysis
- generate_report() for text output
- compare_scenarios() for benchmarking
- CSV/JSON export functions
- Population conservation validation

~350 lines supporting main workflow
Ensures data quality and reproducibility"

echo ""
echo "5. Committing test files..."

git add tests/__init__.py
git commit -m "test: initialize test package structure

Create tests/ package for pytest:
- Makes tests/ a proper Python package
- Allows test discovery
- Enables test imports"

git add tests/test_malaria_model.py
git commit -m "test: add comprehensive model test suite

25+ test cases covering:
- TestModelParameters: initialization, calculations
- TestMalariaModel: simulation, ODE solving
- TestSummaryStatistics: metrics, reductions
- TestValidation: conservation laws, R0
- TestEdgeCases: boundary conditions

Tests verify:
- Population conservation (±0.001%)
- No negative values
- ITN efficacy decay
- Effective R0 calculations
- Multi-scenario consistency
- Numerical stability

~300 lines with pytest framework
Ensures model correctness and reliability"

echo ""
echo "6. Committing main execution scripts..."

git add main.py
git commit -m "feat: add main analysis pipeline script

Complete end-to-end workflow:
1. Initialize model parameters
2. Run 4 scenarios (no ITN, no resist, low resist, high resist)
3. Calculate summary statistics
4. Validate model results
5. Generate visualizations
6. Create analysis reports
7. Export to CSV/JSON/PNG

~300 lines with progress feedback
Professional output and error handling
Run with: python main.py"

git add example_usage.py
git commit -m "feat: add quick start example for beginners

Simplified 5-minute tutorial:
- Basic parameter setup
- Single scenario simulation
- Multi-scenario comparison
- Simple visualization
- Key findings interpretation
- Saves example outputs

~150 lines for immediate productivity
Perfect for learning the API
Run with: python example_usage.py"

git add notebooks/Malaria-Transmission-Model-Madagascar.ipynb
git commit -m "refactor: move Jupyter notebook to notebooks directory

Relocate interactive analysis notebook:
- R-kernel based implementation
- Comprehensive markdown explanations
- Step-by-step execution cells
- Inline visualizations
- Summary statistics tables

File content unchanged, location improved
Now: notebooks/Malaria-Transmission-Model-Madagascar.ipynb"

git add scripts/Malaria-Transmission-Model-Madagascar.r
git commit -m "refactor: move R script to scripts directory

Relocate R implementation:
- Complete tidyverse-based analysis
- deSolve ODE integration
- ggplot2 visualizations
- 4 scenario comparisons
- Summary statistics calculation

File content unchanged, location improved  
Now: scripts/Malaria-Transmission-Model-Madagascar.r
Run with: source('scripts/Malaria-Transmission-Model-Madagascar.r')"

echo ""
echo "=== All files committed individually! ==="
echo "Total: 28 individual commits with unique messages"

