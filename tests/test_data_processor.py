"""Tests for the data_processor module, demonstrating mocking and tmp_path."""

import pytest
import json
import os
import requests
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