#!/usr/bin/env python3
"""
Quick Start Example - Malaria Transmission Model

This script demonstrates basic usage of the malaria transmission model.
Perfect for getting started quickly!
"""

import numpy as np
import matplotlib.pyplot as plt
from src.malaria_model import MalariaModel, ModelParameters, calculate_summary_statistics
from src.visualization import MalariaVisualizer

def main():
    """Run a simple example simulation"""
    
    print("=" * 70)
    print("MALARIA TRANSMISSION MODEL - QUICK START EXAMPLE")
    print("=" * 70)
    print()
    
    # Step 1: Create model parameters
    print("Step 1: Creating model parameters...")
    params = ModelParameters(
        R0=2.0,                      # Basic reproduction number
        infectious_period=14.0,      # 14 days
        itn_coverage=0.8,            # 80% ITN coverage
        itn_efficacy=0.9,            # 90% initial efficacy
        resistance_rate=0.1,         # 10% resistance per year
        simulation_days=365 * 2      # 2 years simulation
    )
    print(f"  ✓ R0 = {params.R0}")
    print(f"  ✓ ITN coverage = {params.itn_coverage * 100}%")
    print(f"  ✓ Simulation duration = {params.simulation_days / 365} years")
    print()
    
    # Step 2: Create and run model
    print("Step 2: Running simulation...")
    model = MalariaModel(params)
    
    # Run single scenario
    results = model.run_simulation()
    print(f"  ✓ Simulation completed: {len(results)} time points")
    print(f"  ✓ Peak infections: {results['Ih'].max():,.0f} humans")
    print()
    
    # Step 3: Run multiple scenarios for comparison
    print("Step 3: Running all scenarios for comparison...")
    scenarios = model.run_multiple_scenarios()
    print(f"  ✓ Completed {len(scenarios)} scenarios")
    print()
    
    # Step 4: Calculate statistics
    print("Step 4: Calculating summary statistics...")
    summary = calculate_summary_statistics(scenarios)
    print(summary[['scenario', 'max_infected_humans', 'peak_reduction_percent']])
    print()
    
    # Step 5: Visualize results
    print("Step 5: Creating visualizations...")
    visualizer = MalariaVisualizer()
    
    # Plot human infections
    fig = visualizer.plot_human_infections(scenarios, figsize=(10, 6))
    plt.savefig('output/example_human_infections.png', dpi=150, bbox_inches='tight')
    print("  ✓ Saved: output/example_human_infections.png")
    
    # Plot ITN efficacy
    time_points = np.arange(0, params.simulation_days + 1, 1)
    fig = visualizer.plot_itn_efficacy(time_points, figsize=(10, 6))
    plt.savefig('output/example_itn_efficacy.png', dpi=150, bbox_inches='tight')
    print("  ✓ Saved: output/example_itn_efficacy.png")
    
    # Close plots
    plt.close('all')
    print()
    
    # Step 6: Show key findings
    print("Step 6: Key Findings")
    print("-" * 70)
    
    baseline = summary[summary['scenario'] == 'No ITNs']
    high_res = summary[summary['scenario'] == 'ITNs (High Resistance)']
    
    if not baseline.empty and not high_res.empty:
        baseline_peak = baseline['max_infected_humans'].iloc[0]
        high_res_peak = high_res['max_infected_humans'].iloc[0]
        reduction = (baseline_peak - high_res_peak) / baseline_peak * 100
        
        print(f"Peak infections without ITNs: {baseline_peak:,.0f}")
        print(f"Peak infections with ITNs (high resistance): {high_res_peak:,.0f}")
        print(f"Reduction: {reduction:.1f}%")
        print()
        
        if reduction > 20:
            print("✓ CONCLUSION: ITNs are effective even with high resistance!")
        elif reduction > 10:
            print("⚠ CONCLUSION: ITNs provide moderate benefit with resistance")
        else:
            print("✗ CONCLUSION: ITN effectiveness is limited with high resistance")
    
    print()
    print("=" * 70)
    print("Example completed successfully!")
    print("Check the 'output/' directory for generated plots.")
    print("=" * 70)


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    import os
    os.makedirs('output', exist_ok=True)
    
    # Run example
    main()

