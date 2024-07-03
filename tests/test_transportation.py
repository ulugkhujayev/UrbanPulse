from django.test import TestCase
from django.contrib.gis.geos import Point, LineString
from apps.transportation.models import Vehicle, Route
from apps.transportation.serializers import VehicleSerializer, RouteSerializer
from faker import Faker

fake = Faker()


class VehicleModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            vehicle_id=fake.unique.license_plate(),
            vehicle_type=fake.random_element(elements=("bus", "train", "tram")),
            location=Point(float(fake.longitude()), float(fake.latitude())),
            speed=fake.random_int(min=0, max=100),
            heading=fake.random_int(min=0, max=359),
        )

    def test_vehicle_creation(self):
        self.assertTrue(isinstance(self.vehicle, Vehicle))
        self.assertEqual(
            self.vehicle.__str__(),
            f"{self.vehicle.get_vehicle_type_display()} - {self.vehicle.vehicle_id}",
        )


class VehicleSerializerTest(TestCase):
    def setUp(self):
        self.vehicle_attributes = {
            "vehicle_id": fake.unique.license_plate(),
            "vehicle_type": fake.random_element(elements=("bus", "train", "tram")),
            "location": Point(float(fake.longitude()), float(fake.latitude())),
            "speed": fake.random_int(min=0, max=100),
            "heading": fake.random_int(min=0, max=359),
        }
        self.serializer = VehicleSerializer(data=self.vehicle_attributes)

    def test_valid_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_fields(self):
        if self.serializer.is_valid():
            data = self.serializer.validated_data
            self.assertEqual(
                set(data.keys()),
                set(["vehicle_id", "vehicle_type", "location", "speed", "heading"]),
            )


class RouteModelTest(TestCase):
    def setUp(self):
        self.route = Route.objects.create(
            name=fake.street_name(),
            path=LineString(
                (float(fake.longitude()), float(fake.latitude())),
                (float(fake.longitude()), float(fake.latitude())),
                (float(fake.longitude()), float(fake.latitude())),
            ),
        )

    def test_route_creation(self):
        self.assertTrue(isinstance(self.route, Route))
        self.assertEqual(self.route.__str__(), self.route.name)


class RouteSerializerTest(TestCase):
    def setUp(self):
        self.route_attributes = {
            "name": fake.street_name(),
            "path": LineString(
                (float(fake.longitude()), float(fake.latitude())),
                (float(fake.longitude()), float(fake.latitude())),
                (float(fake.longitude()), float(fake.latitude())),
            ),
        }
        self.serializer = RouteSerializer(data=self.route_attributes)

    def test_valid_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_fields(self):
        if self.serializer.is_valid():
            data = self.serializer.validated_data
            self.assertEqual(set(data.keys()), set(["name", "path"]))
