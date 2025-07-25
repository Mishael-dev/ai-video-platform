from tasks import run_video_generation
import time

demo_video = {'id': '3825853e-be8b-40a0-a499-e4001ed4e949', 'video_idea': None, 'duration': None, 'script': 'Quick tips for daily productivity', 'music': None, 'thumbnail': None, 'hashtags': ['#productivity', '#tips', '#daily'], 'caption': 'Boost your productivity with these tips', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}

print("=============================================================================================")
start_time = time.time()
print(f"start time: {start_time}")

result = run_video_generation.delay({
    "id": "3229d6ae-0523-4b27-bb2b-1722240a287d",
    "url": None,
    "music": None,
    "script": "Quick tips for daily productivity",
    "status": "pending",
    "caption": "Boost your productivity with these tips",
    "duration": None,
    "hashtags": [
      "#productivity",
      "#tips",
      "#daily"
    ],
    "thumbnail": None,
    "created_at": "2025-07-25T06:35:22.810643+00:00",
    "updated_at": "2025-07-25T06:35:22.810643+00:00"
  })

result.get() 

end_time = time.time()
print("=============================================================================================")
print(f"completion time: {end_time - start_time}")

# celery -A celery_app worker --loglevel=info --pool=solo
# celery -A celery_app beat --loglevel=info

