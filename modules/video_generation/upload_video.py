from db import supabase
from sentry import sentry_sdk
import os

def upload_video(file_name):
    try:
        video_filepath = os.path.join("videos", file_name)
        with open(video_filepath, "rb") as f:
            response = (
                supabase.storage
                .from_("generated-videos")
                .upload(
                    file=f,
                    path=file_name,
                    file_options={
                "cache-control": "3600",
                "upsert": "false",
                "content-type": "video/mp4"   # <-- set correct MIME type here
            }
                )
            )
        url = f"https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//{response.path}"
        return url

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Error during (video_generation) while (uploading the video to supabase storage): {e}")
        return []

# semple response
# https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//3825853e-be8b-40a0-a499-e4001ed4e949.mp4

