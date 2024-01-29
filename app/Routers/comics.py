from fastapi import APIRouter, Request, HTTPException
from ..Models.models import comics
from ..Database.functions import get_all_comics, get_filtered_comics, return_or_404
from ..Schemas import schemas

#Create router for endpoint /comics
router = APIRouter(prefix='/comics')


#GET request to root of endpoint comics
@router.get('/')
async def root(req:Request) -> list[schemas.comic]:

    #convert query string to dict
    query = dict(req.query_params)

    #check if query string is used
    if query == {}:
        return return_or_404(resource="Comic books", result=get_all_comics())
    else:
        return return_or_404(resource="Comic books", result=get_filtered_comics(query))
