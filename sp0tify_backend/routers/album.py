from fastapi import APIRouter, Depends
from genius import genius
from .utils import verify_query

router = APIRouter(prefix="/album")

@router.get("/", dependencies=[Depends(verify_query)])
async def search_album(album_id: str):
    res = genius.album(album_id)
    return res