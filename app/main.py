from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import ResponseValidationError
from .database.connection import init_db
from .routers.characters import router as char_router
from .routers.comics import router as comics_router
from .routers.publishers import router as pub_router
from .routers.series import router as series_router


init_db()

app = FastAPI()

app.include_router(char_router)
app.include_router(comics_router)
app.include_router(pub_router)
app.include_router(series_router)


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    raise HTTPException(status_code=500, detail="Response validation error") 

#GET request to root endpoint
@app.get("/")
async def root():
    return "Dit is de demo update"