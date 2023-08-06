from fastapi import APIRouter, HTTPException, Depends
from ..genius import genius
from pprint import pprint
from .utils import verify_query

router = APIRouter(prefix="/search", dependencies=[Depends(verify_query)])

@router.get("/")
async def search(q: str, per_page=None, page=None):
    res = genius.search_all(q, per_page, page)

    pprint(res, indent=2)
    return res

@router.get("/artists")
async def search_artists(q: str, per_page=None, page=None):
    res = genius.search_artists(q, per_page, page)

    pprint(res, indent=2)
    return res

@router.get("/songs")
async def search_songs(q: str, per_page=None, page=None):
    res = genius.search_songs(q, per_page, page)

    pprint(res, indent=2)
    return res

@router.get("/albums")
async def search_albums(q: str, per_page=None, page=None):
    res = genius.search_albums(q, per_page, page)

    pprint(res, indent=2)
    return res

@router.get("/lyrics")
async def search_lyrics(q: str, per_page=None, page=None):
    res = genius.search_lyrics(q, per_page, page)

    pprint(res, indent=2)
    return res

@router.get("/videos")
async def search_web(q: str, per_page=None, page=None):
    res = genius.search_videos(q, per_page, page)

    pprint(res, indent=2)
    return res
