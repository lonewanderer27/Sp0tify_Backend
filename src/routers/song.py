from fastapi import APIRouter, Depends
from ..genius import genius
from .utils import verify_id

router = APIRouter(prefix="/song")

@router.get("/{id}", dependencies=[Depends(verify_id)])
async def search_song(id):
    res = genius.song(id)
    return res

@router.get("/{id}/activity")
async def activity_song(id, per_page=None, page=None):
    res = genius.song_activity(id, per_page, page)
    return res