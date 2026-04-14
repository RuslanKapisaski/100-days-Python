from datetime import datetime, timedelta
from pprint import pprint

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import  NotificationManager


# Get dates
today = datetime.today()
tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(weeks=24)

# Instances
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


# Find the cheapest flight in our sheet
sheet_data = data_manager.get_destination_data()

# Bulgaria iata code
ORIGIN_CITY_CODE = "SOF"
ORIGIN_CITY_NAME = "Sofia"

for destination in sheet_data:
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = FlightData.find_cheapest_flight(
        data=flights,
        return_date=six_month_from_today.strftime("%Y-%m-%d")
    )
    pprint(f"Cheapest flight from {ORIGIN_CITY_NAME} to {destination['city']} is GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")

        notification_manager.send_sms(
            message_body=f"Low price! GBP {cheapest_flight.price} | {ORIGIN_CITY_NAME} -> {destination['city']} | {cheapest_flight.out_date} to {cheapest_flight.return_date}")