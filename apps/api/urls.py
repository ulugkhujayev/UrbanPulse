from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.transportation.views import VehicleViewSet, RouteViewSet
from apps.traffic.views import TrafficIncidentViewSet
from apps.events.views import EventViewSet
from .views import UserViewSet, GeofenceViewSet

router = DefaultRouter()
router.register(r"vehicles", VehicleViewSet)
router.register(r"routes", RouteViewSet)
router.register(r"traffic-incidents", TrafficIncidentViewSet)
router.register(r"events", EventViewSet)
router.register(r"users", UserViewSet)
router.register(r"geofence", GeofenceViewSet, basename="geofence")

urlpatterns = [
    path("", include(router.urls)),
]
