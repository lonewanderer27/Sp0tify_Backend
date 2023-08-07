from fastapi import APIRouter, Depends, Query
from ..genius import genius
from .utils import verify_id
from typing import Union

router = APIRouter(prefix="/song", tags=["Song"])


@router.get("/{id}", dependencies=[Depends(verify_id)])
async def search_song(id: int):
    res = genius.song(id)
    return res


@router.get("/{id}/activity")
async def activity_song(
    id: int,
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")):
    res = genius.song_activity(id, per_page, page)
    return res
