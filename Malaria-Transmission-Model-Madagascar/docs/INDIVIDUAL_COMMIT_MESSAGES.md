# Individual Commit Messages — Malaria Transmission Model (Madagascar)

Each file below has a **unique commit message** (no type prefixes).

| File | Message |
|------|---------|
| `LICENSE` | Add MIT license for open malaria modeling reuse |
| `.gitignore` | Exclude build artifacts, envs, and notebook checkpoints |
| `.gitattributes` | Normalize line endings and binary handling across operating systems |
| `requirements.txt` | Pin Python stack for ODE simulation and plotting |
| `environment.yml` | Add Conda spec for Python and R dual-language workflow |
| `setup.py` | Register malaria-model package for editable installs |
| `Makefile` | Add make targets for test, lint, run, and clean |
| `src/__init__.py` | Expose MalariaModel API from src package root |
| `src/malaria_model.py` | Implement SIR-SI ODE model with ITN resistance decay for Madagascar |
| `src/utils.py` | Add validation, R0 helpers, and export utilities for simulation results |
| `src/visualization.py` | Add MalariaVisualizer for scenario comparison plots and dashboards |
| `tests/__init__.py` | Mark tests directory as a pytest-discoverable package |
| `tests/test_malaria_model.py` | Verify ODE stability, ITN decay, and multi-scenario consistency |
| `main.py` | Orchestrate full Madagascar analysis pipeline from simulation to export |
| `example_usage.py` | Add minimal API walkthrough for first-time users |
| `scripts/Malaria-Transmission-Model-Madagascar.r` | Port transmission model to R with deSolve and ggplot2 |
| `notebooks/Malaria-Transmission-Model-Madagascar.ipynb` | Add interactive notebook for step-by-step model exploration |
| `data/README.md` | Describe input data layout and Madagascar epidemiological data sources |
| `output/README.md` | Catalog simulation artifacts written by the main analysis pipeline |
| `docs/model_description.md` | Formalize differential equations, parameters, and model assumptions |
| `docs/INSTALLATION.md` | Add platform-specific setup for Python, R, and Conda environments |
| `README.md` | Publish project overview, quick start guide, and citation block |
| `QUICKSTART.md` | Five-minute path from clone to first malaria simulation run |
| `CHANGELOG.md` | Record v1.0.0 R release and v1.1.0 Python expansion |
| `CONTRIBUTING.md` | Define contribution standards for code and epidemiology pull requests |
| `PROJECT_SUMMARY.md` | Summarize v1.1.0 restructure and G-WAC research deliverables |
| `GIT_COMMANDS.md` | Add maintainer cheat sheet for commits, branches, and releases |
| `.github/workflows/ci.yml` | Test Python 3.8 through 3.11 on Ubuntu, Windows, and macOS |
| `INDIVIDUAL_COMMITS.md` | Index per-file commit messages for portfolio commit hygiene |
| `commit_files_individually.sh` | Add bash script to replay granular commit history per file |
| `docs/INDIVIDUAL_COMMIT_MESSAGES.md` | Reference guide for unique commit messages per project file |

**Updated:** June 2026 · G-WAC Madagascar malaria transmission
