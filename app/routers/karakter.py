from fastapi import APIRouter

# endpoint karakter maken
router = APIRouter(prefix='/karakter')

# root van endpoint karakter
@router.get('/')
async def root():
    return {"karakter":"Spiderman"}

    
