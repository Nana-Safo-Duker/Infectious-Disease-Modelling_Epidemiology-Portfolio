"""
Utility functions for malaria transmission model
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
import json


@dataclass
class SimulationResults:
    """Container for simulation results"""
    scenarios: Dict[str, pd.DataFrame]
    summary_statistics: pd.DataFrame
    parameters: Dict
    
    def save_to_csv(self, output_dir: str = 'output'):
        """
        Save results to CSV files
        
        Args:
            output_dir: Directory to save files
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Combine all scenarios into one DataFrame
        all_results = pd.concat(self.scenarios.values(), ignore_index=True)
        all_results.to_csv(f'{output_dir}/malaria_simulation_results.csv', index=False)
        
        # Save summary statistics
        self.summary_statistics.to_csv(f'{output_dir}/malaria_summary_statistics.csv', index=False)
        
        # Save parameters as JSON
        with open(f'{output_dir}/model_parameters.json', 'w') as f:
            json.dump(self.parameters, f, indent=2)
        
        print(f"Results saved to '{output_dir}/' directory:")
        print(f"  - malaria_simulation_results.csv")
        print(f"  - malaria_summary_statistics.csv")
        print(f"  - model_parameters.json")
    
    def get_scenario(self, scenario_name: str) -> pd.DataFrame:
        """Get results for a specific scenario"""
        return self.scenarios.get(scenario_name)
    
    def print_summary(self):
        """Print a formatted summary of results"""
        print("\n" + "="*70)
        print("MALARIA TRANSMISSION MODEL - SIMULATION SUMMARY")
        print("="*70)
        
        print("\nModel Parameters:")
        print("-" * 70)
        for key, value in self.parameters.items():
            if isinstance(value, float):
                print(f"  {key:25s}: {value:.4f}")
            else:
                print(f"  {key:25s}: {value}")
        
        print("\nSummary Statistics:")
        print("-" * 70)
        print(self.summary_statistics.to_string(index=False))
        
        # Key findings
        baseline = self.summary_statistics[
            self.summary_statistics['scenario'] == 'No ITNs'
        ]
        high_resistance = self.summary_statistics[
            self.summary_statistics['scenario'] == 'ITNs (High Resistance)'
        ]
        
        if not baseline.empty and not high_resistance.empty:
            baseline_peak = baseline['max_infected_humans'].iloc[0]
            high_res_peak = high_resistance['max_infected_humans'].iloc[0]
            reduction = (baseline_peak - high_res_peak) / baseline_peak * 100
            
            print("\nKey Findings:")
            print("-" * 70)
            print(f"  Peak infections without ITNs: {baseline_peak:,.0f}")
            print(f"  Peak infections with ITNs (high resistance): {high_res_peak:,.0f}")
            print(f"  Reduction: {reduction:.1f}%")
            
            if reduction > 20:
                print("\n  ✓ RECOMMENDATION: ITNs are effective even with resistance")
            elif reduction > 10:
                print("\n  ⚠ RECOMMENDATION: ITNs provide moderate benefit")
            else:
                print("\n  ✗ RECOMMENDATION: ITN cost-effectiveness should be evaluated")
        
        print("="*70 + "\n")


def validate_model_results(scenarios: Dict[str, pd.DataFrame], 
                          human_population: int) -> Dict[str, bool]:
    """
    Validate simulation results
    
    Args:
        scenarios: Dictionary of scenario DataFrames
        human_population: Expected total human population
        
    Returns:
        Dictionary of validation checks
    """
    validation = {}
    
    for scenario_name, data in scenarios.items():
        # Check human population conservation
        total_humans = data['Sh'] + data['Ih'] + data['Rh']
        population_conserved = np.allclose(total_humans, human_population, rtol=1e-5)
        
        # Check for negative values
        no_negative_humans = (data[['Sh', 'Ih', 'Rh']] >= 0).all().all()
        no_negative_vectors = (data[['Sv', 'Iv']] >= 0).all().all()
        
        # Check for infinite/NaN values
        no_invalid_values = not (
            data[['Sh', 'Ih', 'Rh', 'Sv', 'Iv']].isnull().any().any() or
            np.isinf(data[['Sh', 'Ih', 'Rh', 'Sv', 'Iv']].values).any()
        )
        
        validation[scenario_name] = {
            'population_conserved': population_conserved,
            'no_negative_humans': no_negative_humans,
            'no_negative_vectors': no_negative_vectors,
            'no_invalid_values': no_invalid_values,
            'all_checks_passed': (population_conserved and no_negative_humans and 
                                 no_negative_vectors and no_invalid_values)
        }
    
    return validation


