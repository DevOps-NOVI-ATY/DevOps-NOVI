from sqlalchemy import select
from ..models.dbFunctions import runSelectStatement
from ..models.models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover

    
def zoekKarakters():
    stmt = select(Karakter)
    return runSelectStatement(stmt)

def zoekStipboekBijKarakter(karakterNaam):
    stmt = select(Stripboek)\
        .join(Stripboek.karakters)\
        .where(Karakter.naam == karakterNaam)
    return runSelectStatement(stmt)

