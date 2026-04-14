
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    @staticmethod
    def find_cheapest_flight(data, return_date):
        if data == "" or data is None:
            print("No flight data")
            return FlightData(price="N/A", origin_airport="N/A",destination_airport="N/A", out_date="N/A",  return_date="N/A")

        all_flights = data.get("best_flights", []) + data.get("other_flights", [])

        # filter out flights with no price
        all_flights = [f for f in all_flights if f.get("price") is not None]

        if not all_flights:
            print("No flights found")
            return FlightData(price="N/A", origin_airport="N/A", destination_airport="N/A", out_date="N/A",
                              return_date="N/A")

        first_flight = all_flights[0]
        lowest_price = first_flight["price"]

        origin = first_flight["flights"][0]["departure_airport"]["id"]
        destination = first_flight["flights"][-1]["arrival_airport"]["id"]
        out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]


        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

        for flight in all_flights[1:]:
            price = flight.get("price")
            if price< lowest_price:
                lowest_price = price
                origin = flight["flights"][0]["departure_airport"]["id"]
                destination = flight["flights"][-1]["arrival_airport"]["id"]
                out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

        return cheapest_flight