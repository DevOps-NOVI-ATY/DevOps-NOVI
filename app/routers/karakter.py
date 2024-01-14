from fastapi import APIRouter
from ..services import serviceFunctions

#maak router aan voor endpoint karakter
router = APIRouter(prefix='/karakter')

#GET request naar root van endpoint karakter
@router.get('/')
async def root():
    return serviceFunctions.zoekKarakters()

#GET request naar zoekStrip van endpoint karakter met een karakternaam in path
@router.get("/zoekstrip/{karakterNaam}")
async def zoekStripsBijKarakter(karakterNaam):
    return serviceFunctions.zoekStripboekBijKarakter_Py(karakterNaam)

#GET request naar zoekstripvolgorde van endpoint karakter met een karakternaam in path
@router.get("/zoekstripvolgorde/{karakterNaam}")
async def zoekStripVolgordeBijKarakter(karakterNaam):
    return serviceFunctions.zoekStripVolgordeBijKarakter_Py(karakterNaam)

#GET request naar zoekSerie van endpoint karakter met een karakternaam in path

