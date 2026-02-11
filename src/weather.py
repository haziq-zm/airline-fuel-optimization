import random

def fetch_weather(origin, destination):
    """
    Simulated METAR/TAF effects
    """
    return {
        "headwind_knots": random.choice([-20, -10, 0, 10, 20]),
        "turbulence": random.choice(["none", "light", "moderate"]),
        "temp_deviation_c": random.choice([-5, 0, 5])
    }
