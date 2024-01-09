from fastapi import APIRouter

#maak router aan voor endpoint karakter
router = APIRouter(prefix='/karakter')

#GET request naar root van endpoint karakter
@router.get('/')
async def root():
    return {"karakter":"Spiderman"}
