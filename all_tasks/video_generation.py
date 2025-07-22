from db import supabase
from env import HEYGEN_API_KEY
import requests
import time

def get_pending_videos():
    from celery_app import sentry_sdk
    try:
        response = supabase.table("videos") \
            .select("*") \
            .eq("status", "pending") \
            .execute()
        pending_ideas = response.data
        return pending_ideas
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Error fetching pending videos: {e}")
        return []

    
    
    #example response
#     [{'id': '3825853e-be8b-40a0-a499-e4001ed4e949', 'video_idea': None, 'duration': None, 'script': 'Quick tips for daily productivity', 'music': None, 'thumbnail': None, 'hashtags': ['#productivity', '#tips', '#daily'], 'caption': 'Boost your productivity with these tips', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}, {'id': 'bdea7541-ab1d-4833-863c-9dbba8bf94bd', 'video_idea': None, 'duration': None, 'script': 'How to cook easy meals fast', 'music': None, 'thumbnail': None, 'hashtags': ['#cooking', '#easymeals', '#quickrecipes'], 'caption': 'Simple and quick meal recipes', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}, {'id': 'bae37d49-6c0e-43e4-9b3e-46ac8997bee0', 'video_idea': None, 'duration': None, 'script': 'Best exercises for beginners', 'music': None, 'thumbnail': None, 'hashtags': ['#fitness', '#beginnerworkout', 
# '#health'], 'caption': 'Start your fitness journey today', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}]
# [{'id': '3825853e-be8b-40a0-a499-e4001ed4e949', 'video_idea': None, 'duration': None, 'script': 'Quick tips for daily productivity', 'music': None, 'thumbnail': None, 'hashtags': ['#productivity', '#tips', '#daily'], 'caption': 'Boost your productivity with these tips', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}, {'id': 'bdea7541-ab1d-4833-863c-9dbba8bf94bd', 'video_idea': None, 'duration': None, 'script': 'How to cook easy meals fast', 'music': None, 'thumbnail': None, 'hashtags': ['#cooking', '#easymeals', '#quickrecipes'], 'caption': 'Simple and quick meal recipes', 'status': 'pending', 'url': None, 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}, {'id': 'bae37d49-6c0e-43e4-9b3e-46ac8997bee0', 

def generate_video(script):
    url = 'https://api.heygen.com/v2/video/generate'
    api_key = HEYGEN_API_KEY

    # Build the JSON payload
    data = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": "e75bcfe5b4314c5aa7075aec29e09b13",
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": script,
                    "voice_id": "9526fc40f97d4d4db18cd8915497d952"
                },
                "background": {
                    "type": "color",
                    "value": "#008000"
                }
            }
        ],
        "dimension": {
            "width": 1280,
            "height": 720
        }
    }

    # Set the request headers
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json'
    }

    # Make the POST request
    response = requests.post(url, json=data, headers=headers)

    data = response.json()
    video_id = data["data"]["video_id"]
    return (video_id)

# print(generate_video("hello"))
# example response
# {'error': None, 'data': {'video_id': '1c449ce2268140e986ef94890e80ebd0'}}

def download_video(video_id, video_fileid):
    headers = {
        'X-Api-Key': HEYGEN_API_KEY
    }

    video_status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    while True:
        response = requests.get(video_status_url, headers=headers)
        status = response.json()["data"]["status"]

        if status == "completed":
            video_url = response.json()["data"]["video_url"]
            thumbnail_url = response.json()["data"]["thumbnail_url"]
            print(
                f"Video generation completed! \nVideo URL: {video_url} \nThumbnail URL: {thumbnail_url}"
            )

            # Save the video to a file
            video_filename = f"{video_fileid}.mp4"
            with open(video_filename, "wb") as video_file:
                video_content = requests.get(video_url).content
                video_file.write(video_content)
            break
            
        elif status == "processing" or status == "pending":
            print("Video is still processing. Checking status...")
            time.sleep(5)  # Sleep for 5 seconds before checking again
            
        elif status == "failed":
            error = response.json()["data"]["error"]
            print(f"Video generation failed. '{error}'")
            break
    return video_filename
# sample response
# 3825853e-be8b-40a0-a499-e4001ed4e949.mp4


def upload_video(file_name):
    with open(file_name, "rb") as f:
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

# semple response
# https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//3825853e-be8b-40a0-a499-e4001ed4e949.mp4


def update_video_status_and_url(url, video_id):
    data = {
        "status": "completed",
        "url": url,
    }

    response = supabase.table("videos") \
        .update(data) \
        .eq("id", video_id) \
        .execute()

    print(response.data)

# update_video_status_and_url("https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//3825853e-be8b-40a0-a499-e4001ed4e949.mp4", "3825853e-be8b-40a0-a499-e4001ed4e949" )

# sample response
# [{'id': '3825853e-be8b-40a0-a499-e4001ed4e949', 'video_idea': None, 'duration': None, 'script': 'Quick tips for daily productivity', 'music': None, 'thumbnail': None, 'hashtags': ['#productivity', '#tips', '#daily'], 'caption': 'Boost your productivity with these tips', 'status': 'completed', 'url': 'https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//3825853e-be8b-40a0-a499-e4001ed4e949.mp4', 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}]