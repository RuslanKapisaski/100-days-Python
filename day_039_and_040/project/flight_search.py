import os
import requests
from dotenv import load_dotenv


load_dotenv()

GOOGLE_FLIGHTS_ENDPOINT = "https://serpapi.com/search?engine=google_flights"

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("SERP_API_KEY")


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time,is_direct=True):
        params = {
          "engine": "google_flights",
          "departure_id": origin_city_code,
          "arrival_id": destination_city_code,
          "outbound_date": from_time.strftime("%Y-%m-%d"),
          "return_date": to_time.strftime("%Y-%m-%d"),
          "type": "1",
          "adults": "1",
          "currency": "GBP",
          "api_key": self._api_key,
         }

        if is_direct:
            params["stops"] = 0
        else:
            params["stops"] = 1

        response = requests.get(GOOGLE_FLIGHTS_ENDPOINT, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()

        if "error" in data:
            print(f"API error: {data['error']}")
            return None

        return data


