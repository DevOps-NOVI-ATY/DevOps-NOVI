from fastapi import FastAPI
from app.routers import karakter

app = FastAPI()

#Voeg de routers toe.
app.include_router(karakter.router)

#GET request naar root endpoint.
@app.get("/")
async def root():
    return {"greeting":"Hello world"}


import app.database


