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