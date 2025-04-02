"""Specific tests demonstrating pytest.raises"""

import pytest
from src.my_package import exceptions

def test_divide_normal():
    """Test normal division."""
    assert exceptions.divide_by_zero(10, 2) == 5

def test_divide_by_zero():
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        exceptions.divide_by_zero(10, 0)

def test_divide_by_zero_message():
    """Test the exact message of the ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Division by zero!"):
        exceptions.divide_by_zero(5, 0)

def test_custom_error_normal():
    """Test raising the custom error with a valid message."""
    message = "Something went wrong"
    with pytest.raises(ValueError, match=message):
        exceptions.raise_custom_error(message)

@pytest.mark.parametrize(
    "invalid_input, expected_exception",
    [
        ("", ValueError),             # Empty message raises ValueError
        (None, TypeError),           # Non-string raises TypeError
        (123, TypeError),            # Non-string raises TypeError
        ([], TypeError),             # Non-string raises TypeError
    ]
)
def test_custom_error_invalid_input(invalid_input, expected_exception):
    """Test different invalid inputs for raise_custom_error."""
    with pytest.raises(expected_exception):
        exceptions.raise_custom_error(invalid_input)

def test_no_exception_raised():
    """Demonstrates checking that NO exception is raised (less common)."""
    try:
        exceptions.divide_by_zero(100, 5)
    except Exception as e:
        pytest.fail(f"An unexpected exception was raised: {e}")
    # If no exception, the test passes