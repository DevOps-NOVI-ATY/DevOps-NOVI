from pydantic import BaseModel,ConfigDict
from datetime import date

class cover(BaseModel):
    type: str

class character(BaseModel):
    name: str

class publisher(BaseModel):
    name: str

class serie(BaseModel):
    size: int
    publisher: str
    name: str


class comic(BaseModel):
    name: str
    pages: int
    issue: int
    release: date
    price: float
    series: serie
    characters: character
    covers: cover




