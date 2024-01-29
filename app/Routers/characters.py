from fastapi import APIRouter
from ..Models.models import characters
from ..Database.functions import get_all, return_or_404
from ..Schemas import schemas

#Create router for endpoint /characters
router = APIRouter(prefix='/characters')


#GET request to root of endpoint characters
@router.get('/')
async def root() -> list[schemas.character]:
    return return_or_404(resource="Characters", result=get_all(characters))

