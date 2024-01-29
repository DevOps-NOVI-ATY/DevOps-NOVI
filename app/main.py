from fastapi import FastAPI
from .Database.connection import init_db
from .Routers.characters import router as char_router
from .Routers.comics import router as comics_router
from .Routers.publishers import router as pub_router
from .Routers.series import router as series_router


init_db()

app = FastAPI()

app.include_router(char_router)
app.include_router(comics_router)
app.include_router(pub_router)
app.include_router(series_router)

#GET request to root endpoint
@app.get("/")
async def root():
    return "NOVI - Comic books API"