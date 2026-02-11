import json

def load_aircraft_data(path):
    with open(path) as f:
        return json.load(f)

def estimate_fuel(distance_nm, base_burn, altitude_ft, optimal_altitude, weather):
    fuel = distance_nm * base_burn

    # Wind effect
    if weather["headwind_knots"] > 0:
        fuel *= 1.05
    elif weather["headwind_knots"] < 0:
        fuel *= 0.95

    # Altitude efficiency
    altitude_diff = abs(altitude_ft - optimal_altitude)
    fuel *= 1 + (altitude_diff / 10000) * 0.03

    return round(fuel, 2)
