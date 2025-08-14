# Malaria Transmission Model - Technical Documentation

## Table of Contents
1. [Model Overview](#model-overview)
2. [Mathematical Formulation](#mathematical-formulation)
3. [Parameters](#parameters)
4. [Implementation Details](#implementation-details)
5. [Assumptions](#assumptions)
6. [Validation](#validation)
7. [References](#references)

## Model Overview

This model simulates malaria transmission dynamics in Madagascar using a modified SIR (Susceptible-Infected-Recovered) framework that incorporates both human and vector populations, with special attention to the effects of Insecticide-Treated Nets (ITNs) and the development of insecticide resistance.

### Key Components

1. **Human Population Dynamics**
   - Susceptible humans (Sh)
   - Infected humans (Ih)
   - Recovered humans (Rh)

2. **Vector Population Dynamics**
   - Susceptible mosquitoes (Sv)
   - Infected mosquitoes (Iv)

3. **Intervention Effects**
   - ITN coverage and efficacy
   - Time-dependent resistance development

4. **Environmental Factors**
   - Seasonal variation in vector mortality

## Mathematical Formulation

### Human Compartments

The human population is divided into three compartments following the SIR model:

**Susceptible Humans:**
```
dSh/dt = -βv→h * Sh * (Nv/Nh) * (Iv/Nv) * (1/4) + α * Rh
```

**Infected Humans:**
```
dIh/dt = βv→h * Sh * (Nv/Nh) * (Iv/Nv) * (1/4) - γh * Ih
```

**Recovered Humans:**
```
dRh/dt = γh * Ih - α * Rh
```

Where:
- `βv→h`: Transmission rate from vectors to humans
- `Nv/Nh`: Vector-to-human ratio
- `Iv/Nv`: Proportion of infected vectors
- `1/4`: Biting rate adjustment factor
- `γh`: Human recovery rate
- `α`: Immunity loss rate

### Vector Compartments

The vector population follows an SI (Susceptible-Infected) model with logistic growth:

**Susceptible Vectors:**
```
dSv/dt = r*Nv*(1 - Nv/K) - βh→v*Sv*(Ih/Nh)*(1/4) - [(1 + sin(2πt/365))/5]*d*Sv
```

**Infected Vectors:**
```
dIv/dt = βh→v*Sv*(Ih/Nh)*(1/4) - [(1 + sin(2πt/365))/5]*d*Iv
```

Where:
- `r`: Vector birth rate
- `K`: Carrying capacity
- `d`: Vector death rate
- `βh→v`: Transmission rate from humans to vectors
- `sin(2πt/365)`: Seasonal variation with period of 1 year

### ITN Effects

ITNs reduce transmission through a time-dependent efficacy function:

**Current Efficacy:**
```
E(t) = E₀ * exp(-r_res * t/365)
```

**Effective Coverage:**
```
C_eff(t) = C * E(t)
```

**Transmission Modification:**
```
β(t) = β₀ * (1 - C_eff(t))
```

Where:
- `E₀`: Initial ITN efficacy (typically 0.9)
- `r_res`: Resistance rate (per year)
- `C`: ITN coverage
- `β₀`: Base transmission rate

## Parameters

### Epidemiological Parameters

| Parameter | Symbol | Value | Unit | Source |
|-----------|--------|-------|------|--------|
| Basic reproduction number | R₀ | 2.0 | - | Literature |
| Infectious period | 1/γh | 14 | days | WHO |
| Immunity duration | 1/α | 365 | days | Literature |
| Recovery rate | γh | 0.071 | day⁻¹ | Calculated |
| Immunity loss rate | α | 0.0027 | day⁻¹ | Calculated |
| Transmission rate | β | 0.143 | day⁻¹ | Calculated from R₀ |

### Vector Parameters

| Parameter | Symbol | Value | Unit | Source |
|-----------|--------|-------|------|--------|
| Carrying capacity | K | 500,000 | vectors | Estimated |
| Vector death rate | d | 0.036 | day⁻¹ | Literature (28-day lifespan) |
| Vector birth rate | r | 0.08 | day⁻¹ | Fitted |
| Biting rate factor | - | 0.25 | - | Literature |

### ITN Parameters

| Parameter | Symbol | Value | Range | Notes |
|-----------|--------|-------|-------|-------|
| Coverage | C | 0.8 | 0-1 | 80% coverage |
| Initial efficacy | E₀ | 0.9 | 0-1 | 90% effectiveness |
| Resistance rate (high) | r_res | 0.10 | - | 10% per year |
| Resistance rate (low) | r_res | 0.05 | - | 5% per year |
| Resistance rate (none) | r_res | 0.0 | - | No resistance |

### Population Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Human population | 200,000 | Representative region |
| Vector population | 400,000 | 2:1 vector-to-human ratio |
| Initial infected humans | 1 | Endemic introduction |
| Initial infected vectors | 10,000 | Endemic state |

## Implementation Details

### Numerical Methods

- **ODE Solver**: LSODA (Livermore Solver for Ordinary Differential Equations)
  - Automatically switches between stiff and non-stiff methods
  - Adaptive step size control
  - Maximum step size: 0.1 days

### Time Discretization

- **Simulation Duration**: 1,825 days (5 years)
- **Time Steps**: Daily resolution
- **Output Points**: 1,826 time points (including t=0)

### Population Conservation

The model maintains conservation laws:

1. **Human Population**: `Nh(t) = Sh(t) + Ih(t) + Rh(t) = constant`
2. **Vector Population**: `Nv(t) = Sv(t) + Iv(t)` (varies due to logistic growth)

## Assumptions

### Model Assumptions

1. **Homogeneous Mixing**: All individuals have equal contact rates
2. **Closed Population**: No migration or births/deaths in human population
3. **Vector Lifespan**: Vectors do not recover from infection
4. **Immunity**: Recovered humans gain temporary immunity
5. **Seasonal Effects**: Sinusoidal variation in vector mortality
6. **ITN Effect**: Proportional reduction in transmission

### Biological Assumptions

1. **Incubation Period**: Negligible compared to infectious period
2. **Age Structure**: Homogeneous population (no age stratification)
3. **Spatial Structure**: Well-mixed population (no spatial heterogeneity)
4. **Vector Behavior**: Constant biting rates
5. **Resistance**: Exponential decay in ITN efficacy

### Intervention Assumptions

1. **ITN Distribution**: Instantaneous at t=0
2. **ITN Usage**: Perfect compliance among covered population
3. **ITN Quality**: Uniform efficacy across all nets
4. **Resistance Development**: Continuous and deterministic

## Validation

### Model Validation Checks

1. **Population Conservation**
   - Human population remains constant (±0.001%)
   - No negative compartment values

2. **Numerical Stability**
   - No infinite or NaN values
   - Smooth trajectories without oscillations

3. **Biological Plausibility**
   - Infection peaks occur within reasonable timeframes
   - Endemic equilibrium is stable
   - R₀ matches expected transmission dynamics

4. **Intervention Effects**
   - ITNs reduce transmission monotonically
   - Resistance reduces ITN effectiveness over time
   - Higher resistance leads to higher infections

### Sensitivity Analysis

Key parameters tested:
- R₀: 1.5 - 3.0
- ITN coverage: 0.4 - 1.0
- ITN efficacy: 0.7 - 1.0
- Resistance rate: 0.0 - 0.2 per year

## Calibration

### Parameter Estimation

1. **R₀**: Set to 2.0 based on literature for endemic malaria
2. **β**: Calculated from R₀ = β/γh
3. **Vector parameters**: Fitted to maintain stable vector population
4. **ITN efficacy**: Based on field trials (Bhatt et al., 2015)
5. **Resistance rates**: Based on entomological surveys (Ranson et al., 2016)

### Model Fitting

The model is not fitted to specific data but uses parameters from:
- Epidemiological literature
- WHO guidelines
- Field studies in Madagascar and similar settings

## Model Limitations

1. **Spatial Homogeneity**: Does not account for geographic variation
2. **Simplified Vector Biology**: No explicit egg/larval stages
3. **Fixed Parameters**: Many parameters vary seasonally in reality
4. **Human Behavior**: Assumes perfect ITN compliance
5. **Single Parasite Species**: Does not distinguish P. falciparum from P. vivax
6. **No Co-infections**: Ignores other diseases affecting susceptibility
7. **Deterministic**: No stochastic variation or demographic noise

## Extensions

Potential model improvements:

1. **Spatial Structure**: Metapopulation or spatial grid
2. **Age Stratification**: Different risk groups
3. **Multiple Interventions**: IRS, treatment, vaccines
4. **Stochastic Effects**: Individual-based model
5. **Climate Drivers**: Temperature and rainfall effects
6. **Drug Resistance**: Parasite resistance to treatment
7. **Genetic Dynamics**: Mosquito population genetics

## References

1. **WHO (2023)**. World Malaria Report 2023. Geneva: World Health Organization.

2. **Bhatt, S., et al. (2015)**. The effect of malaria control on Plasmodium falciparum in Africa between 2000 and 2015. *Nature*, 526(7572), 207-211.

3. **Ranson, H., et al. (2016)**. Insecticide resistance in African Anopheles mosquitoes: a worsening situation that needs urgent action. *Trends in Parasitology*, 32(3), 187-196.

4. **Griffin, J.T., et al. (2010)**. Reducing Plasmodium falciparum malaria transmission in Africa: a model-based evaluation of intervention strategies. *PLoS Medicine*, 7(8), e1000324.

5. **Ross, R. (1911)**. The Prevention of Malaria. London: John Murray. (Historical foundation)

6. **Macdonald, G. (1957)**. The Epidemiology and Control of Malaria. London: Oxford University Press.

7. **Smith, D.L., et al. (2007)**. Ross, Macdonald, and a theory for the dynamics and control of mosquito-transmitted pathogens. *PLoS Pathogens*, 3(4), e45.

---

**Version**: 1.1.0  
**Last Updated**: October 2025  
**Authors**: Safo et al. (2025)

