from django.test import TestCase
from django.contrib.gis.geos import Point
from apps.transportation.models import Vehicle
from utils.geofencing import check_geofence
from faker import Faker

fake = Faker()


class GeofencingTest(TestCase):
    def setUp(self):
        self.center_lat, self.center_lon = fake.latlng()
        self.vehicle1 = Vehicle.objects.create(
            vehicle_id=fake.unique.license_plate(),
            vehicle_type=fake.random_element(elements=("bus", "train", "tram")),
            location=Point(float(self.center_lon), float(self.center_lat)),
            speed=fake.random_int(min=0, max=100),
            heading=fake.random_int(min=0, max=359),
        )
        self.vehicle2 = Vehicle.objects.create(
            vehicle_id=fake.unique.license_plate(),
            vehicle_type=fake.random_element(elements=("bus", "train", "tram")),
            location=Point(float(self.center_lon + 1), float(self.center_lat + 1)),
            speed=fake.random_int(min=0, max=100),
            heading=fake.random_int(min=0, max=359),
        )

    def test_check_geofence(self):
        vehicles = check_geofence(
            float(self.center_lat), float(self.center_lon), 100000
        )
        self.assertEqual(vehicles.count(), 1)
        self.assertEqual(vehicles.first(), self.vehicle1)

        vehicles = check_geofence(
            float(self.center_lat), float(self.center_lon), 200000
        )
        self.assertEqual(vehicles.count(), 2)

        vehicles = check_geofence(float(self.center_lat), float(self.center_lon), 50000)
        self.assertEqual(vehicles.count(), 1)
        self.assertEqual(vehicles.first(), self.vehicle1)
