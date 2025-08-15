# Quick Start Guide

Get up and running with the Malaria Transmission Model in 5 minutes!

## 🚀 Installation (30 seconds)

```bash
# Clone the repository
git clone https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar.git
cd Malaria-Transmission-Model-Madagascar

# Install Python dependencies
pip install -r requirements.txt
```

## 🎯 Run Your First Simulation (1 minute)

### Option 1: Python (Recommended)

```bash
# Run quick example
python example_usage.py
```

**What happens:**
- ✅ Simulates 4 scenarios over 2 years
- ✅ Creates visualizations in `output/` directory
- ✅ Displays summary statistics

### Option 2: R

```r
# In R or RStudio
source("scripts/Malaria-Transmission-Model-Madagascar.r")
```

### Option 3: Jupyter Notebook

```bash
jupyter notebook notebooks/Malaria-Transmission-Model-Madagascar.ipynb
```

## 📊 View Results

Check the `output/` directory for:
- 📈 `example_human_infections.png` - Infection dynamics
- 📉 `example_itn_efficacy.png` - ITN effectiveness over time

## 🔧 Customize Parameters

### Python

```python
from src.malaria_model import MalariaModel, ModelParameters

# Change ITN coverage to 90%
params = ModelParameters(itn_coverage=0.9)

# Run simulation
model = MalariaModel(params)
results = model.run_simulation()

# View peak infections
print(f"Peak infections: {results['Ih'].max():,.0f}")
```

### R

```r
# Change ITN coverage to 90%
itn_coverage <- 0.9

# Run the rest of the script
source("scripts/Malaria-Transmission-Model-Madagascar.r")
```

## 📚 Next Steps

1. **Read the documentation**: See [README.md](README.md) for full documentation
2. **Explore the model**: Check [docs/model_description.md](docs/model_description.md)
3. **Run full analysis**: Execute `python main.py`
4. **Customize scenarios**: Edit parameters in the code
5. **View test coverage**: Run `pytest tests/ -v`

## 🆘 Common Issues

### "Module not found" error
```bash
pip install -e .
```

### R packages missing
```r
install.packages(c("tidyverse", "deSolve", "ggplot2"))
```

### Need help?
- 📧 Email: freshsafoduker3@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/issues)

## 🎓 Key Concepts

- **R₀**: Basic reproduction number (how many people one infected person infects)
- **ITN**: Insecticide-Treated Nets (bed nets that kill mosquitoes)
- **Resistance**: Mosquitoes becoming resistant to insecticides over time
- **Scenarios**: Different combinations of ITN coverage and resistance rates

## 📈 Understanding Results

Your simulation compares 4 scenarios:
1. **No ITNs** - Baseline (no intervention)
2. **ITNs (No Resistance)** - Best case scenario
3. **ITNs (Low Resistance)** - 5% resistance per year
4. **ITNs (High Resistance)** - 10% resistance per year

**Key Finding**: Even with high resistance, ITNs still reduce malaria by ~60%!

---

**Ready to dive deeper?** Check out the [full README](README.md)!

