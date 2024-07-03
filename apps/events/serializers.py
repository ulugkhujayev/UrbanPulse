from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Event


class EventSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Event
        geo_field = "location"
        fields = (
            "id",
            "name",
            "description",
            "start_time",
            "end_time",
            "is_active",
            "created_at",
            "updated_at",
        )
