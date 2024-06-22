from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import charts, search, song, album, lyrics, video, artist
import uvicorn
import os


sp0tify = FastAPI(title="Sp0tify LG",
                  description="Sp0tify LG wraps LyricsGenius into a REST-API that allows you to get information about songs, artists, albums, lyrics, videos, and charts.",
                  version="1.0.0")

sp0tify.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

sp0tify.include_router(search.router)
sp0tify.include_router(song.router)
sp0tify.include_router(artist.router)
sp0tify.include_router(album.router)
sp0tify.include_router(lyrics.router)
sp0tify.include_router(video.router)
sp0tify.include_router(charts.router)


@sp0tify.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(sp0tify, host="0.0.0.0", port=int(
        os.environ.get("PORT", 8000)))
