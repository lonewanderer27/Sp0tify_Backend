from fastapi import FastAPI, Request, HTTPException
from routers import search, song, album, lyrics, video, leaderboard

sp0tify = FastAPI()

sp0tify.include_router(search.router)
sp0tify.include_router(song.router)
sp0tify.include_router(album.router)
sp0tify.include_router(lyrics.router)
sp0tify.include_router(video.router)
sp0tify.include_router(leaderboard.router)

@sp0tify.get("/")
async def root():
    return {"message": "Sp0tify API"}
