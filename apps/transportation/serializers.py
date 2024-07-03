from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Vehicle, Route


class VehicleSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Vehicle
        geo_field = "location"
        fields = (
            "id",
            "vehicle_id",
            "vehicle_type",
            "speed",
            "heading",
            "created_at",
            "updated_at",
        )


class RouteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Route
        geo_field = "path"
        fields = ("id", "name", "created_at", "updated_at")
