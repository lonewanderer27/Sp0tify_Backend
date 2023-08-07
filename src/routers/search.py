from fastapi import APIRouter, Depends, Query
from typing import Annotated, Union
from ..genius import genius
from pprint import pprint
from .utils import verify_query

router = APIRouter(prefix="/search", dependencies=[Depends(verify_query)], tags=["Search"])


@router.get("/multi")
async def search_all(
    q=Query(description="A term to search"),
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)"),
):
    res = genius.search_all(q, per_page, page)

    pprint(res, indent=2)
    return res


@router.get("/artists")
async def search_artists(
    q=Query(description="A term to search"),
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)"),
):
    res = genius.search_artists(q, per_page, page)

    pprint(res, indent=2)
    return res


@router.get("/songs")
async def search_songs(
    q=Query(description="A term to search"),
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)"),
):
    res = genius.search_songs(q, per_page, page)

    pprint(res, indent=2)
    return res


@router.get("/albums")
async def search_albums(
    q=Query(description="A term to search"),
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)"),
):
    res = genius.search_albums(q, per_page, page)

    pprint(res, indent=2)
    return res


@router.get("/lyrics")
async def search_lyrics(
    q=Query(description="A term to search"),
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)"),
):
    res = genius.search_lyrics(q, per_page, page)

    pprint(res, indent=2)
    return res


@router.get("/videos")
async def search_web(
    q=Query(description="A term to search"),
    per_page: Union[str, None] = Query(None,
                                       description="Number of results to return per page"),
    page: Union[str, None] = Query(
        None, description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)"),
):
    res = genius.search_videos(q, per_page, page)

    pprint(res, indent=2)
    return res
