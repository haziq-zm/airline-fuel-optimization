def optimize_flight(flight, aircraft, weather):
    base_altitude = flight["planned_altitude_ft"]
    distance = flight["distance_nm"]

    scenarios = [
        base_altitude - 2000,
        base_altitude,
        base_altitude + 2000
    ]

    results = []

    for alt in scenarios:
        fuel = aircraft["estimate_fuel"](
            distance,
            aircraft["fuel_burn"],
            alt,
            aircraft["optimal_altitude_ft"],
            weather
        )
        results.append({"altitude": alt, "fuel": fuel})

    best = min(results, key=lambda x: x["fuel"])
    original = next(r for r in results if r["altitude"] == base_altitude)

    return {
        "original": original,
        "optimized": best,
        "fuel_saved": round(original["fuel"] - best["fuel"], 2)
    }
