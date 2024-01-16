from fastapi import APIRouter
from ..services import serviceFunctions

#maak router aan voor endpoint serie
router = APIRouter(prefix='/serie')

#GET request naar root van endpoint serie
@router.get('/')
async def root():
    return serviceFunctions.zoekSeries()

#GET request naar zoekStrip van endpoint serie met een serienaam in path
@router.get("/zoekstrip/{serie_naam}")
async def zoekStripsBijSerie(serie_naam):
    return serviceFunctions.zoekStripboekBijSerie(serie_naam)

#GET request naar zoekKarakter van endpoint serie met een serienaam in path


#GET request naar zoekUitgever van endpoint serie met een serienaam in path

