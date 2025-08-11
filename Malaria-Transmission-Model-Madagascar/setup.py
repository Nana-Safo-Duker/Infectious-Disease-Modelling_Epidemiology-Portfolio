"""
Setup script for malaria transmission model package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="malaria-transmission-model",
    version="1.1.0",
    author="Safo et al.",
    author_email="freshsafoduker3@gmail.com",
    description="Malaria transmission model with ITN effects and resistance for Madagascar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "black>=21.0",
            "flake8>=3.9.0",
            "mypy>=0.900",
        ],
    },
    entry_points={
        "console_scripts": [
            "malaria-model=main:main",
        ],
    },
    keywords="malaria epidemiology modeling ITN insecticide-resistance Madagascar public-health",
    project_urls={
        "Bug Reports": "https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/issues",
        "Source": "https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar",
        "Documentation": "https://github.com/Nana-Safo-Duker/Malaria-Transmission-Model-Madagascar/blob/main/docs/model_description.md",
    },
)

