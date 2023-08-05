from fastapi import APIRouter
from genius import genius
from typing import Union, Literal

router = APIRouter()


@router.get("/leaderboard/")
async def get_leaderboard(time_period='day', per_page=None, page=None):
    res = genius.leaderboard(time_period, per_page, page)
    return res


@router.get("/charts")
async def get_charts(time_period='day', chart_genre='all', per_page=None, page=None, type_='songs'):
    res = genius.charts(time_period, chart_genre, per_page, page, type_)
    return res
