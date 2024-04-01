import requests
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to extract data from a REST API
def extract_data(api_url, params=None, headers=None):
    try:
        # Send a GET request to the API
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP status codes 4xx/5xx

        # Extract data from the response
        data = response.json()
        return data

    except requests.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        sys.exit(1)
    except Exception as err:
        logging.error(f'An error occurred: {err}')
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Replace the URL with your API URL then uncomment the line
    # API_URL = 'https://example.com/api/data'
    # Add any required parameters or headers here
    PARAMETERS = {'key': 'value'}
    HEADERS = {'Authorization': 'Bearer your_token'}

    data = extract_data(API_URL, params=PARAMETERS, headers=HEADERS)
    logging.info(f'Data extracted: {data}')