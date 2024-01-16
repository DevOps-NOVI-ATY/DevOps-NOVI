from sqlalchemy import select
from ..models.dbFunctions import runSelectStatement
from ..models.models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover

    
'''
-------------------------------------------------------------------
|           Functies voor endpoint /stripboeken                   |
-------------------------------------------------------------------
'''

# Haal alle stripboeken op
def zoek_stripboeken():
    stmt = select(Uitgever, Serie, Stripboek, Karakter, Cover_soort)\
        .join(Stripboek.karakters)\
        .join(Stripboek.covers)\
        .join(Stripboek.series)\
    
    return runSelectStatement(stmt)

# Haal alle stripboeken gefilterd op querystring op
def zoek_stripboeken_query(query:dict):

    # haal alle stripboeken op
    alle_stripboeken = zoek_stripboeken()
    
    # list om alle gefilterde stripboeken op te slaan.
    stripboeken_gefilterd = []

    # over alle stripboeken itereren
    for stripboek in alle_stripboeken:
        
        check = True

        # controleer of eigenschappen van stripboek overeenkomen met filters
        for key, value in query.items():

            #verander + in spaties
            if "+" in value:
                value.replace("+", " ")
            

            if key == 'uitgever':
                #als eigenschap van stripboek niet overeenkomt, ga naar volgende stripboek
                if stripboek['Uitgever'].naam != value:
                    check = False
                    break

            elif key == 'serie':
                if stripboek['Serie'].naam != value:
                    check = False
                    break

            elif key == 'stripboek':
                if stripboek['Stripboek'].naam != value:
                    check = False
                    break

            elif key == 'karakter':
                if stripboek['Karakter'].naam != value:
                    check = False
                    break

            elif key == 'cover':
                if stripboek['Cover_soort'].naam != value:
                    check = False
                    break
                        

        # als stripboek overeenkomt, voeg deze dan toe aan de lijst.             
        if check:
            stripboeken_gefilterd.append(stripboek)

        
    # check of er stripboeken zijn 
    if len(stripboeken_gefilterd) > 0:

        #check of het op volgorde moet
        if "volgorde" in query:
            return sorted(stripboeken_gefilterd, key= lambda i: i["Stripboek"].Uitgavedatum)    
        
        return stripboeken_gefilterd
    else:
        return "Geen stripboeken gevonden"
    

'''
-------------------------------------------------------------------
|           Functies voor endpoint /karakters                     |
-------------------------------------------------------------------
'''
#haal alle karakters op
def zoekKarakters():
    stmt = select(Karakter)
    return runSelectStatement(stmt)

#Haal alle stripboeken gefilterd op karakternaam op
def zoekStripboekBijKarakter(karakterNaam):
    stmt = select(Uitgever, Serie, Stripboek, Karakter, Cover_soort)\
        .join(Stripboek.karakters)\
        .join(Stripboek.covers)\
        .join(Stripboek.series)\
        .where(Karakter.naam == karakterNaam)
    #print(stmt)
    return runSelectStatement(stmt)

#Haal alle stripboeken gefilterd op karakternaam op en sorteer deze op uitgavedatum
def zoekStripVolgordeBijKarakter(karakterNaam):
    stmt = select(Uitgever, Serie, Stripboek, Karakter, Cover_soort)\
        .join(Stripboek.karakters)\
        .join(Stripboek.covers)\
        .join(Stripboek.series)\
        .where(Karakter.naam == karakterNaam)\
        .order_by(Stripboek.Uitgavedatum.asc())
    #print(stmt)
    return runSelectStatement(stmt)

#Haal alle series waarin de karakter in voorkomt
def zoek_serie_bij_karakter(karakterNaam):
    stmt = select(Serie, Karakter)\
        .join(Stripboek.karakters)\
        .join(Stripboek.series)\
        .where(Karakter.naam == karakterNaam)
    
    return runSelectStatement(stmt)
'''
-------------------------------------------------------------------
|           Functies voor endpoint /series                        |
-------------------------------------------------------------------
'''
#Haal alle series op
def zoekSeries():
    stmt = select(Serie)
    return runSelectStatement(stmt)

#Haal alle stripboeken van een serie
def zoekStripboekBijSerie(serie_naam):

    stmt = select(Uitgever, Serie, Stripboek, Karakter, Cover_soort)\
        .join(Stripboek.karakters)\
        .join(Stripboek.covers)\
        .join(Stripboek.series)\
        .where(Serie.naam == serie_naam)
    
    return runSelectStatement(stmt) 
'''
-------------------------------------------------------------------
|           Functies voor endpoint /uitgevers                     |
-------------------------------------------------------------------
'''
#Haal alle uitgevers op
def zoekUitgevers():
    stmt = select(Uitgever)
    return runSelectStatement(stmt)

#Zoek alle series van een uitgever
def zoek_serie_bij_uitgever(uitgever_naam):
    stmt = select(Serie).where(Serie.uitgever_naam==uitgever_naam)
    return runSelectStatement(stmt)