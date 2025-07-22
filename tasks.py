from celery_app import celery

# utility functions for video generation
from utils.video_generation.get_pending_videos import get_pending_videos
from utils.video_generation.generate_video import generate_video
from utils.video_generation.download_video import download_video
from utils.video_generation.upload_video import upload_video
from utils.video_generation.update_video_status_and_url import update_video_status_and_url

import time

# @celery.task
def run_video_generation():
    pending_videos = get_pending_videos()
    print("pending_videos=============")
    print(pending_videos)

    for video in pending_videos:
        script = video["script"]
        print("script=============")
        print(script)

        id = video["id"]
        print("id=============")
        print(id)

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

print("=============================================================================================")
start_time = time.time()
print(f"start time: {start_time}")

run_video_generation()

end_time = time.time()
print("=============================================================================================")
print(f"completion time: {end_time - start_time}")

# celery -A celery_app worker --loglevel=info --pool=solo
# celery -A celery_app beat --loglevel=info

