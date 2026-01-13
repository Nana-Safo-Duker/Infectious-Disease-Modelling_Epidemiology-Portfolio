"""
Malaria Transmission Model with ITN Effects and Resistance

This module implements a modified SIR epidemiological model for malaria transmission
incorporating Insecticide-Treated Nets (ITNs) and resistance effects.
"""

import numpy as np
from scipy.integrate import odeint
import pandas as pd
from dataclasses import dataclass
from typing import Tuple, Dict, List


@dataclass
class ModelParameters:
    """Parameters for the malaria transmission model"""
    
    # Epidemiological parameters
    R0: float = 2.0                    # Basic reproduction number
    infectious_period: float = 14.0    # Days
    immunity_loss_rate: float = 1/365  # Per day (1 year immunity)
    
    # Vector parameters
    carrying_capacity: float = 5e5     # Maximum vector population
    vector_death_rate: float = 1/28    # Per day
    vector_birth_rate: float = 0.08    # Per day
    
    # ITN parameters
    itn_coverage: float = 0.8          # 80% coverage
    itn_efficacy: float = 0.9          # 90% initial efficacy
    resistance_rate: float = 0.1       # 10% per year
    
    # Population parameters
    human_population: int = 200000
    vector_population: int = 400000
    initial_infected_humans: int = 1
    initial_infected_vectors: int = 10000
    
    # Simulation parameters
    simulation_days: int = 365 * 5     # 5 years
    
    @property
    def gamma_h(self) -> float:
        """Recovery rate for humans"""
        return 1 / self.infectious_period
    
    @property
    def beta(self) -> float:
        """Transmission rate"""
        return self.R0 * self.gamma_h
    
    def get_initial_conditions(self) -> np.ndarray:
        """Get initial conditions [Sh, Ih, Rh, Sv, Iv]"""
        return np.array([
            self.human_population - self.initial_infected_humans,  # Sh
            self.initial_infected_humans,                          # Ih
            0,                                                      # Rh
            self.vector_population - self.initial_infected_vectors, # Sv
            self.initial_infected_vectors                           # Iv
        ])


class MalariaModel:
    """
    Malaria transmission model with ITN effects and insecticide resistance
    
    The model includes:
    - Human compartments: Susceptible (Sh), Infected (Ih), Recovered (Rh)
    - Vector compartments: Susceptible (Sv), Infected (Iv)
    - ITN effects with time-dependent efficacy decay
    - Seasonal variation in vector mortality
    """
    
    def __init__(self, params: ModelParameters):
        """
        Initialize the malaria model
        
        Args:
            params: ModelParameters object containing all model parameters
        """
        self.params = params
        
    def _sir_si_itn_model(self, y: np.ndarray, t: float) -> List[float]:
        """
        Differential equations for the SIR-SI model with ITN effects
        
        Args:
            y: State variables [Sh, Ih, Rh, Sv, Iv]
            t: Current time (days)
            
        Returns:
            List of derivatives [dSh/dt, dIh/dt, dRh/dt, dSv/dt, dIv/dt]
        """
        Sh, Ih, Rh, Sv, Iv = y
        
        # Population sizes
        Nh = Sh + Ih + Rh
        Nv = Sv + Iv
        
        # ITN effectiveness decreases over time due to resistance
        current_efficacy = self.params.itn_efficacy * np.exp(
            -self.params.resistance_rate * t / 365
        )
        
        # Effective ITN coverage
        effective_itn_coverage = self.params.itn_coverage * current_efficacy
        
        # Transmission reduction factor due to ITNs
        transmission_reduction = 1 - effective_itn_coverage
        
        # Modified transmission rates with ITN effects
        beta_h_to_v = self.params.beta * transmission_reduction
        beta_v_to_h = self.params.beta * transmission_reduction
        
        # Seasonal vector mortality
        seasonal_mortality = (1 + np.sin(t * 2 * np.pi / 365)) / 5
        
        # Differential equations
        dSh_dt = (-beta_v_to_h * Sh * (Nv/Nh) * (Iv/Nv) / 4 + 
                  self.params.immunity_loss_rate * Rh)
        
        dIh_dt = (beta_v_to_h * Sh * (Nv/Nh) * (Iv/Nv) / 4 - 
                  self.params.gamma_h * Ih)
        
        dRh_dt = (self.params.gamma_h * Ih - 
                  self.params.immunity_loss_rate * Rh)
        
        dSv_dt = (self.params.vector_birth_rate * Nv * (1 - Nv / self.params.carrying_capacity) -
                  beta_h_to_v * Sv * (Ih/Nh) / 4 -
                  seasonal_mortality * self.params.vector_death_rate * Sv)
        
        dIv_dt = (beta_h_to_v * Sv * (Ih/Nh) / 4 -
                  seasonal_mortality * self.params.vector_death_rate * Iv)
        
        return [dSh_dt, dIh_dt, dRh_dt, dSv_dt, dIv_dt]
    
    def run_simulation(self, time_points: np.ndarray = None) -> pd.DataFrame:
        """
        Run the malaria transmission simulation
        
        Args:
            time_points: Array of time points for simulation (default: daily for simulation_days)
            
        Returns:
            DataFrame with columns: time, Sh, Ih, Rh, Sv, Iv
        """
        if time_points is None:
            time_points = np.arange(0, self.params.simulation_days + 1, 1)
        
        # Get initial conditions
        y0 = self.params.get_initial_conditions()
        
        # Solve ODE
        solution = odeint(self._sir_si_itn_model, y0, time_points)
        
        # Create DataFrame
        results = pd.DataFrame({
            'time': time_points,
            'Sh': solution[:, 0],
            'Ih': solution[:, 1],
            'Rh': solution[:, 2],
            'Sv': solution[:, 3],
            'Iv': solution[:, 4]
        })
        
        return results
    
    def run_multiple_scenarios(self) -> Dict[str, pd.DataFrame]:
        """
        Run simulations for multiple ITN scenarios
        
        Returns:
            Dictionary mapping scenario names to result DataFrames
        """
        scenarios = {}
        time_points = np.arange(0, self.params.simulation_days + 1, 1)
        
        # Scenario 1: No ITNs
        params_no_itn = ModelParameters(
            **{**vars(self.params), 'itn_coverage': 0.0}
        )
        model_no_itn = MalariaModel(params_no_itn)
        results = model_no_itn.run_simulation(time_points)
        results['scenario'] = 'No ITNs'
        scenarios['No ITNs'] = results
        
        # Scenario 2: ITNs with no resistance
        params_no_resistance = ModelParameters(
            **{**vars(self.params), 'resistance_rate': 0.0}
        )
        model_no_resistance = MalariaModel(params_no_resistance)
        results = model_no_resistance.run_simulation(time_points)
        results['scenario'] = 'ITNs (No Resistance)'
        scenarios['ITNs (No Resistance)'] = results
        
        # Scenario 3: ITNs with low resistance (5%/year)
        params_low_resistance = ModelParameters(
            **{**vars(self.params), 'resistance_rate': 0.05}
        )
        model_low_resistance = MalariaModel(params_low_resistance)
        results = model_low_resistance.run_simulation(time_points)
        results['scenario'] = 'ITNs (Low Resistance)'
        scenarios['ITNs (Low Resistance)'] = results
        
        # Scenario 4: ITNs with high resistance (10%/year)
        results = self.run_simulation(time_points)
        results['scenario'] = 'ITNs (High Resistance)'
        scenarios['ITNs (High Resistance)'] = results
        
        return scenarios
    
    def calculate_itn_efficacy(self, time_points: np.ndarray) -> np.ndarray:
        """
        Calculate ITN efficacy over time
        
        Args:
            time_points: Array of time points
            
        Returns:
            Array of efficacy values
        """
        return self.params.itn_efficacy * np.exp(
            -self.params.resistance_rate * time_points / 365
        )
    
    def calculate_effective_R0(self, time: float = 0) -> float:
        """
        Calculate effective reproduction number with ITNs
        
        Args:
            time: Time point (days)
            
        Returns:
            Effective R0 value
        """
        current_efficacy = self.params.itn_efficacy * np.exp(
            -self.params.resistance_rate * time / 365
        )
        effective_coverage = self.params.itn_coverage * current_efficacy
        return self.params.R0 * (1 - effective_coverage)


