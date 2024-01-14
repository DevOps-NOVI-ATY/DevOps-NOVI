from fastapi import APIRouter
from ..services import serviceFunctions

#maak router aan voor endpoint uitgever
router = APIRouter(prefix='/uitgever')

#GET request naar root van endpoint uitgever
@router.get('/')
async def root():
    return serviceFunctions.zoekUitgevers()


#GET request naar zoekSerie van endpoint uitgever met uitgevernaam in path
@router.get('/zoekserie/{uitgever_naam}')
async def zoek_serie_bij_uitgever(uitgever_naam):
    return serviceFunctions.zoek_serie_bij_uitgever(uitgever_naam)



