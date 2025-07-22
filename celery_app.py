from celery import Celery
from celery.schedules import crontab
from sentry import sentry_sdk

celery = Celery(
    "video_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
import tasks 

celery.conf.timezone = "Africa/Lagos"
celery.conf.enable_utc = True

celery.conf.beat_schedule = {
    "run_video_generation": {
        "task": "tasks.run_video_generation",  # Notice this points to tasks.py
        "schedule": crontab(minute=16, hour=2),
    },
}