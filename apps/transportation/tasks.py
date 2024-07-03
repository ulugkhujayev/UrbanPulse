from celery import shared_task
from django.contrib.gis.geos import Point
from .models import Vehicle
from .api import get_vehicle_locations


@shared_task
def update_vehicle_locations():
    vehicle_data = get_vehicle_locations()
    for data in vehicle_data:
        vehicle, created = Vehicle.objects.update_or_create(
            vehicle_id=data["vehicle_id"],
            defaults={
                "vehicle_type": data["vehicle_type"],
                "location": Point(data["longitude"], data["latitude"]),
                "speed": data["speed"],
                "heading": data["heading"],
            },
        )
    return f"Updated {len(vehicle_data)} vehicles"
