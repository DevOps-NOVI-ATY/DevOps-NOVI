from fastapi import APIRouter, HTTPException
from ..models.models import series
from ..Database.functions import get_all, filtered_series, return_or_404
from ..schemas import schemas

#Create router for endpoint /series
router = APIRouter(prefix='/series')


#GET request to root of endpoint series
@router.get('/')
async def root() -> list[schemas.serie]:
    return return_or_404("series", result=get_all(series))


#GET request get series filtered by publisher
@router.get('/publisher/{publisher}')
async def filtered_series_by_publisher(publisher) -> list[schemas.serie]:

    return return_or_404("series", result=filtered_series(publisher))


#GET request get series filtered by size
@router.get('/size/{size}')
async def filtered_series_by_publisher(size) -> list[schemas.serie]:
    return return_or_404("series", result=filtered_series(size))
