from fastapi import APIRouter
from ..models.models import publishers
from ..database.functions import get_all, return_or_404
from ..schemas import schemas

#Create router for endpoint /publishers
router = APIRouter(prefix='/publishers')


#GET request to root of endpoint publishers
@router.get('/')
async def root() -> list[schemas.publisher]:
    return return_or_404(resource="Publishers", result=get_all(publishers))