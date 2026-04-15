import requests_cache
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_EMAILS_ENDPOINT = os.getenv("SHEETY_EMAILS_ENDPOINT")


requests_cache.install_cache()
requests.get(SHEETY_PRICES_ENDPOINT)


class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_emails = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_EMAILS_ENDPOINT,auth=self._authorization)
        data = response.json()
        for user in data["users"]:
            self.customer_emails.append(user["whatIsYourEmailAddress?"])

        return self.customer_emails

