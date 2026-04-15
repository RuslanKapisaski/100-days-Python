
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date,stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

    @staticmethod
    def find_cheapest_flight(data, return_date):
        if not data:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)

        try:
            all_flights = data.get("best_flights", []) + data.get("other_flights", [])
            all_flights = [f for f in all_flights if f.get("price") is not None]

            if not all_flights:
                print("No flights found")
                return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)

            cheapest_flight = None
            lowest_price = float("inf")

            for flight in all_flights:
                try:
                    price = flight["price"]
                    segments = flight.get("flights", [])

                    if not segments:
                        continue

                    nr_stops = len(segments) - 1

                    origin = segments[0]["departure_airport"]["id"]
                    destination = segments[-1]["arrival_airport"]["id"]
                    out_date = segments[0]["departure_airport"]["time"].split(" ")[0]

                    if price < lowest_price:
                        lowest_price = price
                        cheapest_flight = FlightData(
                            price,
                            origin,
                            destination,
                            out_date,
                            return_date,
                            nr_stops
                        )

                except (KeyError, IndexError, TypeError) as e:
                    print(f"Skipping bad flight entry: {e}")
                    continue

            if cheapest_flight is None:
                return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)

            return cheapest_flight

        except Exception as e:
            print(f"Unexpected error parsing flight data: {e}")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)