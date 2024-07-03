from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.transportation.models import Vehicle
from django.contrib.gis.geos import Point
from faker import Faker

fake = Faker()


class VehicleAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username=fake.user_name(), password=fake.password()
        )
        self.client.force_authenticate(user=self.user)
        self.vehicle = Vehicle.objects.create(
            vehicle_id=fake.unique.license_plate(),
            vehicle_type=fake.random_element(elements=("bus", "train", "tram")),
            location=Point(float(fake.longitude()), float(fake.latitude())),
            speed=fake.random_int(min=0, max=100),
            heading=fake.random_int(min=0, max=359),
        )
        self.url = reverse("vehicle-list")

    def test_get_vehicle_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["features"]), 1)

    def test_create_vehicle(self):
        data = {
            "vehicle_id": fake.unique.license_plate(),
            "vehicle_type": fake.random_element(elements=("bus", "train", "tram")),
            "location": {
                "type": "Point",
                "coordinates": [float(fake.longitude()), float(fake.latitude())],
            },
            "speed": fake.random_int(min=0, max=100),
            "heading": fake.random_int(min=0, max=359),
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 2)

    def test_get_vehicle_detail(self):
        url = reverse("vehicle-detail", kwargs={"pk": self.vehicle.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["properties"]["vehicle_id"], self.vehicle.vehicle_id
        )

    def test_update_vehicle(self):
        url = reverse("vehicle-detail", kwargs={"pk": self.vehicle.pk})
        data = {
            "vehicle_id": self.vehicle.vehicle_id,
            "vehicle_type": self.vehicle.vehicle_type,
            "location": {
                "type": "Point",
                "coordinates": [float(fake.longitude()), float(fake.latitude())],
            },
            "speed": fake.random_int(min=0, max=100),
            "heading": fake.random_int(min=0, max=359),
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.speed, data["speed"])

    def test_delete_vehicle(self):
        url = reverse("vehicle-detail", kwargs={"pk": self.vehicle.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vehicle.objects.count(), 0)
