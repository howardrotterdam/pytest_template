# Create a template project with test cases demonstrating all features of pytest.

## Gemini 2.5 Pro:

<thoughts>

Here's a breakdown of the thought process to generate the pytest example project:

1.  **Understand the Goal:** The request is to create a template project showcasing various pytest features through test cases. This means demonstrating core concepts, common fixtures, markers, parameterization, mocking, handling exceptions, test structure, and potentially some plugins or advanced features.

2.  **Project Structure:** A standard Python project structure is best for clarity and maintainability.
    *   A root directory (e.g., `pytest_showcase`).
    *   A source directory for the code being tested (e.g., `src/my_package`).
    *   A tests directory (e.g., `tests`).
    *   Configuration files (`pyproject.toml` for modern packaging/build/pytest config, `pytest.ini` as an alternative/older pytest config, `requirements.txt` for dependencies).
    *   A simple `README.md` explaining the project.

3.  **Code to Test:** Need some simple but non-trivial code to demonstrate various testing scenarios.
    *   **Basic Functions:** Simple arithmetic (add, subtract) to show basic assertions.
    *   **Class-Based Code:** A class with methods (e.g., `Calculator`) to demonstrate testing methods, potentially state.
    *   **Code with Dependencies/Side Effects:** A function that interacts with an external system (like reading a file or making a network request) to demonstrate mocking (`my_io.py`).
    *   **Code that Raises Exceptions:** A function designed to raise specific errors (e.g., division by zero) to demonstrate testing exception handling.

