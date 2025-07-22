from env import HEYGEN_API_KEY
import requests
from sentry import sentry_sdk

def generate_video(script):
    try:
        url = 'https://api.heygen.com/v2/video/generate'
        api_key = HEYGEN_API_KEY

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

        headers = {
            'X-Api-Key': api_key,
            'Content-Type': 'application/json'
        }

        # response = requests.post(url, json=data, headers=headers)
        # response.raise_for_status()  # Raises an error for 4xx or 5xx

        # data = response.json()
        # video_id = data["data"]["video_id"]
        # return video_id
        return "1c449ce2268140e986ef94890e80ebd0"

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Error during (video_generation) while (sending video generation request to hey gen): {e}")
        return None

# print(generate_video("hello"))
# example response
# {'error': None, 'data': {'video_id': '1c449ce2268140e986ef94890e80ebd0'}}