from django.contrib.gis.db import models
from apps.core.models import BaseModel


class Vehicle(BaseModel):
    VEHICLE_TYPES = [
        ("bus", "Bus"),
        ("train", "Train"),
        ("tram", "Tram"),
    ]
    vehicle_id = models.CharField(max_length=100, unique=True)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    location = models.PointField()
    speed = models.FloatField(default=0)
    heading = models.FloatField(default=0)

    def get_vehicle_type_display(self):
        return dict(self.VEHICLE_TYPES).get(self.vehicle_type, "Unknown")

    def __str__(self):
        return f"{self.get_vehicle_type_display()} - {self.vehicle_id}"


class Route(BaseModel):
    name = models.CharField(max_length=100)
    path = models.LineStringField()

    def __str__(self):
        return str(self.name)
