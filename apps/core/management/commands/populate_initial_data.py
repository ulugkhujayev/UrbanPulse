from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point, LineString
from apps.transportation.models import Vehicle, Route
from apps.traffic.models import TrafficIncident
from apps.events.models import Event
from faker import Faker
from datetime import timedelta


class Command(BaseCommand):
    help = "Populates the database with initial data using Faker"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating initial data...")
        fake = Faker()

        # Create vehicles
        for _ in range(50):
            Vehicle.objects.create(
                vehicle_id=fake.unique.license_plate(),
                vehicle_type=fake.random_element(elements=("bus", "train", "tram")),
                location=Point(fake.longitude(), fake.latitude()),
                speed=fake.random_int(min=0, max=100),
                heading=fake.random_int(min=0, max=359),
            )

        # Create routes
        for _ in range(10):
            Route.objects.create(
                name=fake.street_name(),
                path=LineString(
                    (fake.longitude(), fake.latitude()),
                    (fake.longitude(), fake.latitude()),
                    (fake.longitude(), fake.latitude()),
                ),
            )

        # Create traffic incidents
        for _ in range(20):
            TrafficIncident.objects.create(
                incident_type=fake.random_element(
                    elements=("accident", "construction", "congestion")
                ),
                location=Point(fake.longitude(), fake.latitude()),
                description=fake.sentence(),
                severity=fake.random_int(min=1, max=5),
            )

        # Create events
        for _ in range(15):
            start_time = fake.future_datetime(end_date="+30d")
            Event.objects.create(
                name=fake.catch_phrase(),
                description=fake.text(),
                location=Point(fake.longitude(), fake.latitude()),
                start_time=start_time,
                end_time=start_time + timedelta(hours=fake.random_int(min=1, max=8)),
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated initial data"))
