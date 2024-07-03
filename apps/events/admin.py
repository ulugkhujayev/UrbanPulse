from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Event


@admin.register(Event)
class EventAdmin(OSMGeoAdmin):
    list_display = ("name", "start_time", "end_time", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
