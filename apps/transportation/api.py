import random
from django.contrib.gis.geos import Point


def get_vehicle_locations():
    # This is a mock API
    vehicles = []
    for i in range(50):
        vehicles.append(
            {
                "vehicle_id": f"VEH-{i:03d}",
                "vehicle_type": random.choice(["bus", "train", "tram"]),
                "latitude": random.uniform(40.7128, 40.7828),
                "longitude": random.uniform(-74.0060, -73.9360),
                "speed": random.uniform(0, 60),
                "heading": random.uniform(0, 360),
            }
        )
    return vehicles
