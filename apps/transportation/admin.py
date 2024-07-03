from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Vehicle, Route


@admin.register(Vehicle)
class VehicleAdmin(OSMGeoAdmin):
    list_display = ("vehicle_id", "vehicle_type", "speed", "heading", "updated_at")
    list_filter = ("vehicle_type",)
    search_fields = ("vehicle_id",)


@admin.register(Route)
class RouteAdmin(OSMGeoAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