def calculate_reproduction_number(beta: float, gamma_h: float, 
                                  itn_coverage: float = 0, 
                                  itn_efficacy: float = 0,
                                  resistance_rate: float = 0,
                                  time: float = 0) -> float:
    """
    Calculate effective reproduction number
    
    Args:
        beta: Transmission rate
        gamma_h: Recovery rate
        itn_coverage: ITN coverage
        itn_efficacy: ITN efficacy
        resistance_rate: Resistance rate (per year)
        time: Time (days)
        
    Returns:
        Effective R value
    """
    R0 = beta / gamma_h
    
    if itn_coverage > 0:
        current_efficacy = itn_efficacy * np.exp(-resistance_rate * time / 365)
        effective_coverage = itn_coverage * current_efficacy
        return R0 * (1 - effective_coverage)
    
    return R0


def generate_report(results: SimulationResults, 
                   output_file: str = 'output/analysis_report.txt'):
    """
    Generate a detailed text report
    
    Args:
        results: SimulationResults object
        output_file: Path to output file
    """
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("MALARIA TRANSMISSION MODEL - COMPREHENSIVE ANALYSIS REPORT\n")
        f.write("="*80 + "\n\n")
        
        f.write("1. MODEL PARAMETERS\n")
        f.write("-"*80 + "\n")
        for key, value in results.parameters.items():
            if isinstance(value, float):
                f.write(f"  {key:30s}: {value:.4f}\n")
            else:
                f.write(f"  {key:30s}: {value}\n")
        
        f.write("\n2. SUMMARY STATISTICS\n")
        f.write("-"*80 + "\n")
        f.write(results.summary_statistics.to_string(index=False))
        
        f.write("\n\n3. SCENARIO COMPARISON\n")
        f.write("-"*80 + "\n")
        
        for scenario_name, data in results.scenarios.items():
            f.write(f"\n{scenario_name}:\n")
            f.write(f"  Peak infected humans: {data['Ih'].max():,.0f}\n")
            f.write(f"  Mean infected humans: {data['Ih'].mean():,.0f}\n")
            f.write(f"  Final infected humans: {data['Ih'].iloc[-1]:,.0f}\n")
            f.write(f"  Peak infected vectors: {data['Iv'].max():,.0f}\n")
        
        f.write("\n\n4. RECOMMENDATIONS\n")
        f.write("-"*80 + "\n")
        
        baseline = results.summary_statistics[
            results.summary_statistics['scenario'] == 'No ITNs'
        ]
        high_resistance = results.summary_statistics[
            results.summary_statistics['scenario'] == 'ITNs (High Resistance)'
        ]
        
        if not baseline.empty and not high_resistance.empty:
            reduction = high_resistance['peak_reduction_percent'].iloc[0]
            
            if reduction > 20:
                f.write("✓ ITNs should be deployed even with high resistance.\n")
                f.write(f"  They provide {reduction:.1f}% reduction in peak infections.\n")
            elif reduction > 10:
                f.write("⚠ ITNs provide moderate benefit with high resistance.\n")
                f.write("  Consider combining with other interventions.\n")
            else:
                f.write("✗ ITN cost-effectiveness should be carefully evaluated.\n")
                f.write("  Alternative interventions may be more appropriate.\n")
        
        f.write("\n" + "="*80 + "\n")
    
    print(f"Report saved to: {output_file}")


def compare_scenarios(scenarios: Dict[str, pd.DataFrame], 
                     metric: str = 'Ih',
                     time_point: int = None) -> pd.DataFrame:
    """
    Compare scenarios at a specific metric and time point
    
    Args:
        scenarios: Dictionary of scenario DataFrames
        metric: Column name to compare (e.g., 'Ih', 'Iv')
        time_point: Specific time point (None for all times)
        
    Returns:
        DataFrame with comparison
    """
    comparison = []
    
    for scenario_name, data in scenarios.items():
        if time_point is not None:
            value = data[data['time'] == time_point][metric].values
            if len(value) > 0:
                comparison.append({
                    'scenario': scenario_name,
                    'time': time_point,
                    metric: value[0]
                })
        else:
            comparison.append({
                'scenario': scenario_name,
                f'{metric}_max': data[metric].max(),
                f'{metric}_mean': data[metric].mean(),
                f'{metric}_final': data[metric].iloc[-1]
            })
    
    return pd.DataFrame(comparison)


if __name__ == "__main__":
    # Example usage
    from malaria_model import MalariaModel, ModelParameters, calculate_summary_statistics
    
    params = ModelParameters()
    model = MalariaModel(params)
    scenarios = model.run_multiple_scenarios()
    summary = calculate_summary_statistics(scenarios)
    
    results = SimulationResults(
        scenarios=scenarios,
        summary_statistics=summary,
        parameters=vars(params)
    )
    
    results.print_summary()
    results.save_to_csv()
    
    # Validation
    validation = validate_model_results(scenarios, params.human_population)
    print("\nValidation Results:")
    for scenario, checks in validation.items():
        print(f"{scenario}: {'✓ PASSED' if checks['all_checks_passed'] else '✗ FAILED'}")

