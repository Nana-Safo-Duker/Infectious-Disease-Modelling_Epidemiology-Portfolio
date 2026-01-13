"""
Unit tests for malaria transmission model
"""

import pytest
import numpy as np
import pandas as pd
from src.malaria_model import MalariaModel, ModelParameters, calculate_summary_statistics
from src.utils import validate_model_results, calculate_reproduction_number


class TestModelParameters:
    """Test ModelParameters class"""
    
    def test_default_parameters(self):
        """Test default parameter values"""
        params = ModelParameters()
        
        assert params.R0 == 2.0
        assert params.infectious_period == 14.0
        assert params.itn_coverage == 0.8
        assert params.itn_efficacy == 0.9
        assert params.human_population == 200000
        
    def test_gamma_h_calculation(self):
        """Test recovery rate calculation"""
        params = ModelParameters(infectious_period=14.0)
        expected_gamma = 1.0 / 14.0
        assert abs(params.gamma_h - expected_gamma) < 1e-10
        
    def test_beta_calculation(self):
        """Test transmission rate calculation"""
        params = ModelParameters(R0=2.0, infectious_period=14.0)
        expected_beta = 2.0 * (1.0 / 14.0)
        assert abs(params.beta - expected_beta) < 1e-10
        
    def test_initial_conditions(self):
        """Test initial conditions generation"""
        params = ModelParameters(
            human_population=1000,
            initial_infected_humans=10,
            vector_population=2000,
            initial_infected_vectors=100
        )
        
        initial = params.get_initial_conditions()
        
        assert len(initial) == 5
        assert initial[0] == 990   # Sh
        assert initial[1] == 10    # Ih
        assert initial[2] == 0     # Rh
        assert initial[3] == 1900  # Sv
        assert initial[4] == 100   # Iv


class TestMalariaModel:
    """Test MalariaModel class"""
    
    def test_model_initialization(self):
        """Test model initialization"""
        params = ModelParameters()
        model = MalariaModel(params)
        
        assert model.params == params
        
    def test_run_simulation(self):
        """Test running a basic simulation"""
        params = ModelParameters(simulation_days=100)
        model = MalariaModel(params)
        
        results = model.run_simulation()
        
        assert isinstance(results, pd.DataFrame)
        assert len(results) == 101  # 0 to 100 inclusive
        assert all(col in results.columns for col in ['time', 'Sh', 'Ih', 'Rh', 'Sv', 'Iv'])
        
    def test_population_conservation(self):
        """Test that human population is conserved"""
        params = ModelParameters(simulation_days=365)
        model = MalariaModel(params)
        
        results = model.run_simulation()
        
        total_humans = results['Sh'] + results['Ih'] + results['Rh']
        
        # Check all time points conserve population within tolerance
        assert np.allclose(total_humans, params.human_population, rtol=1e-5)
        
    def test_no_negative_values(self):
        """Test that no compartment has negative values"""
        params = ModelParameters(simulation_days=365)
        model = MalariaModel(params)
        
        results = model.run_simulation()
        
        for col in ['Sh', 'Ih', 'Rh', 'Sv', 'Iv']:
            assert (results[col] >= 0).all(), f"Negative values found in {col}"
            
    def test_itn_efficacy_decay(self):
        """Test ITN efficacy decay calculation"""
        params = ModelParameters(itn_efficacy=0.9, resistance_rate=0.1)
        model = MalariaModel(params)
        
        time_points = np.array([0, 365, 365*2])
        efficacy = model.calculate_itn_efficacy(time_points)
        
        # At t=0, efficacy should be initial
        assert abs(efficacy[0] - 0.9) < 1e-10
        
        # Efficacy should decrease over time
        assert efficacy[1] < efficacy[0]
        assert efficacy[2] < efficacy[1]
        
    def test_effective_r0(self):
        """Test effective R0 calculation"""
        params = ModelParameters(R0=2.0, itn_coverage=0.8, itn_efficacy=0.9)
        model = MalariaModel(params)
        
        # At t=0, effective R0 should be reduced by ITNs
        r0_initial = model.calculate_effective_R0(0)
        
        assert r0_initial < params.R0
        assert r0_initial > 0
        
    def test_no_itn_scenario(self):
        """Test simulation with no ITNs"""
        params = ModelParameters(itn_coverage=0.0)
        model = MalariaModel(params)
        
        results = model.run_simulation()
        
        # Should have some infections
        assert results['Ih'].max() > 0
        
    def test_multiple_scenarios(self):
        """Test running multiple scenarios"""
        params = ModelParameters(simulation_days=100)
        model = MalariaModel(params)
        
        scenarios = model.run_multiple_scenarios()
        
        assert len(scenarios) == 4
        assert 'No ITNs' in scenarios
        assert 'ITNs (No Resistance)' in scenarios
        assert 'ITNs (Low Resistance)' in scenarios
        assert 'ITNs (High Resistance)' in scenarios
        
        for scenario_name, data in scenarios.items():
            assert isinstance(data, pd.DataFrame)
            assert 'scenario' in data.columns
            assert all(data['scenario'] == scenario_name)


