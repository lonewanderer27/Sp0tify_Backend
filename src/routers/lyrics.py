from fastapi import APIRouter, Depends
from ..genius import genius
from .utils import verify_id

router = APIRouter(prefix="/lyrics")

@router.get("/{id}", dependencies=[Depends(verify_id)])
async def search_lyrics(id):
    res = genius.lyrics(id)
    return res