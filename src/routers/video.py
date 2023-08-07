from fastapi import APIRouter, Depends, Query
from .utils import verify_id
from ..genius import genius
from typing import Annotated, Union, Optional

router = APIRouter(tags=["Video"])


@router.get("/video", dependencies=[Depends(verify_id)])
async def search_video(id: int):
    res = genius.video(id)
    return res


@router.get("/videos")
async def search_videos(
        album_id=None, article_id=None, song_id=None, video_id=None,
        per_page: Annotated[Union[int, None], Query(
            description="Number of results to return per page", le=50, ge=0)] = None,
        page: Annotated[Union[int, None], Query(
            description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None,
        series: Annotated[bool, Query(
            description="Whether to return videos in a series")] = False
):
    res = genius.videos(album_id, article_id, song_id,
                        video_id, per_page, page, series)
    return res
