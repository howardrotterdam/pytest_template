"""Tests for basic_math module."""

import pytest
from src.my_package import basic_math

# 1. Basic Assertions
def test_add_integers():
    """Test adding two positive integers."""
    assert basic_math.add(2, 3) == 5

def test_add_floats():
    """Test adding two floating-point numbers."""
    assert basic_math.add(1.5, 2.5) == 4.0

def test_add_mixed_types():
    """Test adding an integer and a float."""
    assert basic_math.add(5, 1.5) == 6.5

def test_subtract():
    """Test subtraction."""
    assert basic_math.subtract(10, 4) == 6

def test_sqrt():
    """Test square root function."""
    assert basic_math.sqrt(4) == 2
    assert basic_math.sqrt(9) == 3
    assert basic_math.sqrt(0) == 0
    assert basic_math.sqrt(2) == pytest.approx(1.414, rel=1e-3)

def test_sqrt_negative():
    """Test square root of a negative number."""
    with pytest.raises(ValueError):
        basic_math.sqrt(-1)

# 2. Parameterization (@pytest.mark.parametrize)
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),         # Test case 1: Positive integers
        (-1, 5, -5),       # Test case 2: Negative and positive
        (0, 10, 0),        # Test case 3: Zero multiplication
        (2.5, 4, 10.0),    # Test case 4: Float and integer
        (-2, -3, 6),       # Test case 5: Two negatives
    ],
    ids=["pos*pos", "neg*pos", "zero*pos", "float*int", "neg*neg"] # Optional descriptive IDs
)
def test_multiply_parametrized(a, b, expected):
    """Test multiplication with various inputs using parametrization."""
    print(f"\n    Testing multiply({a}, {b}) == {expected}") # Visible with pytest -s
    assert basic_math.multiply(a, b) == expected

# Example of a simple test function name (pytest discovery)
def check_subtraction_with_negative():
    """Checks subtraction resulting in a negative number."""
    assert basic_math.subtract(3, 5) == -2