from db import supabase
from sentry import sentry_sdk

def update_video_status_and_url(url, video_id):
    try:
        data = {
            "status": "completed",
            "url": url,
        }

        response = supabase.table("videos") \
            .update(data) \
            .eq("id", video_id) \
            .execute()

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Error during (video_generation) while (updating the video status and url): {e}")
        return []

# update_video_status_and_url("https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//3825853e-be8b-40a0-a499-e4001ed4e949.mp4", "3825853e-be8b-40a0-a499-e4001ed4e949" )
# sample response
# [{'id': '3825853e-be8b-40a0-a499-e4001ed4e949', 'video_idea': None, 'duration': None, 'script': 'Quick tips for daily productivity', 'music': None, 'thumbnail': None, 'hashtags': ['#productivity', '#tips', '#daily'], 'caption': 'Boost your productivity with these tips', 'status': 'completed', 'url': 'https://tuaaacbguivultdxbcmj.supabase.co/storage/v1/object/public/generated-videos//3825853e-be8b-40a0-a499-e4001ed4e949.mp4', 'created_at': '2025-07-21T04:29:49.578902+00:00', 'updated_at': '2025-07-21T04:29:49.578902+00:00'}]