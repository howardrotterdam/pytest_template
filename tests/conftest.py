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