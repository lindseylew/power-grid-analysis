import os
import pandas as pd
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("EIA_API_URL")
API_KEY = os.getenv("EIA_API_KEY")

def fetch_eia_data(API_URL, API_KEY):
    """
    Fetches data from the EIA API.
    
    Args:
    - api_url (str): The API URL to fetch data from.
    - api_key (str): The EIA API key.

    Returns:
    - response_json (dict): The JSON respone from the API if successful, None otherwise.
    """

    full_url = f"{API_URL}?api_key={API_KEY}"

    params = {
    "frequency": "hourly",
    "data[]": "value",
    "facets[respondent][]": "FMPP",
    "start": "2022-01-01T00",
    "end": "2024-12-31T00",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset": 0,
    "length": 5000
    }

    try:
        response = requests.get(full_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from EIA API: {e}")
        print(f"Response content: {response.content}")
        return None
    
# Function to save the data to a CSV
def save_data_to_csv(data, file_name):
    """
    Saves the fectched data to a CSV file.
    
    Args:
    -data (dict): The data to save.
    -file_name (str): the file name to save the data as (e.g., 'eia_data.csv').
    """
    if data and "response" in data:
        df = pd.DataFrame(data["response"]["data"])
        df.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")
    else:
        print("No data to save or unexpected format.")


if __name__ == "__main__":
    data = fetch_eia_data(API_URL, API_KEY)
    save_data_to_csv(data, "eia_data.csv")
    print("Data fetched and saved successfully.")

