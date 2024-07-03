import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("urbanpulse")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update-vehicle-locations": {
        "task": "apps.transportation.tasks.update_vehicle_locations",
        "schedule": 60.0,  # every minute
    },
    "cleanup-old-incidents": {
        "task": "apps.traffic.tasks.cleanup_old_incidents",
        "schedule": crontab(hour=0, minute=0),  # daily at midnight
    },
    "update-incident-status": {
        "task": "apps.traffic.tasks.update_incident_status",
        "schedule": crontab(minute="*/15"),  # every 15 minutes
    },
}
