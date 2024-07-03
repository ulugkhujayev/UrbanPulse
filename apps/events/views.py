from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from apps.api.permissions import IsAdminOrReadOnly
from django_filters import rest_framework as filters


class EventFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="start_time", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="end_time", lookup_expr="lte")

    class Meta:
        model = Event
        fields = ["start_date", "end_date", "is_active"]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filterset_class = EventFilter
