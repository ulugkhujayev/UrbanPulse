from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from apps.transportation.models import Vehicle


def check_geofence(latitude, longitude, radius):
    """
    Check if any vehicles are within the specified geofence.

    :param latitude: Latitude of the center of the geofence
    :param longitude: Longitude of the center of the geofence
    :param radius: Radius of the geofence in meters
    :return: QuerySet of vehicles within the geofence
    """
    center_point = Point(float(longitude), float(latitude), srid=4326)
    return Vehicle.objects.filter(location__distance_lte=(center_point, D(m=radius)))
