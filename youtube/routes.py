from fastapi import APIRouter, Request
from youtube_transcript_api import YouTubeTranscriptApi

router = APIRouter()

@router.post('/get-transcript')
async def get_transcript(requet: Request):
    data = await requet.json()
    video_id = data['video_id']
    video_transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return {"message": f"Youtube video transcript for { video_id }", "transcript": video_transcript}