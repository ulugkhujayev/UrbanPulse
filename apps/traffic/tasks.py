from celery import shared_task
from django.utils import timezone
from .models import TrafficIncident


@shared_task
def cleanup_old_incidents():
    # Remove incidents older than 24 hours
    day_ago = timezone.now() - timezone.timedelta(days=1)
    TrafficIncident.objects.filter(created_at__lt=day_ago).delete()
    return "Old incidents cleaned up"


@shared_task
def update_incident_status():
    # Set incidents older than 2 hours to inactive
    two_hours_ago = timezone.now() - timezone.timedelta(hours=2)
    updated = TrafficIncident.objects.filter(
        created_at__lt=two_hours_ago, is_active=True
    ).update(is_active=False)
    return f"Updated {updated} incidents to inactive"
