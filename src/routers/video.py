from fastapi import APIRouter, Depends
from .utils import verify_id
from ..genius import genius

router = APIRouter(tags=["Video"])


@router.get("/video", dependencies=[Depends(verify_id)])
async def search_video(id: int):
    res = genius.video(id)
    return res


@router.get("/videos")
async def search_videos(album_id=None, article_id=None, song_id=None, video_id=None, per_page=None, page=None, series=False):
    res = genius.videos(album_id, article_id, song_id,
                        video_id, per_page, page, series)
    return res
