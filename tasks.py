from celery_app import celery
from sentry import sentry_sdk

# utility functions for video generation
from modules.video_generation.generate_video import generate_video
from modules.video_generation.download_video import download_video
from modules.video_generation.upload_video import upload_video
from modules.video_generation.update_video_status_and_url import update_video_status_and_url

import time

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

