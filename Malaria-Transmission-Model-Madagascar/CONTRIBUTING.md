# Contributing to Malaria Transmission Model

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background or identity.

### Expected Behavior

- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Malaria-Transmission-Model-Madagascar.git
   cd Malaria-Transmission-Model-Madagascar
   ```

3. **Set up development environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install in editable mode with dev dependencies
   ```

4. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Process

### Types of Contributions

We welcome several types of contributions:

1. **Bug Fixes**: Fix issues in existing code
2. **New Features**: Add new functionality
3. **Documentation**: Improve or add documentation
4. **Tests**: Add or improve test coverage
5. **Performance**: Optimize existing code
6. **Refactoring**: Improve code quality without changing functionality

### Before You Start

1. **Check existing issues** to see if your idea is already being discussed
2. **Open an issue** to discuss major changes before implementing
3. **Ask questions** if you're unsure about anything

## Coding Standards

### Python Code Style

We follow **PEP 8** with some modifications:

```python
# Good example
def calculate_infection_rate(
    susceptible: int, 
    infected: int, 
    transmission_rate: float
) -> float:
    """
    Calculate infection rate using standard formula.
    
    Args:
        susceptible: Number of susceptible individuals
        infected: Number of infected individuals
        transmission_rate: Rate of transmission
        
    Returns:
        Infection rate
    """
    if susceptible == 0:
        return 0.0
    return transmission_rate * susceptible * infected
```

**Key Points:**
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to all functions and classes
- Use type hints where appropriate

### R Code Style

Follow the **tidyverse style guide**:

```r
# Good example
calculate_infection_rate <- function(susceptible, infected, transmission_rate) {
  # Calculate infection rate using standard formula
  #
  # Args:
  #   susceptible: Number of susceptible individuals
  #   infected: Number of infected individuals  
  #   transmission_rate: Rate of transmission
  #
  # Returns:
  #   Infection rate
  
  if (susceptible == 0) {
    return(0)
  }
  
  transmission_rate * susceptible * infected
}
```

### Code Organization

- Keep functions focused and single-purpose
- Limit function length to ~50 lines when possible
- Use meaningful names for variables and functions
- Comment complex logic
- Avoid magic numbers (use named constants)

## Testing

### Writing Tests

All new features must include tests:

```python
import pytest
from src.malaria_model import MalariaModel, ModelParameters

def test_new_feature():
    """Test description"""
    params = ModelParameters()
    model = MalariaModel(params)
    
    result = model.new_feature()
    
    assert result is not None
    assert isinstance(result, expected_type)
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_malaria_model.py

# Run with coverage
pytest --cov=src tests/

# Run with verbose output
pytest -v tests/
```

### Test Coverage

- Aim for >80% test coverage
- Test edge cases and boundary conditions
- Test error handling

## Documentation

### Docstrings

Use **NumPy-style docstrings**:

```python
def function_name(param1: int, param2: float) -> str:
    """
    Short description of function.
    
    Longer description if needed, explaining what the function does,
    when to use it, and any important considerations.
    
    Parameters
    ----------
    param1 : int
        Description of param1
    param2 : float
        Description of param2
        
    Returns
    -------
    str
        Description of return value
        
    Examples
    --------
    >>> function_name(5, 2.5)
    'result'
    
    Notes
    -----
    Any additional notes or mathematical formulas.
    """
    pass
```

### Documentation Files

- Update relevant `.md` files in `docs/`
- Update `README.md` if adding major features
- Include examples in documentation

## Submitting Changes

### Commit Messages

Write clear, descriptive commit messages:

```
# Good examples
Add ITN resistance decay function
Fix population conservation bug in vector model
Update documentation for ModelParameters class
Improve test coverage for visualization module

# Bad examples
Fix bug
Update code
Changes
```

**Format:**
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Pull Request Process

1. **Update your branch** with the latest main:
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Run tests** and ensure they pass:
   ```bash
   pytest tests/
   ```

3. **Check code style**:
   ```bash
   # Python
   black src/ tests/
   flake8 src/ tests/
   
   # R
   # Use RStudio code formatter
   ```

4. **Push your changes**:
   ```bash
   git push origin your-branch
   ```

5. **Create Pull Request** on GitHub:
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what changes were made and why
   - Include screenshots for UI changes
   - List any breaking changes

6. **Address review comments** and update as needed

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Code Review

### As a Contributor

- Respond to feedback constructively
- Make requested changes promptly
- Ask questions if feedback is unclear
- Be patient with the review process

### As a Reviewer

- Be respectful and constructive
- Focus on code, not the person
- Explain reasoning for suggestions
- Approve when satisfied with changes

## Questions?

- Open an issue for general questions
- Email: freshsafoduker3@gmail.com
- Check existing issues and documentation first

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes
- Academic citations (for significant contributions)

Thank you for contributing to malaria research and public health!

