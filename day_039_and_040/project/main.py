from datetime import datetime, timedelta

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


# Dates
today = datetime.today()
tomorrow = today + timedelta(days=1)
week_from_tomorrow = today + timedelta(weeks=1)

# Constants
ORIGIN_CITY_CODE = "SOF"
ORIGIN_CITY_NAME = "Sofia"

# Instances
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Data
sheet_data = data_manager.get_destination_data()
user_data = data_manager.get_customer_emails()

# Store all good deals
deals = []

for destination in sheet_data:
    print(f"Getting data for destination: {destination['city']}...")

    # Try direct flights
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=week_from_tomorrow,
        is_direct=True
    )

    cheapest_flight = FlightData.find_cheapest_flight(
        data=flights,
        return_date=week_from_tomorrow.strftime("%Y-%m-%d")
    )

    # If no direct flights → try indirect
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Checking indirect flights...")

        flights = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_CODE,
            destination_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=week_from_tomorrow,
            is_direct=False
        )

        cheapest_flight = FlightData.find_cheapest_flight(
            data=flights,
            return_date=week_from_tomorrow.strftime("%Y-%m-%d")
        )

    # Check if it's a deal
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price found for {destination['city']}!")

        deals.append({
            "city": destination["city"],
            "price": cheapest_flight.price,
            "out_date": cheapest_flight.out_date,
            "return_date": cheapest_flight.return_date,
            "stops": cheapest_flight.stops
        })

    print(
        f"Cheapest flight from {ORIGIN_CITY_NAME} to {destination['city']} "
        f"is GBP {cheapest_flight.price} with {cheapest_flight.stops} stops"
    )


#  Send emails ONCE per user
if deals:
    print("Sending deal emails...")

    for user in user_data:
        message = "Low price flight deals found:\n\n"

        for deal in deals:
            message += (
                f"{ORIGIN_CITY_NAME} -> {deal['city']}"
                f"Price: GBP {deal['price']}\n"
                f"Dates: {deal['out_date']} to {deal['return_date']}\n"
                f"Stops: {deal['stops']}\n\n"
            )

        notification_manager.send_email(
            user_email=user,
            message_body=message
        )

        notification_manager.send_sms(
            message_body=message)

else:
    print("No deals found today.")