# from celery_app import celery
from all_tasks.video_generation import get_pending_videos, generate_video, download_video, upload_video, update_video_status_and_url
import time

# @celery.task
# def run_video_generation():
#     pass



def video_generation():
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

video_generation()

end_time = time.time()
print("=============================================================================================")
print(f"completion time: {end_time - start_time}")

# celery -A celery_app worker --loglevel=info --pool=solo
# celery -A celery_app beat --loglevel=info

