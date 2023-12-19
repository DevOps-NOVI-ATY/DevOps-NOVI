from fastapi import FastAPI
from models import Base
from database import engine

app = FastAPI()

#configureer alle tabellen in db
Base.metadata.create_all(engine)

#GET request naar root endpoint.
@app.get("/")
async def root():
    return {"greeting":"Hello world"}


