from ingest import load_flights
from weather import fetch_weather
from performance import load_aircraft_data, estimate_fuel
from optimizer import optimize_flight
from mcp_publisher import publish_recommendation

class FuelOptimizationStrand:

    def run(self):
        flights = load_flights("data/flights.csv")
        aircraft_data = load_aircraft_data("data/aircraft_performance.json")

        reports = []

        for flight in flights:
            weather = fetch_weather(flight["origin"], flight["destination"])

            aircraft = aircraft_data[flight["aircraft_type"]]
            aircraft["estimate_fuel"] = estimate_fuel
            aircraft["fuel_burn"] = aircraft["fuel_burn_kg_per_nm"]

            result = optimize_flight(flight, aircraft, weather)

            report = {
                "flight_id": flight["flight_id"],
                "weather": weather,
                "recommendation": result
            }

            publish_recommendation(report)
            reports.append(report)

        return reports
