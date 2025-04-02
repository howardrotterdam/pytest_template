"""Functions designed to raise exceptions"""

def divide_by_zero(a, b):
    """Performs division, raises ZeroDivisionError for b=0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    return a / b

def raise_custom_error(message: str):
    """Raises a custom ValueError."""
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    if not message:
        raise ValueError("Cannot raise error with empty message")
    raise ValueError(message)