from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import TrafficIncident


@admin.register(TrafficIncident)
class TrafficIncidentAdmin(OSMGeoAdmin):
    list_display = ("incident_type", "severity", "is_active", "created_at")
    list_filter = ("incident_type", "severity", "is_active")
    search_fields = ("description",)
