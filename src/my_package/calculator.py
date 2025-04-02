"""A simple Calculator class"""

class CalculationError(Exception):
    """Custom exception for calculator errors."""
    pass

class Calculator:
    """Performs basic arithmetic operations."""
    def __init__(self, initial_value: float = 0):
        self._current_value = float(initial_value)

    @property
    def total(self) -> float:
        """Returns the current calculated value."""
        return self._current_value

    def add(self, value: float):
        """Adds a value to the current total."""
        self._current_value += float(value)
        return self

    def subtract(self, value: float):
        """Subtracts a value from the current total."""
        self._current_value -= float(value)
        return self

    def multiply(self, value: float):
        """Multiplies the current total by a value."""
        self._current_value *= float(value)
        return self

    def divide(self, value: float):
        """Divides the current total by a value."""
        if value == 0:
            raise CalculationError("Cannot divide by zero")
        self._current_value /= float(value)
        return self

    def clear(self):
        """Resets the calculator to zero."""
        self._current_value = 0.0
        return self