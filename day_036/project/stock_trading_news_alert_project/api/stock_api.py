import os
from dotenv import load_dotenv

from utils.requester import get_data

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.getenv("NEWS_API_KEY")

PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

def check_stock():
    data = get_data(url="https://www.alphavantage.co/query", params=PARAMETERS)
    print(data)
    time_series = data["Time Series (Daily)"]
    dates = list(time_series.keys())

    yesterday_close = float(time_series[dates[0]]["4. close"])
    day_before_close = float(time_series[dates[1]]["4. close"])

    difference = abs(yesterday_close - day_before_close)
    percent_change = (difference / day_before_close) * 100

    return percent_change
