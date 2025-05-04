"""Basic math operations"""
from math import sqrt as math_sqrt
import q as qq

def add(a: int | float, b: int | float) -> int | float:
    """Adds two numbers."""
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts second number from first."""
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    """Multiplies two numbers."""
    return a * b

def sqrt(x: int | float) -> float:
    """Returns the square root of a number.
    
    Args:
        x: A non-negative number
        
    Returns:
        The square root of x
        
    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math_sqrt(x)