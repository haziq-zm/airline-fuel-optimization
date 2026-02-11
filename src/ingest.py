import csv

def load_flights(path):
    flights = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["planned_altitude_ft"] = int(row["planned_altitude_ft"])
            row["distance_nm"] = float(row["distance_nm"])
            flights.append(row)
    return flights
