import requests

def get_data(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()