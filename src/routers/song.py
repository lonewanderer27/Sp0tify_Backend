from fastapi import APIRouter, Depends, Query
from ..genius import genius
from .utils import verify_id
from typing import Union, Annotated

router = APIRouter(prefix="/song", tags=["Song"])


@router.get("/{id}", dependencies=[Depends(verify_id)])
async def search_song(id: int):
    res = genius.song(id)
    return res


@router.get("/{id}/activity")
async def activity_song(
    id: int,
    per_page: Annotated[int | None, Query(
        description="Number of results to return per page", le=50, ge=0)] = None,
    page: Union[int, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")):
    res = genius.song_activity(id, per_page, page)
    return res
