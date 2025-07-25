from fastapi import FastAPI
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from tasks import run_video_generation

app = FastAPI()

@app.post("/generate-video")
def generate_video(video_data: dict):
    video_record = video_data["record"]
    task = run_video_generation.delay(video_record)
    return {"message": f"video generation task started with ID: {task.id}"}