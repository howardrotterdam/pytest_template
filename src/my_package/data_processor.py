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