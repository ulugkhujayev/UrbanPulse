from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TrafficIncident
from .serializers import TrafficIncidentSerializer


class TrafficIncidentViewSet(viewsets.ModelViewSet):
    queryset = TrafficIncident.objects.all()
    serializer_class = TrafficIncidentSerializer
    permission_classes = [IsAuthenticated]
