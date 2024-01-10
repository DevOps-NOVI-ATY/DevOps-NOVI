from sqlalchemy import select
from ..models.dbFunctions import runSelectStatement
from ..models.models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover

    
def zoekKarakters():
    stmt = select(Karakter)
    return runSelectStatement(stmt)

def zoekStipboekBijKarakter(karakterNaam):
    stmt = select(Stripboek, Serie, Uitgever, Cover_soort)\
        .join(Stripboek.karakters)\
        .join(Stripboek.covers)\
        .join(Stripboek.series)\
        .where(Karakter.naam == karakterNaam)
    #print(stmt)
    return runSelectStatement(stmt)

