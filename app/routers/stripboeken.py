from fastapi import APIRouter, Request
from ..services import serviceFunctions

#maak router aan voor endpoint karakter
router = APIRouter(prefix='/stripboeken')

#GET request naar root van endpoint karakter
@router.get('/')
async def root(request:Request):

    #zet query string om naar dict
    query = dict(request.query_params)

    #Geef alle stripboeken, wanneer er geen querystring is gegeven.
    if query == {}:
        return serviceFunctions.zoek_stripboeken()
    else:
        return serviceFunctions.zoek_stripboeken_query(query)