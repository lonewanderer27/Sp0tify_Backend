from fastapi import APIRouter, Depends, Query
from ..genius import genius
from .utils import verify_id
from typing import Union, Annotated
from src.models.song import Model

router = APIRouter(prefix="/song", tags=["Song"], dependencies=[Depends(verify_id)])


@router.get("/{id}", description="Gets data for a specific song.", response_model=Model)
async def search_song(id: int):
    res = genius.song(id)
    return res


@router.get("/{id}/activity", description="Gets activities on a song.")
async def activity_song(
    id: int,
    per_page: Annotated[Union[int, None], Query(
        description="Number of results to return per page. It can’t be more than 50.", le=50, ge=0)] = None,
    page: Annotated[Union[int, None], Query(
            description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None
):
    res = genius.song_activity(id, per_page, page)
    return res


@router.get("/{id}/annotations", description="Return song’s annotations with associated fragment in list of tuple.")
async def annotations_song(id: int):
    res = genius.song_annotations(id)
    return res


@router.get("/{id}/comments", description="Gets the comments on a song.")
async def comments_song(
    id: int,
    per_page: Annotated[Union[int, None], Query(
        description="Number of results to return per page. It can’t be more than 50.", le=50, ge=0)] = None,
    page: Annotated[Union[int, None], Query(
        description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None,
):
    res = genius.song_comments(id, per_page, page)
    return res