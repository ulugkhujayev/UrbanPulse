from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import TrafficIncident


class TrafficIncidentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrafficIncident
        geo_field = "location"
        fields = (
            "description",
            "severity",
            "is_active",
            "incident_type",
            
        )
