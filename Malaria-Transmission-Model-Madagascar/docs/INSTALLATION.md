# Installation Guide

Complete installation instructions for the Malaria Transmission Model.

## Table of Contents

- [System Requirements](#system-requirements)
- [Python Installation](#python-installation)
- [R Installation](#r-installation)
- [Conda Installation](#conda-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: 4 GB minimum, 8 GB recommended
- **Disk Space**: 500 MB for software + 100 MB for outputs
- **Python**: 3.8 or higher (for Python version)
- **R**: 4.0 or higher (for R version)

### Recommended

- **RAM**: 16 GB for large-scale simulations
- **CPU**: Multi-core processor for faster simulations
- **Display**: 1920x1080 or higher for viewing visualizations

## Python Installation

### Method 1: Using pip (Recommended)

#### Step 1: Clone Repository

```bash
# Clone the repository
git clone https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar.git
cd Malaria-Transmission-Model-Madagascar
```

#### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install package in editable mode
pip install -e .
```

### Method 2: Using setup.py

```bash
# Install package directly
python setup.py install

# Or install in development mode
python setup.py develop
```

## R Installation

### Step 1: Install R

Download and install R from [CRAN](https://cran.r-project.org/):
- **Windows**: Download the `.exe` installer
- **macOS**: Download the `.pkg` installer  
- **Linux**: Use package manager (e.g., `sudo apt install r-base`)

### Step 2: Install RStudio (Optional but Recommended)

Download from [RStudio](https://www.rstudio.com/products/rstudio/download/)

### Step 3: Install R Packages

Open R or RStudio and run:

```r
# Install required packages
install.packages(c(
  "tidyverse",
  "deSolve",
  "ggplot2",
  "dplyr",
  "knitr"
))

# Verify installation
library(tidyverse)
library(deSolve)
```

## Conda Installation

### Using Conda Environment

```bash
# Create environment from file
conda env create -f environment.yml

# Activate environment
conda activate malaria-model

# Verify installation
python -c "import numpy, scipy, pandas; print('Success!')"
```

### Manual Conda Installation

```bash
# Create new environment
conda create -n malaria-model python=3.10

# Activate environment
conda activate malaria-model

# Install packages
conda install -c conda-forge numpy scipy pandas matplotlib seaborn jupyter

# Install additional packages with pip
pip install -r requirements.txt
```

## Verification

### Verify Python Installation

```bash
# Check Python version
python --version

# Test imports
python -c "from src.malaria_model import MalariaModel; print('Success!')"

# Run tests
pytest tests/ -v
```

### Verify R Installation

```r
# Check R version
R.version.string

# Test script
source("scripts/Malaria-Transmission-Model-Madagascar.r")
```

### Run Example

```bash
# Python example
python example_usage.py

# Check output directory
ls output/
```

## Troubleshooting

### Common Issues

#### Issue: "Module not found" error

**Solution:**
```bash
# Make sure you're in the project directory
cd Malaria-Transmission-Model-Madagascar

# Install in editable mode
pip install -e .
```

#### Issue: "Permission denied" when installing

**Solution (Linux/macOS):**
```bash
# Use user installation
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Solution (Windows - Run as Administrator):**
- Right-click PowerShell/Command Prompt
- Select "Run as Administrator"
- Navigate to project directory
- Run installation commands

#### Issue: R packages won't install

**Solution:**
```r
# Try installing from source
install.packages("deSolve", type = "source")

# Or specify CRAN mirror
install.packages("tidyverse", repos = "https://cran.rstudio.com/")

# Update R if version is too old
# Download latest from: https://cran.r-project.org/
```

#### Issue: Jupyter notebook won't open

**Solution:**
```bash
# Install Jupyter if missing
pip install jupyter notebook

# Register Python kernel
python -m ipykernel install --user --name malaria-model

# Start Jupyter
jupyter notebook notebooks/
```

#### Issue: Tests failing

**Solution:**
```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt

# Run tests with verbose output
pytest tests/ -v -s
```

#### Issue: ImportError with scipy or numpy

**Solution:**
```bash
# Uninstall and reinstall
pip uninstall numpy scipy
pip install numpy scipy --no-cache-dir

# For conda users
conda install -c conda-forge numpy scipy
```

### Platform-Specific Issues

#### Windows

**Issue:** `scipy` installation fails

**Solution:**
```bash
# Install pre-compiled wheels
pip install scipy --prefer-binary

# Or use conda
conda install scipy
```

#### macOS

**Issue:** Command line tools missing

**Solution:**
```bash
# Install Xcode command line tools
xcode-select --install
```

#### Linux

**Issue:** Missing system libraries

**Solution (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3-dev build-essential
sudo apt install libatlas-base-dev gfortran
```

**Solution (Fedora/RHEL):**
```bash
sudo dnf install python3-devel gcc gcc-gfortran
sudo dnf install atlas-devel
```

## Getting Help

If you encounter issues not covered here:

1. **Check existing issues**: [GitHub Issues](https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/issues)
2. **Create new issue**: Provide details about your system, error messages, and steps to reproduce
3. **Email support**: freshsafoduker3@gmail.com

## Next Steps

After successful installation:

1. Read the [README.md](../README.md) for project overview
2. Run the quick start example: `python example_usage.py`
3. Explore the [Jupyter notebook](../notebooks/Malaria-Transmission-Model-Madagascar.ipynb)
4. Read the [model documentation](model_description.md)
5. Customize parameters for your use case

---

**Last Updated**: October 2025  
**Version**: 1.1.0

