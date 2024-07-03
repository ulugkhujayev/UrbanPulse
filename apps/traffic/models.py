from django.contrib.gis.db import models
from apps.core.models import BaseModel


class TrafficIncident(BaseModel):
    INCIDENT_TYPES = (
        ("accident", "Accident"),
        ("construction", "Construction"),
        ("congestion", "Congestion"),
    )
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    location = models.PointField()
    description = models.TextField()
    severity = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_active = models.BooleanField(default=True)

    def get_incident_type_display(self):
        return dict(self.INCIDENT_TYPES).get(self.incident_type, "Unknown")

    def __str__(self):
        return f"{self.get_incident_type_display()} at {self.location}"
