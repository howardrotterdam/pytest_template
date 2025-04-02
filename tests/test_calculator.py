"""Tests for the Calculator class."""

import pytest
from src.my_package.calculator import Calculator, CalculationError

# 3. Test Grouping with Classes
# Using a class allows sharing class-scoped fixtures and organizing related tests.
@pytest.mark.usefixtures("calculator_instance_class_scoped") # Apply class-scoped fixture
class TestCalculatorClassScoped:
    """Group of tests using a single Calculator instance for the whole class."""

    def test_class_initial_total(self, calculator_instance_class_scoped):
        """Verify initial total using the class-scoped fixture."""
        print("\n        Running test_class_initial_total...")
        assert calculator_instance_class_scoped.total == 0.0

    def test_class_add_once(self, calculator_instance_class_scoped):
        """Add once and check total (state persists)."""
        print("\n        Running test_class_add_once...")
        calculator_instance_class_scoped.add(5)
        assert calculator_instance_class_scoped.total == 5.0

    def test_class_add_again(self, calculator_instance_class_scoped):
        """Add again (state should be 5.0 from previous test)."""
        # NOTE: This test DEPENDS on the previous one because the fixture is class-scoped.
        # This is often discouraged unless specifically intended.
        print("\n        Running test_class_add_again...")
        calculator_instance_class_scoped.add(10)
        assert calculator_instance_class_scoped.total == 15.0 # 5.0 + 10.0

# --- Tests using function-scoped fixtures (preferred for independence) ---

def test_func_initial_total(calculator_instance_func_scoped):
    """Verify initial total using a fresh function-scoped fixture."""
    print("\n        Running test_func_initial_total...")
    assert calculator_instance_func_scoped.total == 0.0

def test_func_add(calculator_instance_func_scoped):
    """Test add method with a fresh calculator."""
    print("\n        Running test_func_add...")
    calculator_instance_func_scoped.add(10)
    calculator_instance_func_scoped.add(5.5)
    assert calculator_instance_func_scoped.total == 15.5

def test_func_subtract(calculator_instance_func_scoped):
    """Test subtract method with a fresh calculator."""
    print("\n        Running test_func_subtract...")
    calculator_instance_func_scoped.add(100)
    calculator_instance_func_scoped.subtract(30)
    assert calculator_instance_func_scoped.total == 70.0

def test_func_multiply(calculator_instance_func_scoped):
    """Test multiply method with a fresh calculator."""
    print("\n        Running test_func_multiply...")
    calculator_instance_func_scoped.add(5)
    calculator_instance_func_scoped.multiply(3)
    assert calculator_instance_func_scoped.total == 15.0

def test_func_divide(calculator_instance_func_scoped):
    """Test divide method with a fresh calculator."""
    print("\n        Running test_func_divide...")
    calculator_instance_func_scoped.add(20)
    calculator_instance_func_scoped.divide(4)
    assert calculator_instance_func_scoped.total == 5.0

def test_func_chaining(calculator_instance_func_scoped):
    """Test method chaining."""
    print("\n        Running test_func_chaining...")
    result = calculator_instance_func_scoped.add(10).subtract(2).multiply(3).divide(4).total
    # (10 - 2) * 3 / 4 = 8 * 3 / 4 = 24 / 4 = 6
    assert result == 6.0

def test_func_clear(calculator_instance_func_scoped):
    """Test the clear method."""
    print("\n        Running test_func_clear...")
    calculator_instance_func_scoped.add(50)
    calculator_instance_func_scoped.clear()
    assert calculator_instance_func_scoped.total == 0.0

# 4. Testing for Exceptions (`pytest.raises`)
def test_divide_by_zero_raises_exception(calculator_instance_func_scoped):
    """Verify that dividing by zero raises CalculationError."""
    print("\n        Running test_divide_by_zero_raises_exception...")
    calculator_instance_func_scoped.add(10)
    with pytest.raises(CalculationError) as excinfo:
        calculator_instance_func_scoped.divide(0)
    # Optionally check the exception message
    assert "Cannot divide by zero" in str(excinfo.value)

def test_divide_by_zero_alternative_calculator():
    """Alternative way to test exception without fixture."""
    calc = Calculator(10)
    with pytest.raises(CalculationError, match="divide by zero"): # Use match regex
         calc.divide(0)