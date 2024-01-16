from fastapi import FastAPI
from app.routers import karakter, serie, uitgever, stripboeken
import app.database

app = FastAPI()

#Voeg routers toe
app.include_router(karakter.router)
app.include_router(serie.router)
app.include_router(uitgever.router)
app.include_router(stripboeken.router)

#GET request naar root endpoint.
@app.get("/")
async def root():
    return "NOVI - Comic books API"

