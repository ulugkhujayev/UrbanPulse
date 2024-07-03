from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from apps.transportation.serializers import VehicleSerializer
from utils.geofencing import check_geofence

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class GeofenceViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def check(self, request):
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")
        radius = request.data.get("radius")

        if not all([latitude, longitude, radius]):
            return Response(
                {"error": "Latitude, longitude, and radius are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            latitude = float(latitude)
            longitude = float(longitude)
            radius = float(radius)
        except ValueError:
            return Response(
                {"error": "Invalid latitude, longitude, or radius."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        vehicles = check_geofence(latitude, longitude, radius)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
