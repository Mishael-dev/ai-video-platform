from celery_app import celery
from sentry import sentry_sdk

# utility functions for video generation
from utils.video_generation.get_pending_videos import get_pending_videos
from utils.video_generation.generate_video import generate_video
from utils.video_generation.download_video import download_video
from utils.video_generation.upload_video import upload_video
from utils.video_generation.update_video_status_and_url import update_video_status_and_url

import time

import uuid
print(f"--- STARTING VIDEO GENERATION TASK --- {uuid.uuid4()}")

@celery.task
def run_video_generation(video):
    try:
        script = video["script"]
        id = video["id"]
        status = video["status"]

        if status == "pending":
            video_id = generate_video(script)
            print("video_id=============")
            print(video_id)

            video_filename = download_video(video_id, id)
            print("video_filename=============")
            print(video_filename)
            
            video_url = upload_video(video_filename)
            print("video_url=============")
            print(video_url)

            result = update_video_status_and_url(video_url, id)
            print("result=============")
            print(result)
            print("==========")
            print("video generation is complete")
        else :
            raise Exception(f"Error processing video with id {video.get('id')}, this video is not pending it has already been processed or does not exist.")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Error processing video with id {video.get('id')}: {e}")


demo_video = {'id': '3825853e-be8b-40a0-a499-e4001ed4e949', 'video_idea': None, 'duration': None, 'script': 'Quick tips for daily productivity', 'music': None, 'thumbnail': None, 'hashtags': ['#productivity', '#tips', '#daily'], 'caption': 'Boost your productivity with these tips', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}

print("=============================================================================================")
start_time = time.time()
print(f"start time: {start_time}")

run_video_generation.delay(demo_video)

end_time = time.time()
print("=============================================================================================")
print(f"completion time: {end_time - start_time}")

# celery -A celery_app worker --loglevel=info --pool=solo
# celery -A celery_app beat --loglevel=info
# git commit -m"refactoring video generation: made the run_video_generation function only handle a single video object"

