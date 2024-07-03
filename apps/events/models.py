from django.contrib.gis.db import models
from apps.core.models import BaseModel


class Event(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.PointField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