4.  **pytest Features to Demonstrate:** Brainstorm a list of key pytest features:
    *   Basic Assertions (`assert`)
    *   Test Discovery (naming conventions `test_*.py`, `*_test.py`, `Test*` classes, `test_*` methods)
    *   Fixtures (`@pytest.fixture`):
        *   Simple setup/teardown (e.g., creating an object instance).
        *   Different scopes (`function`, `class`, `module`, `session`).
        *   Using fixtures within tests and other fixtures.
        *   Built-in fixtures (`tmp_path`, `capsys`, `monkeypatch`).
    *   Parameterization (`@pytest.mark.parametrize`): Testing the same logic with multiple inputs/outputs.
    *   Markers (`@pytest.mark.*`):
        *   Skipping tests (`skip`, `skipif`).
        *   Marking expected failures (`xfail`).
        *   Custom markers (e.g., `@pytest.mark.slow`).
    *   Testing Exceptions (`pytest.raises`).
    *   Mocking (using `unittest.mock.patch` or `pytest-mock`'s `mocker` fixture).
    *   Capturing Output (`capsys` fixture).
    *   Temporary Files/Directories (`tmp_path` fixture).
    *   Structuring Tests (using classes `Test*`).
    *   Configuration (`pytest.ini` or `pyproject.toml`).
    *   Command-line options (`-v`, `-k`, `-m`, `--cov`).

5.  **Write the Test Files:** Create test files corresponding to the source code and the features to demonstrate.
    *   `tests/test_basic_math.py`: Test simple functions, parameterization.
    *   `tests/test_calculator.py`: Test the `Calculator` class, use fixtures for setup (maybe class-scoped), demonstrate testing methods.
    *   `tests/test_exceptions.py`: Show `pytest.raises`.
    *   `tests/test_fixtures.py`: Explicitly demonstrate different fixture scopes and usage, including built-in ones like `capsys` and `tmp_path`.
    *   `tests/test_markers.py`: Show `skip`, `skipif`, `xfail`, and a custom marker.
    *   `tests/test_mocking.py`: Test `my_io.py` using the `mocker` fixture (from `pytest-mock`) to patch external interactions.

6.  **Implement the Source Code:** Write the simple Python functions and classes (`src/my_package/basic_math.py`, `src/my_package/calculator.py`, `src/my_package/exceptions.py`, `src/my_package/my_io.py`) that the tests will target. Keep them minimal but sufficient to illustrate the testing concepts. Add an `__init__.py` to make `src/my_package` a package.

7.  **Configuration Files:**
    *   `requirements.txt`: List necessary dependencies (`pytest`, `pytest-mock`, `pytest-cov`).
    *   `pytest.ini`: Define custom markers, maybe some default command-line options (like `-v` or addopts), test paths.
    *   `pyproject.toml`: (Recommended Modern Approach) Define project metadata, build system, dependencies, *and* pytest configuration under `[tool.pytest.ini_options]`. This consolidates configuration. Include settings for markers, testpaths, addopts, and coverage.

8.  **README:** Write a clear `README.md` explaining:
    *   The project's purpose.
    *   The structure.
    *   How to set up the environment (create venv, install requirements).
    *   How to run the tests using various `pytest` commands (basic run, verbose, select by keyword, select by marker, run with coverGage).
    *   Briefly explain the key features demonstrated in each test file.

9.  **Refine and Review:**
    *   Read through the code and tests. Are they clear? Do they correctly demonstrate the intended features?
    *   Are the naming conventions consistent?
    *   Are the comments and docstrings helpful?
    *   Does the `README` provide enough information?
    *   Ensure the configuration files are correct.
    *   *Self-Correction:* Initially, I might forget `pytest-mock` or `pytest-cov` in requirements. Add them. Maybe I initially put pytest config *only* in `pytest.ini`, but adding it to `pyproject.toml` is more modern, so include that as the preferred way, mentioning `pytest.ini` as an alternative. Make sure the code being tested actually *needs* mocking or exception handling to make those tests meaningful. Ensure fixture scopes make sense for the examples. Make sure the `__init__.py` files are present.

10. **Format the Output:** Present the file structure clearly, provide the content for each file using code blocks, and include the instructions in the README.

</thoughts>

Okay, here is a template project structure with Python code and corresponding pytest tests demonstrating various features.

**Project Goal:** To provide a clear, runnable example showcasing common and important pytest functionalities.

**Features Demonstrated:**

1.  **Basic Assertions:** Using plain `assert` statements.
2.  **Test Discovery:** How pytest finds tests (`test_*.py` / `*_test.py` files, `Test*` classes, `test_*` functions/methods).
3.  **Fixtures (`@pytest.fixture`):**
    *   Setup/Teardown (implicit).
    *   Different scopes (`function`, `class`, `module`, `session`).
    *   Using fixtures in tests.
    *   Using fixtures within other fixtures.
    *   Built-in fixtures (`tmp_path`, `capsys`, `monkeypatch`).
4.  **Parameterization (`@pytest.mark.parametrize`):** Running tests with multiple input sets.
5.  **Markers (`@pytest.mark.*`):**
    *   `skip`: Unconditionally skip a test.
    *   `skipif`: Skip a test based on a condition.
    *   `xfail`: Mark a test as expected to fail.
    *   Custom markers for grouping/selection.
6.  **Testing Exceptions (`pytest.raises`):** Asserting that specific exceptions are raised.
7.  **Mocking/Patching:** Using `pytest-mock`'s `mocker` fixture (or `unittest.mock.patch`).
8.  **Capturing Output:** Using the `capsys` fixture to test `stdout`/`stderr`.
9.  **Temporary Directories/Files:** Using the `tmp_path` fixture.
10. **Test Grouping:** Using classes (`Test*`) to structure related tests.
11. **Configuration:** Using `pytest.ini` or `pyproject.toml`.
12. **Coverage:** Basic setup for `pytest-cov`.

---

**Project Structure:**

```
pytest_showcase/
├── .gitignore          # Standard Python gitignore
├── pyproject.toml      # Modern project metadata, dependencies, build, and pytest config
├── pytest.ini          # Alternative pytest configuration (can be omitted if using pyproject.toml)
├── requirements.txt    # List of dependencies (alternative to pyproject.toml)
├── README.md           # Project description and instructions
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── basic_math.py   # Simple functions to test
│       ├── calculator.py   # A class to test
│       ├── data_processor.py # Code needing file I/O and external interaction
│       └── exceptions.py   # Code that raises exceptions
└── tests/
    ├── __init__.py
    ├── conftest.py         # Common fixtures for tests
    ├── test_basic_math.py
    ├── test_calculator.py
    ├── test_data_processor.py
    ├── test_exceptions.py
    └── test_fixtures_and_markers.py
```

---

**File Contents:**

**`.gitignore`**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
.venv/
venv/
ENV/
env/
virtualenv/
*/activate_this.py
pip-freeze.txt
pip-log.txt

# Build artifacts
dist/
build/
*.egg-info/
*.egg

# IDEs and editors
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
Thumbs.db

# Coverage
.coverage
coverage.xml
htmlcov/
```

**`pyproject.toml`** (Recommended modern approach)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "pytest-showcase"
version = "0.1.0"
description = "A project demonstrating various pytest features."
readme = "README.md"
requires-python = ">=3.8"
# Add other project metadata as needed

dependencies = [
    # Add runtime dependencies here if any
    # e.g., "requests>=2.20"
]

[project.optional-dependencies]
test = [
    "pytest>=7.0",
    "pytest-mock>=3.0", # For mocker fixture
    "pytest-cov>=3.0",  # For coverage
]

# pytest configuration within pyproject.toml
[tool.pytest.ini_options]
minversion = "7.0"
# Specify test file paths
testpaths = [
    "tests",
]
# Default options to add when running pytest
addopts = "-v --cov=src/my_package --cov-report=term-missing --cov-report=html"
# Register custom markers to avoid warnings
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "api: marks tests that interact with external APIs (usually skipped)",
]
# Python files to consider for test discovery
python_files = "test_*.py *_test.py"
# Python classes to consider for test discovery
python_classes = "Test* *Tests"
# Python functions/methods to consider for test discovery
python_functions = "test_* check_*"

# Coverage configuration (can also be in .coveragerc)
[tool.coverage.run]
branch = true
source = ["src/my_package"]
omit = ["*/__init__.py"] # Optional: omit init files from coverage

[tool.coverage.report]
# Fail if coverage is below threshold
# fail_under = 90
show_missing = true
skip_covered = true
```

**`pytest.ini`** (Alternative if not using `pyproject.toml` for pytest config)

```ini
[pytest]
minversion = 7.0
# Specify test file paths
testpaths = tests
# Default options to add when running pytest
addopts = -v --cov=src/my_package --cov-report=term-missing --cov-report=html
# Register custom markers to avoid warnings
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    api: marks tests that interact with external APIs (usually skipped)
# Python files to consider for test discovery
python_files = test_*.py *_test.py
# Python classes to consider for test discovery
python_classes = Test* *Tests
# Python functions/methods to consider for test discovery
python_functions = test_* check_*
```

**`requirements.txt`** (Alternative for dependencies if not using `pyproject.toml`)

```txt
# Use this file if you prefer pip freeze or don't use pyproject.toml for deps
# Install with: pip install -r requirements.txt

pytest>=7.0
pytest-mock>=3.0
pytest-cov>=3.0
# Add runtime dependencies here if any
```

**`README.md`**

```markdown
# Pytest Showcase Project

This project demonstrates various features of the `pytest` framework.

## Structure

-   **`src/my_package/`**: Contains simple Python modules with code to be tested.
-   **`tests/`**: Contains the pytest test files.
-   **`tests/conftest.py`**: Defines shared fixtures.
-   **`pyproject.toml`**: Project configuration, including dependencies and pytest settings (preferred).
-   **`pytest.ini`**: Alternative pytest configuration file.
-   **`requirements.txt`**: Alternative dependency list.

## Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    (Using `pyproject.toml`)
    ```bash
    pip install -e ".[test]"
    ```
    (Using `requirements.txt`)
    ```bash
    pip install -r requirements.txt
    pip install -e . # Installs src/my_package in editable mode
    ```

## Running Tests

-   **Run all tests:**
    ```bash
    pytest
    ```
    *(Note: The `addopts` in `pyproject.toml`/`pytest.ini` makes this verbose (`-v`) and enables coverage by default).*

-   **Run specific file:**
    ```bash
    pytest tests/test_calculator.py
    ```

-   **Run tests by keyword expression (`-k`):**
    ```bash
    pytest -k "add or total" # Runs tests with 'add' or 'total' in their name
    pytest -k "TestCalculator and not total" # Selects class methods, excludes 'total'
    ```

-   **Run tests by marker (`-m`):**
    ```bash
    pytest -m slow      # Run only tests marked as 'slow'
    pytest -m "not slow" # Run all tests *except* those marked as 'slow'
    pytest -m "api"     # Run only tests marked as 'api'
    ```

-   **Stop on first failure (`-x`):**
    ```bash
    pytest -x
    ```

-   **Show print statements (`-s`):**
    ```bash
    pytest -s
    ```

-   **Generate coverage report only (without running tests again if `.coverage` exists):**
    ```bash
    pytest --cov-report=html
    ```
    *(Open `htmlcov/index.html` in your browser)*

## Features Demonstrated

-   **`tests/test_basic_math.py`**: Basic assertions, `@pytest.mark.parametrize`.
-   **`tests/test_calculator.py`**: Testing class methods, class-scoped fixtures, `pytest.raises`.
-   **`tests/test_exceptions.py`**: Focused examples of `pytest.raises`.
-   **`tests/test_fixtures_and_markers.py`**: Different fixture scopes (`function`, `module`), built-in fixtures (`capsys`), markers (`skip`, `skipif`, `xfail`, custom markers).
-   **`tests/test_data_processor.py`**: Mocking external interactions (`mocker` from `pytest-mock`), using `tmp_path` for file operations.
-   **`tests/conftest.py`**: Defining shared fixtures accessible across test files.

```

**`src/my_package/__init__.py`**

```python
# This file makes src/my_package a Python package
```

**`src/my_package/basic_math.py`**

```python
"""Basic math operations"""

def add(a: int | float, b: int | float) -> int | float:
    """Adds two numbers."""
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts second number from first."""
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    """Multiplies two numbers."""
    return a * b
```

**`src/my_package/calculator.py`**

```python
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
```

**`src/my_package/exceptions.py`**

```python
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

```

**`src/my_package/data_processor.py`**

```python
"""Module simulating data processing with external interactions"""
import json
import requests # External dependency (example)
import time
import os

class ExternalServiceError(Exception):
    """Raised when the external service fails."""
    pass

def fetch_data_from_api(api_url: str) -> dict:
    """Simulates fetching data from a slow external API."""
    print(f"\nAttempting to fetch data from {api_url}...")
    try:
        # Simulate network delay
        time.sleep(0.5)
        response = requests.get(api_url, timeout=5)
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
        print("Data fetched successfully.")
        return response.json()
    except requests.exceptions.Timeout:
        print("API request timed out.")
        raise ExternalServiceError(f"Timeout accessing {api_url}")
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        raise ExternalServiceError(f"Failed to fetch data from {api_url}: {e}")

def process_and_save_data(input_data: dict, output_filepath: str) -> None:
    """Processes fetched data and saves it to a file."""
    if not isinstance(input_data, dict):
        raise TypeError("Input data must be a dictionary.")
    if 'results' not in input_data or not isinstance(input_data['results'], list):
        raise ValueError("Input data must contain a 'results' list.")

    processed = {
        "count": len(input_data['results']),
        "items": [item.get('name', 'Unknown') for item in input_data['results']],
        "timestamp": time.time()
    }

    print(f"Processing complete. Saving {processed['count']} items to {output_filepath}")
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(processed, f, indent=4)
        print("Data saved successfully.")
    except IOError as e:
        print(f"Error saving data to {output_filepath}: {e}")
        raise IOError(f"Could not write to file {output_filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during saving: {e}")
        raise # Re-raise unexpected errors

def complex_data_pipeline(api_url: str, output_file: str) -> bool:
    """Full pipeline: fetch, process, save."""
    try:
        data = fetch_data_from_api(api_url)
        process_and_save_data(data, output_file)
        return True
    except (ExternalServiceError, TypeError, ValueError, IOError) as e:
        print(f"Data pipeline failed: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in data pipeline: {e}")
        return False

```

**`tests/__init__.py`**

```python
# This file allows Python to treat the tests directory as a package
# Usually empty
```

**`tests/conftest.py`**

```python
"""Shared fixtures for pytest"""

import pytest
import time
from src.my_package.calculator import Calculator

print("\n--- Loading conftest.py ---")

# --- Fixture Scopes ---

@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    """Fixture run once per test session."""
    start_time = time.time()
    print("\n*** SESSION START ***")
    yield
    end_time = time.time()
    print(f"\n*** SESSION END (Duration: {end_time - start_time:.2f}s) ***")

@pytest.fixture(scope="module")
def module_resource():
    """Fixture available to all tests in a module."""
    print("\n    [Module Setup] Acquiring expensive module resource...")
    resource = {"id": 1, "data": "shared_module_data"}
    yield resource
    print("\n    [Module Teardown] Releasing expensive module resource...")
    # Add cleanup code here if needed

@pytest.fixture(scope="class")
def calculator_instance_class_scoped():
    """Fixture creating a Calculator instance once per test class."""
    print("\n        {Class Setup} Creating Calculator for the class...")
    calc = Calculator()
    yield calc
    print("\n        {Class Teardown} Cleaning up class-scoped Calculator...")
    # If Calculator had complex state needing cleanup, do it here

@pytest.fixture # Default scope is "function"
def calculator_instance_func_scoped():
    """Fixture creating a fresh Calculator instance for each test function."""
    print("\n            (Function Setup) Creating fresh Calculator...")
    calc = Calculator()
    yield calc
    print("\n            (Function Teardown) Cleaning up function-scoped Calculator...")

# --- Fixture Example using another Fixture ---

@pytest.fixture(scope="module")
def derived_module_resource(module_resource):
    """Fixture that depends on another fixture."""
    print(f"\n    [Derived Module Setup] Using module resource ID: {module_resource['id']}")
    derived = {"original_id": module_resource['id'], "extra_info": "derived_data"}
    yield derived
    print("\n    [Derived Module Teardown] Cleaning up derived resource...")

# --- Fixture for Data Processing Tests ---

@pytest.fixture
def sample_api_data():
    """Provides a sample dictionary simulating API response."""
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {"name": "Item A", "value": 10},
            {"name": "Item B", "value": 20}
        ]
    }
```

**`tests/test_basic_math.py`**

```python
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
```

**`tests/test_calculator.py`**

```python
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

```

**`tests/test_exceptions.py`**

```python
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

```

**`tests/test_data_processor.py`**

```python
"""Tests for the data_processor module, demonstrating mocking and tmp_path."""

import pytest
import json
import os
from src.my_package import data_processor
from src.my_package.data_processor import ExternalServiceError

# 5. Mocking with pytest-mock (`mocker` fixture)

# You need to install pytest-mock: pip install pytest-mock

def test_fetch_data_success(mocker, sample_api_data):
    """Test successful API data fetching by mocking requests.get."""
    api_url = "http://fake-api.com/data"

    # Mock the response object that requests.get returns
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None # Simulate successful status
    mock_response.json.return_value = sample_api_data   # Provide sample data

    # Patch 'requests.get' within the module being tested
    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)

    # Also mock time.sleep to speed up the test
    mock_sleep = mocker.patch("src.my_package.data_processor.time.sleep")

    # Call the function that uses requests.get
    data = data_processor.fetch_data_from_api(api_url)

    # Assertions
    assert data == sample_api_data
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()
    mock_sleep.assert_called_once_with(0.5) # Check sleep was called

def test_fetch_data_timeout(mocker):
    """Test API timeout by making the mocked requests.get raise an exception."""
    api_url = "http://timeout-api.com/data"

    # Configure the mock to raise Timeout when called
    mocker.patch("src.my_package.data_processor.requests.get", side_effect=requests.exceptions.Timeout("Connection timed out"))
    mocker.patch("src.my_package.data_processor.time.sleep") # Still mock sleep

    with pytest.raises(ExternalServiceError, match=f"Timeout accessing {api_url}"):
        data_processor.fetch_data_from_api(api_url)

    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)


def test_fetch_data_http_error(mocker):
    """Test API returning an HTTP error status."""
    api_url = "http://error-api.com/data"

    mock_response = mocker.Mock()
    # Configure the mock to raise HTTPError when raise_for_status is called
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)
    mocker.patch("src.my_package.data_processor.time.sleep")

    with pytest.raises(ExternalServiceError, match="404 Not Found"):
        data_processor.fetch_data_from_api(api_url)

    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    mock_response.raise_for_status.assert_called_once()


# 6. Using `tmp_path` fixture for filesystem operations

def test_process_and_save_data_success(tmp_path, sample_api_data):
    """Test processing data and saving it to a temporary file."""
    # tmp_path is a pathlib.Path object pointing to a unique temp directory
    output_dir = tmp_path / "output"
    output_file = output_dir / "results.json"

    print(f"\n    Using temporary file: {output_file}")

    # Ensure the directory doesn't exist initially (it shouldn't)
    assert not output_dir.exists()

    # Call the function
    data_processor.process_and_save_data(sample_api_data, str(output_file))

    # Assertions
    assert output_file.exists() # Check if file was created
    assert output_dir.exists()  # Check if directory was created

    # Read the created file and check its content
    with open(output_file, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)

    assert saved_data["count"] == 2
    assert saved_data["items"] == ["Item A", "Item B"]
    assert "timestamp" in saved_data
    assert isinstance(saved_data["timestamp"], float)

def test_process_and_save_invalid_data(tmp_path):
    """Test saving with invalid input data structures."""
    output_file = tmp_path / "invalid.json"

    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        data_processor.process_and_save_data("not a dict", str(output_file))

    with pytest.raises(ValueError, match="Input data must contain a 'results' list"):
        data_processor.process_and_save_data({"items": []}, str(output_file))

    with pytest.raises(ValueError, match="Input data must contain a 'results' list"):
        data_processor.process_and_save_data({"results": "not a list"}, str(output_file))

    # Ensure no file was created in case of error before writing
    assert not output_file.exists()

# 7. Testing the integrated pipeline (mocking multiple steps)

def test_complex_data_pipeline_success(mocker, tmp_path, sample_api_data):
    """Test the full pipeline succeeding."""
    api_url = "http://pipeline-api.com/all"
    output_file = tmp_path / "pipeline_output.json"

    # Mock API call
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = sample_api_data
    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)
    mocker.patch("src.my_package.data_processor.time.sleep")
    mocker.patch("src.my_package.data_processor.time.time", return_value=1234567890.0) # Mock timestamp

    # Spy on the processing function to ensure it's called
    spy_process = mocker.spy(data_processor, "process_and_save_data")

    # Run pipeline
    success = data_processor.complex_data_pipeline(api_url, str(output_file))

    # Assertions
    assert success is True
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    spy_process.assert_called_once_with(sample_api_data, str(output_file))
    assert output_file.exists()
    with open(output_file, 'r') as f:
        content = json.load(f)
        assert content["count"] == 2
        assert content["timestamp"] == 1234567890.0

def test_complex_data_pipeline_api_failure(mocker, tmp_path):
    """Test the pipeline failing due to API error."""
    api_url = "http://pipeline-fail-api.com/all"
    output_file = tmp_path / "pipeline_output_fail.json"

    # Mock API call to fail
    mocker.patch("src.my_package.data_processor.requests.get", side_effect=requests.exceptions.ConnectionError)
    mocker.patch("src.my_package.data_processor.time.sleep")
    spy_process = mocker.spy(data_processor, "process_and_save_data")

    success = data_processor.complex_data_pipeline(api_url, str(output_file))

    assert success is False
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    spy_process.assert_not_called() # Process function should not be called
    assert not output_file.exists() # Output file should not be created

def test_complex_data_pipeline_save_failure(mocker, tmp_path, sample_api_data):
    """Test the pipeline failing due to file saving error."""
    api_url = "http://pipeline-save-fail.com/all"
    output_file = tmp_path / "read_only_dir" / "output.json" # Non-existent dir

    # Mock API call to succeed
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = sample_api_data
    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)
    mocker.patch("src.my_package.data_processor.time.sleep")

    # Mock os.makedirs to fail simulating permission issues or similar
    # (Alternatively, mock open() to raise IOError directly)
    mocker.patch("src.my_package.data_processor.os.makedirs", side_effect=IOError("Permission denied"))


    spy_process = mocker.spy(data_processor, "process_and_save_data")

    success = data_processor.complex_data_pipeline(api_url, str(output_file))

    assert success is False
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    # process_and_save_data *was* called, but failed internally
    spy_process.assert_called_once_with(sample_api_data, str(output_file))
    assert not os.path.exists(output_file) # File shouldn't exist

```

**`tests/test_fixtures_and_markers.py`**

```python
"""Tests demonstrating various fixtures scopes and markers."""

import pytest
import sys
import time

# Using fixtures defined in conftest.py

def test_using_module_fixture(module_resource):
    """This test uses the module-scoped fixture."""
    print("\n        Running test_using_module_fixture...")
    assert module_resource["id"] == 1
    assert module_resource["data"] == "shared_module_data"
    # Modify the fixture data (only affects tests within this module)
    module_resource["data"] = "modified_in_test_1"

def test_using_module_fixture_again(module_resource):
    """This test uses the *same* instance of the module-scoped fixture."""
    print("\n        Running test_using_module_fixture_again...")
    assert module_resource["id"] == 1
    # Check if modification from previous test persists (it should for module scope)
    assert module_resource["data"] == "modified_in_test_1"

def test_using_derived_fixture(derived_module_resource):
    """This test uses a fixture that depends on another."""
    print("\n        Running test_using_derived_fixture...")
    assert derived_module_resource["original_id"] == 1
    assert derived_module_resource["extra_info"] == "derived_data"


# 7. Using built-in `capsys` fixture to capture stdout/stderr

def test_print_output(capsys):
    """Test capturing standard output."""
    print("Hello")
    print("World", end="")
    sys.stderr.write("Error message\n")

    captured = capsys.readouterr()
    assert captured.out == "Hello\nWorld"
    assert captured.err == "Error message\n"

    # Test capturing after reading
    print("Another line")
    captured = capsys.readouterr()
    assert captured.out == "Another line\n"
    assert captured.err == ""


# 8. Markers (`skip`, `skipif`, `xfail`, custom)

@pytest.mark.skip(reason="This test is currently disabled because the feature is broken.")
def test_broken_feature():
    """This test will be skipped."""
    assert False # This code won't even run

# Skip based on Python version
@pytest.mark.skipif(sys.version_info < (3, 9), reason="Requires Python 3.9 or higher for specific syntax/feature")
def test_requires_python39():
    """This test only runs on Python 3.9+."""
    print(f"\n    Running on Python {sys.version_info.major}.{sys.version_info.minor}")
    # Example: Use a feature available from 3.9 onwards
    my_dict = {"a": 1} | {"b": 2} # Dictionary union operator (Python 3.9+)
    assert my_dict == {"a": 1, "b": 2}

# Expected failure
@pytest.mark.xfail(reason="This feature is known to be buggy, expecting failure.")
def test_expected_failure():
    """This test is expected to fail, but pytest will run it."""
    assert 1 == 2 # This assertion will fail

@pytest.mark.xfail(sys.version_info >= (3, 10), reason="Fails on Py 3.10+", strict=True)
def test_xfail_conditional_strict():
    """This test is expected to fail ONLY on Python 3.10+ and counts as failure if it passes."""
    if sys.version_info >= (3, 10):
        assert False # Force fail on 3.10+
    else:
        assert True # Should pass on older versions

# Custom Markers (defined in pytest.ini or pyproject.toml)
@pytest.mark.slow
def test_slow_operation():
    """A test marked as 'slow'."""
    print("\n    Running slow test...")
    time.sleep(0.6) # Simulate slowness
    assert True

@pytest.mark.api
@pytest.mark.skip(reason="Skipping actual API call in default runs")
def test_external_api_call():
    """A test marked as 'api' (and usually skipped)."""
    # import requests
    # response = requests.get("http://real-external-api.com")
    # assert response.status_code == 200
    print("\n    Simulating API call test (normally skipped)...")
    assert True # Placeholder

def test_normal_speed():
    """A regular test without custom markers."""
    print("\n    Running normal speed test...")
    time.sleep(0.05)
    assert True

```

---

This comprehensive set of files provides a solid foundation for understanding and utilizing many of pytest's powerful features. Remember to install the dependencies (`pip install -e ".[test]"`) and then run `pytest` from the root `pytest_showcase` directory.


# pytest generates the following error, please fix it.

mocker.patch("src.my_package.data_processor.requests.get", side_effect=requests.exceptions.Timeout("Connection timed out"))
E       NameError: name 'requests' is not defined

tests/test_data_processor.py:43: NameError

## Gemini 2.5 Pro:

<thoughts>

1.  **Identify the error:** The user provided a `NameError: name 'requests' is not defined` occurring in `tests/test_data_processor.py` at line 43.
2.  **Locate the code:** Find line 43 in `tests/test_data_processor.py`. It's inside the `test_fetch_data_timeout` function:
    ```python
    mocker.patch("src.my_package.data_processor.requests.get", side_effect=requests.exceptions.Timeout("Connection timed out"))
    ```
3.  **Analyze the error:** `NameError` means the name `requests` (specifically `requests.exceptions.Timeout`) is being used before it has been assigned a value or imported in the current scope (the test file).
4.  **Determine the cause:** The code is trying to use an exception class (`requests.exceptions.Timeout`) from the `requests` library, but the `requests` library hasn't been imported into the `test_data_processor.py` file itself. Even though the code *being tested* (`src/my_package/data_processor.py`) imports `requests`, the test file needs its own import to reference types from that library directly.
5.  **Formulate the fix:** Add `import requests` at the top of the `tests/test_data_processor.py` file.
6.  **Verify the fix (mental check):** By importing `requests`, the name `requests.exceptions.Timeout` will now be resolvable within the test file's scope.
7.  **Provide the updated code:** Show the corrected `tests/test_data_processor.py` file with the `import requests` line added.
8.  **Explain the fix:** Clearly state *why* the error occurred (missing import) and *how* the fix resolves it (by making the `requests` module and its contents available to the test code).

</thoughts>

Okay, you're absolutely right! The `NameError` occurs because the test file `tests/test_data_processor.py` itself needs to know what `requests.exceptions.Timeout` is when you pass it as the `side_effect` to `mocker.patch`. Even though the *code being tested* imports `requests`, the *test code* also needs the import if it directly references types from that library.

**The Fix:**

Add `import requests` at the top of the `tests/test_data_processor.py` file.

**Corrected `tests/test_data_processor.py`:**

```python
"""Tests for the data_processor module, demonstrating mocking and tmp_path."""

import pytest
import json
import os
import requests # <--- ADD THIS LINE
from src.my_package import data_processor
from src.my_package.data_processor import ExternalServiceError, process_and_save_data # Make process_and_save_data directly available if needed or keep calling via data_processor.*

# 5. Mocking with pytest-mock (`mocker` fixture)

# You need to install pytest-mock: pip install pytest-mock

def test_fetch_data_success(mocker, sample_api_data):
    """Test successful API data fetching by mocking requests.get."""
    api_url = "http://fake-api.com/data"

    # Mock the response object that requests.get returns
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None # Simulate successful status
    mock_response.json.return_value = sample_api_data   # Provide sample data

    # Patch 'requests.get' within the module being tested
    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)

    # Also mock time.sleep to speed up the test
    mock_sleep = mocker.patch("src.my_package.data_processor.time.sleep")

    # Call the function that uses requests.get
    data = data_processor.fetch_data_from_api(api_url)

    # Assertions
    assert data == sample_api_data
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()
    mock_sleep.assert_called_once_with(0.5) # Check sleep was called

def test_fetch_data_timeout(mocker):
    """Test API timeout by making the mocked requests.get raise an exception."""
    api_url = "http://timeout-api.com/data"

    # Configure the mock to raise Timeout when called
    # Now 'requests' is defined because of the import at the top
    mocker.patch("src.my_package.data_processor.requests.get", side_effect=requests.exceptions.Timeout("Connection timed out"))
    mocker.patch("src.my_package.data_processor.time.sleep") # Still mock sleep

    with pytest.raises(ExternalServiceError, match=f"Timeout accessing {api_url}"):
        data_processor.fetch_data_from_api(api_url)

    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)


def test_fetch_data_http_error(mocker):
    """Test API returning an HTTP error status."""
    api_url = "http://error-api.com/data"

    mock_response = mocker.Mock()
    # Configure the mock to raise HTTPError when raise_for_status is called
    # 'requests' is defined here too
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)
    mocker.patch("src.my_package.data_processor.time.sleep")

    with pytest.raises(ExternalServiceError, match="404 Not Found"):
        data_processor.fetch_data_from_api(api_url)

    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    mock_response.raise_for_status.assert_called_once()


# 6. Using `tmp_path` fixture for filesystem operations

def test_process_and_save_data_success(tmp_path, sample_api_data):
    """Test processing data and saving it to a temporary file."""
    # tmp_path is a pathlib.Path object pointing to a unique temp directory
    output_dir = tmp_path / "output"
    output_file = output_dir / "results.json"

    print(f"\n    Using temporary file: {output_file}")

    # Ensure the directory doesn't exist initially (it shouldn't)
    assert not output_dir.exists()

    # Call the function
    process_and_save_data(sample_api_data, str(output_file)) # Use direct import or data_processor.process_and_save_data

    # Assertions
    assert output_file.exists() # Check if file was created
    assert output_dir.exists()  # Check if directory was created

    # Read the created file and check its content
    with open(output_file, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)

    assert saved_data["count"] == 2
    assert saved_data["items"] == ["Item A", "Item B"]
    assert "timestamp" in saved_data
    assert isinstance(saved_data["timestamp"], float)

def test_process_and_save_invalid_data(tmp_path):
    """Test saving with invalid input data structures."""
    output_file = tmp_path / "invalid.json"

    with pytest.raises(TypeError, match="Input data must be a dictionary"):
        process_and_save_data("not a dict", str(output_file))

    with pytest.raises(ValueError, match="Input data must contain a 'results' list"):
        process_and_save_data({"items": []}, str(output_file))

    with pytest.raises(ValueError, match="Input data must contain a 'results' list"):
        process_and_save_data({"results": "not a list"}, str(output_file))

    # Ensure no file was created in case of error before writing
    assert not output_file.exists()

# 7. Testing the integrated pipeline (mocking multiple steps)

def test_complex_data_pipeline_success(mocker, tmp_path, sample_api_data):
    """Test the full pipeline succeeding."""
    api_url = "http://pipeline-api.com/all"
    output_file = tmp_path / "pipeline_output.json"

    # Mock API call
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = sample_api_data
    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)
    mocker.patch("src.my_package.data_processor.time.sleep")
    mocker.patch("src.my_package.data_processor.time.time", return_value=1234567890.0) # Mock timestamp

    # Spy on the processing function to ensure it's called
    spy_process = mocker.spy(data_processor, "process_and_save_data")

    # Run pipeline
    success = data_processor.complex_data_pipeline(api_url, str(output_file))

    # Assertions
    assert success is True
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    spy_process.assert_called_once_with(sample_api_data, str(output_file))
    assert output_file.exists()
    with open(output_file, 'r') as f:
        content = json.load(f)
        assert content["count"] == 2
        assert content["timestamp"] == 1234567890.0

def test_complex_data_pipeline_api_failure(mocker, tmp_path):
    """Test the pipeline failing due to API error."""
    api_url = "http://pipeline-fail-api.com/all"
    output_file = tmp_path / "pipeline_output_fail.json"

    # Mock API call to fail
    # 'requests' is defined here too
    mocker.patch("src.my_package.data_processor.requests.get", side_effect=requests.exceptions.ConnectionError)
    mocker.patch("src.my_package.data_processor.time.sleep")
    spy_process = mocker.spy(data_processor, "process_and_save_data")

    success = data_processor.complex_data_pipeline(api_url, str(output_file))

    assert success is False
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    spy_process.assert_not_called() # Process function should not be called
    assert not output_file.exists() # Output file should not be created

def test_complex_data_pipeline_save_failure(mocker, tmp_path, sample_api_data):
    """Test the pipeline failing due to file saving error."""
    api_url = "http://pipeline-save-fail.com/all"
    output_file = tmp_path / "read_only_dir" / "output.json" # Non-existent dir

    # Mock API call to succeed
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = sample_api_data
    mocker.patch("src.my_package.data_processor.requests.get", return_value=mock_response)
    mocker.patch("src.my_package.data_processor.time.sleep")

    # Mock os.makedirs to fail simulating permission issues or similar
    # (Alternatively, mock open() to raise IOError directly)
    mocker.patch("src.my_package.data_processor.os.makedirs", side_effect=IOError("Permission denied"))


    spy_process = mocker.spy(data_processor, "process_and_save_data")

    success = data_processor.complex_data_pipeline(api_url, str(output_file))

    assert success is False
    data_processor.requests.get.assert_called_once_with(api_url, timeout=5)
    # process_and_save_data *was* called, but failed internally
    spy_process.assert_called_once_with(sample_api_data, str(output_file))
    assert not os.path.exists(output_file) # File shouldn't exist

```

By adding `import requests` at the beginning of the file, Python can resolve `requests.exceptions.Timeout` and `requests.exceptions.ConnectionError` when those lines are executed during the test run.