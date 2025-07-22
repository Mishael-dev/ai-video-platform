from db import supabase
from sentry import sentry_sdk

def get_pending_videos():
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
