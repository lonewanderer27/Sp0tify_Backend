from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import charts, search, song, album, lyrics, video, artist
import uvicorn
import os

sp0tify = FastAPI(title="Sp0tify API")

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


@sp0tify.get("/")
async def root():
    return {"message": "Sp0tify API"}

if __name__ == "__main__":
    uvicorn.run(sp0tify, host="0.0.0.0", port=int(
        os.environ.get("PORT", 8000)))
