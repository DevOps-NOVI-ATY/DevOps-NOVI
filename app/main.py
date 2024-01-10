from fastapi import FastAPI
from app.routers import karakter
from app.database import createDB

createDB()
app = FastAPI()

#Voeg router van endpoint karakter toe
app.include_router(karakter.router)

#GET request naar root endpoint.
@app.get("/")
async def root():
    return {"greeting":"Hello world this is the new file"}

