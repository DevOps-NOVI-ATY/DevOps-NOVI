from main import app
from typing import Annotated
from fastapi import Path, Query

@app.get("/karakter")
async def root():
    return {"karakter":"Spiderman"}

@app.get("/karakter/{karakter_naam}")
async def zoek_karakter( karakter_naam: str | None = None):

    if karakter_naam:
        return {"karakter": karakter_naam}
