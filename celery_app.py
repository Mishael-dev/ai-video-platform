from celery import Celery
from celery.schedules import crontab
from sentry import sentry_sdk

celery = Celery(
    "video_tasks",
    broker="rediss://default:f4371798813641dc9ddcd2c1b24ee2d9@gusc1-honest-bluejay-32297.upstash.io:32297/?ssl_cert_reqs=required",
    backend="rediss://default:f4371798813641dc9ddcd2c1b24ee2d9@gusc1-honest-bluejay-32297.upstash.io:32297/?ssl_cert_reqs=required"
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