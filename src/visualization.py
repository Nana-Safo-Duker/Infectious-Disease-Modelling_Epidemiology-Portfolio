"""
Visualization tools for malaria transmission model results
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional


class MalariaVisualizer:
    """Visualization tools for malaria model results"""
    
    def __init__(self, style: str = 'seaborn-v0_8-darkgrid'):
        """
        Initialize visualizer
        
        Args:
            style: Matplotlib style to use
        """
        plt.style.use('default')
        sns.set_palette("husl")
        self.colors = {
            'No ITNs': '#9B59B6',
            'ITNs (No Resistance)': '#00BFC4',
            'ITNs (Low Resistance)': '#4CAF50',
            'ITNs (High Resistance)': '#E64B35'
        }
        
    def plot_human_infections(self, scenarios: Dict[str, pd.DataFrame], 
                            figsize: Tuple[int, int] = (12, 6)) -> plt.Figure:
        """
        Plot infected human population over time for all scenarios
        
        Args:
            scenarios: Dictionary mapping scenario names to DataFrames
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        # Define scenario order for legend
        scenario_order = ['ITNs (High Resistance)', 'ITNs (Low Resistance)', 
                         'ITNs (No Resistance)', 'No ITNs']
        
        for scenario in scenario_order:
            if scenario in scenarios:
                data = scenarios[scenario]
                ax.plot(data['time'], data['Ih'], 
                       label=scenario, linewidth=2.5,
                       color=self.colors.get(scenario))
        
        ax.set_xlabel('Time (days)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Infected Humans', fontsize=12, fontweight='bold')
        ax.set_title('Malaria Incidence: Effect of ITNs and Resistance', 
                    fontsize=14, fontweight='bold')
        ax.legend(loc='best', frameon=True, shadow=True)
        ax.grid(True, alpha=0.3)
        
        # Format y-axis with commas
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
        
        plt.tight_layout()
        return fig
    
    def plot_vector_infections(self, scenarios: Dict[str, pd.DataFrame],
                              figsize: Tuple[int, int] = (12, 6)) -> plt.Figure:
        """
        Plot infected vector population over time for all scenarios
        
        Args:
            scenarios: Dictionary mapping scenario names to DataFrames
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        scenario_order = ['ITNs (High Resistance)', 'ITNs (Low Resistance)', 
                         'ITNs (No Resistance)', 'No ITNs']
        
        for scenario in scenario_order:
            if scenario in scenarios:
                data = scenarios[scenario]
                ax.plot(data['time'], data['Iv'], 
                       label=scenario, linewidth=2.5,
                       color=self.colors.get(scenario))
        
        ax.set_xlabel('Time (days)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Infected Vectors', fontsize=12, fontweight='bold')
        ax.set_title('Vector Infection: Effect of ITNs and Resistance', 
                    fontsize=14, fontweight='bold')
        ax.legend(loc='best', frameon=True, shadow=True)
        ax.grid(True, alpha=0.3)
        
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
        
        plt.tight_layout()
        return fig
    
    def plot_itn_efficacy(self, time_points: np.ndarray, 
                         initial_efficacy: float = 0.9,
                         resistance_rates: Dict[str, float] = None,
                         figsize: Tuple[int, int] = (12, 6)) -> plt.Figure:
        """
        Plot ITN efficacy decay over time
        
        Args:
            time_points: Array of time points
            initial_efficacy: Initial ITN efficacy (default: 0.9)
            resistance_rates: Dict mapping resistance levels to rates
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        if resistance_rates is None:
            resistance_rates = {
                'No Resistance': 0.0,
                'Low Resistance': 0.05,
                'High Resistance': 0.10
            }
        
        fig, ax = plt.subplots(figsize=figsize)
        
        colors_eff = {
            'No Resistance': '#2196F3',
            'Low Resistance': '#4CAF50',
            'High Resistance': '#E64B35'
        }
        
        for resistance_type, rate in resistance_rates.items():
            efficacy = initial_efficacy * np.exp(-rate * time_points / 365)
            ax.plot(time_points, efficacy, 
                   label=resistance_type, linewidth=2.5,
                   color=colors_eff.get(resistance_type))
        
        ax.set_xlabel('Time (days)', fontsize=12, fontweight='bold')
        ax.set_ylabel('ITN Efficacy', fontsize=12, fontweight='bold')
        ax.set_title('ITN Efficacy Over Time', fontsize=14, fontweight='bold')
        ax.legend(loc='best', frameon=True, shadow=True, title='Resistance Level')
        ax.grid(True, alpha=0.3)
        ax.set_ylim([0.5, 0.95])
        
        plt.tight_layout()
        return fig
    
    def plot_comprehensive_dashboard(self, scenarios: Dict[str, pd.DataFrame],
                                    time_points: np.ndarray,
                                    initial_efficacy: float = 0.9,
                                    resistance_rates: Dict[str, float] = None,
                                    figsize: Tuple[int, int] = (16, 10)) -> plt.Figure:
        """
        Create a comprehensive dashboard with multiple plots
        
        Args:
            scenarios: Dictionary mapping scenario names to DataFrames
            time_points: Array of time points
            initial_efficacy: Initial ITN efficacy
            resistance_rates: Dict mapping resistance levels to rates
            figsize: Figure size
            
        Returns:
            Matplotlib figure
        """
        fig = plt.figure(figsize=figsize)
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        
        # Plot 1: Human infections
        ax1 = fig.add_subplot(gs[0, 0])
        scenario_order = ['ITNs (High Resistance)', 'ITNs (Low Resistance)', 
                         'ITNs (No Resistance)', 'No ITNs']
        for scenario in scenario_order:
            if scenario in scenarios:
                data = scenarios[scenario]
                ax1.plot(data['time'], data['Ih'], 
                        label=scenario, linewidth=2,
                        color=self.colors.get(scenario))
        ax1.set_xlabel('Time (days)', fontweight='bold')
        ax1.set_ylabel('Infected Humans', fontweight='bold')
        ax1.set_title('Human Infections Over Time', fontweight='bold')
        ax1.legend(loc='best', fontsize=8)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Vector infections
        ax2 = fig.add_subplot(gs[0, 1])
        for scenario in scenario_order:
            if scenario in scenarios:
                data = scenarios[scenario]
                ax2.plot(data['time'], data['Iv'], 
                        label=scenario, linewidth=2,
                        color=self.colors.get(scenario))
        ax2.set_xlabel('Time (days)', fontweight='bold')
        ax2.set_ylabel('Infected Vectors', fontweight='bold')
        ax2.set_title('Vector Infections Over Time', fontweight='bold')
        ax2.legend(loc='best', fontsize=8)
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: ITN efficacy
        ax3 = fig.add_subplot(gs[1, 0])
        if resistance_rates is None:
            resistance_rates = {
                'No Resistance': 0.0,
                'Low Resistance': 0.05,
                'High Resistance': 0.10
            }
        colors_eff = {
            'No Resistance': '#2196F3',
            'Low Resistance': '#4CAF50',
            'High Resistance': '#E64B35'
        }
        for resistance_type, rate in resistance_rates.items():
            efficacy = initial_efficacy * np.exp(-rate * time_points / 365)
            ax3.plot(time_points, efficacy, 
                    label=resistance_type, linewidth=2,
                    color=colors_eff.get(resistance_type))
        ax3.set_xlabel('Time (days)', fontweight='bold')
        ax3.set_ylabel('ITN Efficacy', fontweight='bold')
        ax3.set_title('ITN Efficacy Decay', fontweight='bold')
        ax3.legend(loc='best', fontsize=8)
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Summary bar chart
        ax4 = fig.add_subplot(gs[1, 1])
        peak_infections = []
        scenario_names = []
        for scenario in scenario_order:
            if scenario in scenarios:
                peak_infections.append(scenarios[scenario]['Ih'].max())
                scenario_names.append(scenario.replace('ITNs ', ''))
        
        bars = ax4.bar(range(len(scenario_names)), peak_infections,
                       color=[self.colors[s] for s in scenario_order if s in scenarios])
        ax4.set_xticks(range(len(scenario_names)))
        ax4.set_xticklabels(scenario_names, rotation=15, ha='right', fontsize=8)
        ax4.set_ylabel('Peak Infected Humans', fontweight='bold')
        ax4.set_title('Peak Infection Comparison', fontweight='bold')
        ax4.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for i, (bar, val) in enumerate(zip(bars, peak_infections)):
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                    f'{int(val):,}', ha='center', va='bottom', fontsize=8)
        
        fig.suptitle('Malaria Transmission Model: Comprehensive Dashboard', 
                    fontsize=16, fontweight='bold')
        
        return fig
    
    def save_all_plots(self, scenarios: Dict[str, pd.DataFrame],
                      time_points: np.ndarray,
                      output_dir: str = 'output',
                      dpi: int = 300):
        """
        Generate and save all plots
        
        Args:
            scenarios: Dictionary mapping scenario names to DataFrames
            time_points: Array of time points
            output_dir: Directory to save plots
            dpi: Resolution for saved images
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Human infections plot
        fig = self.plot_human_infections(scenarios)
        fig.savefig(f'{output_dir}/human_infections.png', dpi=dpi, bbox_inches='tight')
        plt.close(fig)
        
        # Vector infections plot
        fig = self.plot_vector_infections(scenarios)
        fig.savefig(f'{output_dir}/vector_infections.png', dpi=dpi, bbox_inches='tight')
        plt.close(fig)
        
        # ITN efficacy plot
        fig = self.plot_itn_efficacy(time_points)
        fig.savefig(f'{output_dir}/itn_efficacy.png', dpi=dpi, bbox_inches='tight')
        plt.close(fig)
        
        # Comprehensive dashboard
        fig = self.plot_comprehensive_dashboard(scenarios, time_points)
        fig.savefig(f'{output_dir}/comprehensive_dashboard.png', dpi=dpi, bbox_inches='tight')
        plt.close(fig)
        
        print(f"All plots saved to '{output_dir}/' directory")


if __name__ == "__main__":
    # Example usage
    from malaria_model import MalariaModel, ModelParameters
    
    params = ModelParameters()
    model = MalariaModel(params)
    scenarios = model.run_multiple_scenarios()
    
    visualizer = MalariaVisualizer()
    time_points = np.arange(0, params.simulation_days + 1, 1)
    
    # Save all plots
    visualizer.save_all_plots(scenarios, time_points)

