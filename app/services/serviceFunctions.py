from sqlalchemy import select
from ..models.dbFunctions import runSelectStatement
from ..models.models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover



'''
-------------------------------------------------------------------
|                                                                  |
-------------------------------------------------------------------
'''
#zoekfuncties uitgevoerd door DB

#haal alle karakters op
def zoekKarakters():
    stmt = select(Karakter)
    return runSelectStatement(stmt)

#Haal alle stripboeken gefilterd op karakternaam op
def zoekStripboekBijKarakter(karakterNaam):
    stmt = (
        select(Stripboek.naam, Stripboek.issueNummer, Stripboek.Uitgavedatum, Stripboek.paginas, Stripboek.prijs)
        .join(Stripboek.karakters)
        .join(Stripboek.covers)
        .join(Stripboek.series)
        .distinct(Stripboek.naam, Stripboek.issueNummer, Stripboek.Uitgavedatum, Stripboek.paginas, Stripboek.prijs)
        .where(Karakter.naam == karakterNaam)
    )

    return runSelectStatement(stmt)

#Haal alle stripboeken gefilterd op karakternaam op en sorteer deze op uitgavedatum
def zoekStripVolgordeBijKarakter(karakterNaam):
    stmt = (select(Stripboek, Serie, Uitgever, Cover_soort)
        .join(Stripboek.karakters)
        .join(Stripboek.covers)
        .join(Stripboek.series)
        .distinct(Stripboek.naam, Stripboek.issueNummer, Stripboek.Uitgavedatum, Stripboek.paginas, Stripboek.prijs)
        .where(Karakter.naam == karakterNaam)
        .order_by(Stripboek.Uitgavedatum.asc())
    )
    return runSelectStatement(stmt)


#Haal alle series op
def zoekSeries():
    stmt = select(Serie)
    return runSelectStatement(stmt)


#Haal alle uitgevers op
def zoekUitgevers():
    stmt = select(Uitgever)
    return runSelectStatement(stmt)


'''
-------------------------------------------------------------------
|                                                                  |
-------------------------------------------------------------------
'''

#zoekfuncties uitgevoerd door Python
def zoekStripboekBijKarakter_Py(karakterNaam):
    
    # get alle karakters
    alle_karakters = zoekKarakters()

    #check of karakter bestaat
    check1 = False
    for i in alle_karakters:
       if i["Karakter"].naam == karakterNaam:
           check1 = True
    
    #als karakter niet bestaat geef error terug.
    if not check1:
        return "Karakter bestaat niet"
    
    #alle koppelingen tussen stripboek en karakter ophalen uit koppeltabel
    alle_stripkar = runSelectStatement(select(Strip_kar))

    #stripboeken filteren op karakter
    stripboek_filtered = []
    for j in alle_stripkar:
        if j["karakter"] ==  karakterNaam:
            stripboek_filtered.append(j["stripboek"])
    
    #get alle stripboeken
    alle_stripboeken = runSelectStatement(select(Stripboek))

    #filter resultaten op gefilterde stripboeken
    resultaat = []
    for k in alle_stripboeken:
        if k["Stripboek"].naam in stripboek_filtered:
            resultaat.append(k["Stripboek"].__dict__)

    #alle koppelingen tussen stripboek en coversoort/serie ophalen uit koppeltabel
    alle_stripcover = runSelectStatement(select(Strip_cover))
    alle_seriestrip = runSelectStatement(select(Serie_strip))

    #alle series ophalen
    alle_series = runSelectStatement(select(Serie))

    #coversoort, serie en uitgever toevoegen aan gefilterde stripboeken
    for l in resultaat:

        #filter coversoorten op stripboek en voeg toe
        for m in alle_stripcover:
            if m["stripboek"] == l["naam"]:
                l["cover"] = m["cover_soort"]
        
        #filter series op stripboek en voeg toe
        for n in alle_seriestrip:
            if n["stripboek"] == l["naam"]:
                l["serie"] = n["serie"]
        
        #filter uitgever op serie en voeg toe
        for o in alle_series:
            if o["Serie"].naam == l["serie"]:
                l["uitgever"] = o["Serie"].uitgever_naam
            
    #geef resultaten terug
    return resultaat


def zoekStripVolgordeBijKarakter_Py(karakterNaam):
    
    #haal alle stripboeken op
    resultaat = zoekStripboekBijKarakter_Py(karakterNaam)

    #sorteer stripboeken op uitgave datum
    gesorteerde_res = sorted(resultaat, key= lambda i: i["Uitgavedatum"])

    return gesorteerde_res



    


'''
-------------------------------------------------------------------
|                                                                  |
-------------------------------------------------------------------
'''