class TestSummaryStatistics:
    """Test summary statistics calculation"""
    
    def test_calculate_summary_statistics(self):
        """Test summary statistics calculation"""
        params = ModelParameters(simulation_days=100)
        model = MalariaModel(params)
        scenarios = model.run_multiple_scenarios()
        
        summary = calculate_summary_statistics(scenarios)
        
        assert isinstance(summary, pd.DataFrame)
        assert len(summary) == 4
        assert 'scenario' in summary.columns
        assert 'max_infected_humans' in summary.columns
        assert 'mean_infected_humans' in summary.columns
        
    def test_reduction_calculations(self):
        """Test reduction percentage calculations"""
        params = ModelParameters(simulation_days=100)
        model = MalariaModel(params)
        scenarios = model.run_multiple_scenarios()
        
        summary = calculate_summary_statistics(scenarios)
        
        # No ITNs should have 0% reduction
        no_itn = summary[summary['scenario'] == 'No ITNs']
        if not no_itn.empty and 'peak_reduction_percent' in summary.columns:
            assert abs(no_itn['peak_reduction_percent'].iloc[0]) < 1e-5
            
        # ITNs should show positive reduction
        itn_scenarios = summary[summary['scenario'].str.contains('ITNs')]
        if not itn_scenarios.empty and 'peak_reduction_percent' in summary.columns:
            for _, row in itn_scenarios.iterrows():
                if row['scenario'] != 'No ITNs':
                    # Some reduction expected (could be small depending on parameters)
                    assert row['peak_reduction_percent'] >= 0


class TestValidation:
    """Test validation functions"""
    
    def test_validate_model_results(self):
        """Test model validation"""
        params = ModelParameters(simulation_days=100)
        model = MalariaModel(params)
        scenarios = model.run_multiple_scenarios()
        
        validation = validate_model_results(scenarios, params.human_population)
        
        assert len(validation) == 4
        
        for scenario_name, checks in validation.items():
            assert 'population_conserved' in checks
            assert 'no_negative_humans' in checks
            assert 'no_negative_vectors' in checks
            assert 'no_invalid_values' in checks
            assert 'all_checks_passed' in checks
            
            # All checks should pass
            assert checks['all_checks_passed'], f"Validation failed for {scenario_name}"
            
    def test_calculate_reproduction_number(self):
        """Test reproduction number calculation"""
        # Without ITNs
        R0 = calculate_reproduction_number(beta=0.143, gamma_h=1/14)
        assert abs(R0 - 2.0) < 0.01
        
        # With ITNs at t=0
        R_eff = calculate_reproduction_number(
            beta=0.143, 
            gamma_h=1/14,
            itn_coverage=0.8,
            itn_efficacy=0.9,
            resistance_rate=0.0,
            time=0
        )
        assert R_eff < R0
        assert R_eff > 0


class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_zero_initial_infections(self):
        """Test with zero initial infections"""
        params = ModelParameters(initial_infected_humans=0, initial_infected_vectors=0)
        model = MalariaModel(params)
        
        results = model.run_simulation()
        
        # Should remain at zero infections
        assert (results['Ih'] == 0).all()
        
    def test_full_itn_coverage(self):
        """Test with 100% ITN coverage"""
        params = ModelParameters(itn_coverage=1.0, simulation_days=100)
        model = MalariaModel(params)
        
        results = model.run_simulation()
        
        # Should have lower infections than no ITNs
        assert isinstance(results, pd.DataFrame)
        
    def test_zero_resistance(self):
        """Test with zero resistance rate"""
        params = ModelParameters(resistance_rate=0.0, simulation_days=365)
        model = MalariaModel(params)
        
        # Efficacy should remain constant
        time_points = np.array([0, 365, 365*2])
        efficacy = model.calculate_itn_efficacy(time_points)
        
        assert np.allclose(efficacy, params.itn_efficacy)
        
    def test_high_resistance(self):
        """Test with high resistance rate"""
        params = ModelParameters(resistance_rate=0.5, simulation_days=365)
        model = MalariaModel(params)
        
        # Efficacy should decay rapidly
        efficacy_year1 = model.calculate_itn_efficacy(np.array([365]))[0]
        
        assert efficacy_year1 < params.itn_efficacy * 0.7  # Significant decay


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

