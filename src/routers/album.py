from fastapi import APIRouter, Depends, Query
from ..genius import genius
from .utils import verify_id
from typing import Union, Annotated

router = APIRouter(
    prefix="/album", tags=["Album"], dependencies=[Depends(verify_id)])


@router.get("/{id}", description="Gets data for a specific album.")
async def album(id: int):
    res = genius.album(id)
    return res


@router.get("/{id}/cover_arts", description="Gets cover arts of a specific album.")
async def album_cover_arts(id: int):
    res = genius.album_cover_arts(id)
    return res


@router.get("/{id}/tracks", description="Gets tracks of a specific album.")
async def album_tracks(
    id: int,
    per_page: Annotated[int | None, Query(
        description="Number of results to return per page", le=50, ge=0)] = None,
    page: Union[int, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")):
    res = genius.album_tracks(id, per_page, page)
    return res
