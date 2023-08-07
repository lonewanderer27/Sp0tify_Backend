from fastapi import APIRouter, Depends, Query
from ..genius import genius
from .utils import verify_id
from typing import Union, Literal, Annotated

router = APIRouter(
    prefix="/artist", tags=["Artist"], dependencies=[Depends(verify_id)])


@router.get("/{id}", description="Gets data for a specific artist.")
async def artist(id: int):
    res = genius.artist(id)
    return res


@router.get("/{id}/songs", description="Gets artist’s songs.")
async def artist_songs(
    id,
    sort: Union[str, Literal['title']] = Query(
        'title', description="Sorting preference. Either based on ‘title’, ‘popularity’ or ‘release_date’."),
    per_page: Annotated[Union[int, None], Query(
        description="Number of results to return per page", le=50, ge=0)] = None,
    page: Annotated[Union[int, None], Query(
            description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None):
    res = genius.artist_songs(id, per_page, page, sort)
    return res


@router.get("/{id}/songs/search", description="Searches artist’s songs.")
async def search_artist_songs(
    id,
    q=Query(description="A term to search"),
    sort: Union[str, Literal['title']] = Query(
        'title', description=" Sorting preference. Either based on ‘title’, ‘popularity’ or ‘release_date’."),
    per_page: Annotated[Union[int, None], Query(
        description="Number of results to return per page", le=50, ge=0)] = None,
    page: Annotated[Union[int, None], Query(
            description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None):
    res = genius.search_artist_songs(id, q, per_page, page, sort)
    return res


@router.get("/{id}/albums", description="Gets artist’s albums.")
async def artist_albums(
    id,
    per_page: Annotated[Union[int, None], Query(
        description="Number of results to return per page", le=50, ge=0)] = None,
    page: Annotated[Union[int, None], Query(
            description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None):
    res = genius.artist_songs(id, per_page, page)
    return res
