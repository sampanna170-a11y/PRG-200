# Taxi Fare Calculator
trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for trip in trips:

    distance = trip["distance"]
    hour = trip["hour"]
 # Base fare
    if distance <= 2:
        fare = 150

    # Between 2 km and 10 km
    elif distance <= 10:
        extra_km = distance - 2
        fare = 150 + (extra_km * 35)
