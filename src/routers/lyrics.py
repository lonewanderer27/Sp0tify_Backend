from fastapi import APIRouter, Depends, Query
from ..genius import genius
from typing import Union
from .utils import verify_id
from bs4 import BeautifulSoup as bs
from requests import get
from pprint import pprint
from ..string_utils import remove_punctuation, remove_extra_spaces, remove_apostrophe, replace_apostrophe, remove_zero_width_space, remove_right_to_left_mark, scrub_string, replace_br, keep_until, remove_until, until_embded, replace_br, keep_until, until_embded, remove_see_live_ad, remove_square_brackets

router = APIRouter(prefix="/lyrics", tags=["Lyrics"])


def clean_line(s: str):
    # s = remove_punctuation(s)
    s = remove_until(s, "Verse", True)
    if "verse" in s.lower():
        s = "["+s 
    s = replace_br(s)
    s = scrub_string(s)
    s = until_embded(s, True, False)
    s = remove_see_live_ad(s)
    return s


@router.get("/", description="If you pass a song ID, the method will have to make an extra request to obtain the song’s URL and scrape the lyrics off of it. So it’s best to pass the method the song’s URL if it’s available.")
async def search_lyrics(
    id: Union[int, None] = Query(None, description="Genius song ID"),
    song_url: Union[str, None] = Query(None, description="Song URL"),
    remove_section_headers: bool = Query(
        False, description="Remove section headers (e.g. [Chorus])"),
):
    res = genius.lyrics(id, song_url, remove_section_headers)
    if res:
        lyrics = res.split("\n")
        lyrics.pop(0) # remove first as it usually contains attributions
        cleaned_lyrics = list(map(clean_line, lyrics))
        return cleaned_lyrics
    else:
        return []

