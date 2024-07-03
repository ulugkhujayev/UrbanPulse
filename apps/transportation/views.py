from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Vehicle, Route
from .serializers import VehicleSerializer, RouteSerializer
from apps.api.permissions import IsAdminOrReadOnly
from django_filters import rest_framework as filters


class VehicleFilter(filters.FilterSet):
    vehicle_type = filters.CharFilter(lookup_expr="iexact")
    min_speed = filters.NumberFilter(field_name="speed", lookup_expr="gte")
    max_speed = filters.NumberFilter(field_name="speed", lookup_expr="lte")

    class Meta:
        model = Vehicle
        fields = ["vehicle_type", "min_speed", "max_speed"]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filterset_class = VehicleFilter


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
