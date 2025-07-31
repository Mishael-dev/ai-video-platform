import requests
from env import HEYGEN_API_KEY
import time
from sentry import sentry_sdk
import os

os.makedirs("videos", exist_ok=True) 

def download_video(video_id, video_fileid):
    headers = {
        "X-Api-Key": HEYGEN_API_KEY
    }

    video_status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    video_filename = f"{video_fileid}.mp4"
    video_filepath = os.path.join("videos", video_filename)

    try:
        while True:
            response = requests.get(video_status_url, headers=headers)
            data = response.json().get("data", {})

            status = data.get("status")
            if not status:
                print("Unexpected API response format.")
                break

            if status == "completed":
                video_url = data.get("video_url")
                thumbnail_url = data.get("thumbnail_url")
                print(
                    f"Video generation completed! \nVideo URL: {video_url} \nThumbnail URL: {thumbnail_url}"
                )

                video_content = requests.get(video_url).content
                with open(video_filepath, "wb") as f:
                    f.write(video_content)
                return video_filename

            elif status in {"processing", "pending"}:
                print("Video is still processing. Checking again in 5s...")
                time.sleep(5)
                continue

            elif status == "failed":
                error = data.get("error", "Unknown error")
                print(f"Video generation failed: {error}")
                break

            else:
                print(f"Unknown status: {status}")
                break

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Error during (video_generation) while (downloading video from hey gen): {e}")
        return None

# sample response
# 3825853e-be8b-40a0-a499-e4001ed4e949.mp4
