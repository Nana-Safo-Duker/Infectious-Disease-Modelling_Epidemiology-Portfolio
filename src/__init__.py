"""
Malaria Transmission Model - Madagascar
A comprehensive epidemiological modeling package for malaria transmission dynamics
"""

__version__ = "1.1.0"
__author__ = "Safo et al. (2025)"

from .malaria_model import MalariaModel
from .visualization import MalariaVisualizer
from .utils import ModelParameters, SimulationResults

__all__ = [
    "MalariaModel",
    "MalariaVisualizer", 
    "ModelParameters",
    "SimulationResults"
]