def calculate_summary_statistics(scenarios: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Calculate summary statistics for all scenarios
    
    Args:
        scenarios: Dictionary mapping scenario names to result DataFrames
        
    Returns:
        DataFrame with summary statistics
    """
    summary_stats = []
    
    for scenario_name, data in scenarios.items():
        stats = {
            'scenario': scenario_name,
            'max_infected_humans': data['Ih'].max(),
            'mean_infected_humans': data['Ih'].mean(),
            'total_infected_humans': data['Ih'].sum(),
            'max_infected_vectors': data['Iv'].max(),
            'mean_infected_vectors': data['Iv'].mean(),
        }
        summary_stats.append(stats)
    
    summary_df = pd.DataFrame(summary_stats)
    
    # Calculate reductions compared to "No ITNs" baseline
    baseline = summary_df[summary_df['scenario'] == 'No ITNs']
    if not baseline.empty:
        baseline_total = baseline['total_infected_humans'].iloc[0]
        baseline_mean = baseline['mean_infected_humans'].iloc[0]
        
        summary_df['diff_total_infected_vs_no_itn'] = (
            summary_df['total_infected_humans'] - baseline_total
        )
        summary_df['diff_mean_infected_vs_no_itn'] = (
            summary_df['mean_infected_humans'] - baseline_mean
        )
        summary_df['peak_reduction_percent'] = (
            (baseline_total - summary_df['total_infected_humans']) / baseline_total * 100
        ).round(1)
        summary_df['mean_reduction_percent'] = (
            (baseline_mean - summary_df['mean_infected_humans']) / baseline_mean * 100
        ).round(1)
    
    return summary_df


if __name__ == "__main__":
    # Example usage
    params = ModelParameters()
    model = MalariaModel(params)
    
    print("Running malaria transmission simulations...")
    scenarios = model.run_multiple_scenarios()
    
    print("\nCalculating summary statistics...")
    summary = calculate_summary_statistics(scenarios)
    print(summary)
    
    print("\nEffective R0 values:")
    print(f"  Initial (with ITNs): {model.calculate_effective_R0(0):.2f}")
    print(f"  After 5 years: {model.calculate_effective_R0(365*5):.2f}")

