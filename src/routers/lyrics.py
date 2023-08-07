from fastapi import APIRouter, Depends
from ..genius import genius
from .utils import verify_id

router = APIRouter(prefix="/lyrics", tags=["Lyrics"])

@router.get("/{id}", dependencies=[Depends(verify_id)])
async def search_lyrics(id: int):
    res = genius.lyrics(id)
    return res