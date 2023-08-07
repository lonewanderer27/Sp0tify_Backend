from fastapi import APIRouter, Query
from typing import Union, Literal, Annotated, Union
from ..genius import genius

router = APIRouter()


@router.get("/charts", description="Gets the Genius charts.", tags=["Genius Charts"])
async def get_charts(
        time_period: Literal['day', 'week', 'month', 'all_time'] = Query(
            'day', description="Time period of the results"),
        chart_genre: Literal['all', 'rap', 'pop', 'rb', 'rock', 'country'] = Query(
            'all', description="The genre of the results."),
        per_page: Annotated[Union[int, None], Query(
        description="Number of results to return per page. It can’t be more than 50.", le=50, ge=0)] = None,
        page: Annotated[Union[int, None], Query(
            description="Paginated offset (e.g., per_page=5&page=3 returns songs 11-15)")] = None,
        type_: Literal['songs', 'albums', 'artists'] = Query(
            'songs', description="Type of chart to get")
):
    res = genius.charts(time_period, chart_genre, per_page, page, type_)
    return res
