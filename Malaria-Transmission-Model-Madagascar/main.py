#!/usr/bin/env python3
"""
Malaria Transmission Model - Madagascar
Main execution script

This script runs the complete malaria transmission simulation with ITN effects
and generates comprehensive visualizations and reports.
"""

import numpy as np
import pandas as pd
from pathlib import Path

from src.malaria_model import MalariaModel, ModelParameters, calculate_summary_statistics
from src.visualization import MalariaVisualizer
from src.utils import SimulationResults, validate_model_results, generate_report


def main():
    """Main execution function"""
    
    print("="*80)
    print("MALARIA TRANSMISSION MODEL - MADAGASCAR")
    print("ITN Effectiveness and Insecticide Resistance Analysis")
    print("="*80)
    print()
    
    # Initialize model parameters
    print("1. Initializing model parameters...")
    params = ModelParameters(
        R0=2.0,
        infectious_period=14.0,
        itn_coverage=0.8,
        itn_efficacy=0.9,
        resistance_rate=0.1,
        human_population=200000,
        simulation_days=365 * 5  # 5 years
    )
    
    print(f"   - Basic reproduction number (R0): {params.R0}")
    print(f"   - ITN coverage: {params.itn_coverage * 100}%")
    print(f"   - Initial ITN efficacy: {params.itn_efficacy * 100}%")
    print(f"   - Resistance rate: {params.resistance_rate * 100}% per year")
    print(f"   - Simulation duration: {params.simulation_days / 365} years")
    print()
    
    # Create model and run simulations
    print("2. Running simulations for all scenarios...")
    model = MalariaModel(params)
    scenarios = model.run_multiple_scenarios()
    
    print(f"   - Completed {len(scenarios)} scenarios:")
    for scenario_name in scenarios.keys():
        print(f"     • {scenario_name}")
    print()
    
    # Calculate summary statistics
    print("3. Calculating summary statistics...")
    summary_stats = calculate_summary_statistics(scenarios)
    print(f"   - Generated summary for {len(summary_stats)} scenarios")
    print()
    
    # Validate results
    print("4. Validating model results...")
    validation = validate_model_results(scenarios, params.human_population)
    all_valid = all(v['all_checks_passed'] for v in validation.values())
    
    for scenario_name, checks in validation.items():
        status = "✓ PASSED" if checks['all_checks_passed'] else "✗ FAILED"
        print(f"   - {scenario_name}: {status}")
    
    if not all_valid:
        print("\n   WARNING: Some validation checks failed!")
    print()
    
    # Create results object
    results = SimulationResults(
        scenarios=scenarios,
        summary_statistics=summary_stats,
        parameters=vars(params)
    )
    
    # Save results to CSV
    print("5. Saving results...")
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    results.save_to_csv(str(output_dir))
    print()
    
    # Generate visualizations
    print("6. Generating visualizations...")
    visualizer = MalariaVisualizer()
    time_points = np.arange(0, params.simulation_days + 1, 1)
    
    visualizer.save_all_plots(scenarios, time_points, output_dir=str(output_dir))
    print()
    
    # Generate comprehensive report
    print("7. Generating analysis report...")
    generate_report(results, output_file=str(output_dir / 'analysis_report.txt'))
    print()
    
    # Print summary
    print("8. Analysis Summary:")
    print("-" * 80)
    results.print_summary()
    
    # Calculate effectiveness metrics
    print("\n9. ITN Effectiveness Analysis:")
    print("-" * 80)
    
    baseline = summary_stats[summary_stats['scenario'] == 'No ITNs']
    no_resistance = summary_stats[summary_stats['scenario'] == 'ITNs (No Resistance)']
    low_resistance = summary_stats[summary_stats['scenario'] == 'ITNs (Low Resistance)']
    high_resistance = summary_stats[summary_stats['scenario'] == 'ITNs (High Resistance)']
    
    if not baseline.empty:
        baseline_peak = baseline['max_infected_humans'].iloc[0]
        
        print(f"\nPeak infections without ITNs: {baseline_peak:,.0f}")
        
        if not no_resistance.empty:
            no_res_peak = no_resistance['max_infected_humans'].iloc[0]
            reduction = (baseline_peak - no_res_peak) / baseline_peak * 100
            print(f"Peak with ITNs (no resistance): {no_res_peak:,.0f} ({reduction:.1f}% reduction)")
        
        if not low_resistance.empty:
            low_res_peak = low_resistance['max_infected_humans'].iloc[0]
            reduction = (baseline_peak - low_res_peak) / baseline_peak * 100
            print(f"Peak with ITNs (low resistance): {low_res_peak:,.0f} ({reduction:.1f}% reduction)")
        
        if not high_resistance.empty:
            high_res_peak = high_resistance['max_infected_humans'].iloc[0]
            reduction = (baseline_peak - high_res_peak) / baseline_peak * 100
            print(f"Peak with ITNs (high resistance): {high_res_peak:,.0f} ({reduction:.1f}% reduction)")
        
        # Calculate effective R0 values
        print(f"\nEffective R0 values:")
        print(f"  - Initial (with ITNs): {model.calculate_effective_R0(0):.3f}")
        print(f"  - After 1 year: {model.calculate_effective_R0(365):.3f}")
        print(f"  - After 5 years: {model.calculate_effective_R0(365*5):.3f}")
        
        # ITN efficacy decay
        initial_eff = params.itn_efficacy * 100
        final_eff = model.calculate_itn_efficacy(np.array([365*5]))[0] * 100
        print(f"\nITN efficacy:")
        print(f"  - Initial: {initial_eff:.1f}%")
        print(f"  - After 5 years: {final_eff:.1f}%")
        print(f"  - Decay: {initial_eff - final_eff:.1f} percentage points")
    
    print("\n" + "="*80)
    print("SIMULATION COMPLETE")
    print("="*80)
    print(f"\nAll outputs saved to: {output_dir.absolute()}")
    print("\nGenerated files:")
    print("  - malaria_simulation_results.csv (complete time series data)")
    print("  - malaria_summary_statistics.csv (summary statistics)")
    print("  - model_parameters.json (model configuration)")
    print("  - human_infections.png (human infection plot)")
    print("  - vector_infections.png (vector infection plot)")
    print("  - itn_efficacy.png (ITN efficacy decay plot)")
    print("  - comprehensive_dashboard.png (all plots combined)")
    print("  - analysis_report.txt (detailed text report)")
    print()


if __name__ == "__main__":
    main()

