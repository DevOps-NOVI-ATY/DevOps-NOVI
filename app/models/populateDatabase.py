from .models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover
from .dbFunctions import startSession, commitAndCloseSession, runSelectStatement
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
import csv

def populateDatabase(engine):
    session = startSession()
    # 1. Add records to the Uitgever table
    marvel = Uitgever(naam='Marvel Comics')
    session.add(marvel)

    # 2. Add records to the Serie table
    spiderman5min = Serie(naam='5 Minute Spider-Man Stories HC', serieGrootte=1, uitgever=marvel)
    session.add(spiderman5min)

    spidermanADV = Serie(naam='The Adventures of Spider-Man', serieGrootte=14, uitgever=marvel)
    session.add(spidermanADV)

    spidermanHulk = Serie(naam='Amazing Spider-Man Dallas Times Herald Giveaway', serieGrootte=5, uitgever=marvel)
    session.add(spidermanHulk)

    # 3. Add records to the Karakter table
    spiderman = Karakter(naam='spiderman')
    session.add(spiderman)
    
    hulk = Karakter(naam='hulk')
    session.add(hulk)

    # 4. Add records to the Cover_soort table
    hardCover = Cover_soort(naam='hardCover')
    session.add(hardCover)

    softCover = Cover_soort(naam='softCover')
    session.add(softCover)


    # 5. Add records to the Stripboek table
    spiderman5MinStrip = Stripboek(naam='5 Minute Spider-Man Stories HC', issueNummer=1, Uitgavedatum='2017-06-21', paginas=192, prijs=12.99)
    spiderman5MinStrip.series.append(spiderman5min)  # Link the stripboek to the serie
    spiderman5MinStrip.karakters.append(spiderman)
    spiderman5MinStrip.covers.append(hardCover)
    session.add(spiderman5MinStrip)

    spidermanStrip1 = Stripboek(naam='The Adventures of Spider-Man #1', issueNummer=1, Uitgavedatum='1996-04-03', paginas=36, prijs=.99)
    spidermanStrip1.series.append(spidermanADV)  # Link the stripboek to the serie
    spidermanStrip1.karakters.append(spiderman)
    spidermanStrip1.covers.append(softCover)
    session.add(spidermanStrip1)

    spidermanStrip2 = Stripboek(naam='The Adventures of Spider-Man #2', issueNummer=1, Uitgavedatum='1996-04-03', paginas=36, prijs=.99)
    spidermanStrip2.series.append(spidermanADV)  # Link the stripboek to the serie]
    spidermanStrip2.karakters.append(spiderman)
    spidermanStrip2.covers.append(softCover)
    session.add(spidermanStrip2)

    spidermanStrip3 = Stripboek(naam='The Adventures of Spider-Man #3', issueNummer=1, Uitgavedatum='1996-04-03', paginas=36, prijs=.99)
    spidermanStrip3.series.append(spidermanADV)  # Link the stripboek to the serie
    spidermanStrip3.karakters.append(spiderman)
    spidermanStrip3.covers.append(softCover)
    session.add(spidermanStrip3)

    spidermanHulkStrip1 = Stripboek(naam='Amazing Spider-Man Dallas Times Herald Giveaway #1', issueNummer=1, Uitgavedatum='1981-08-05', paginas=32, prijs=0)
    spidermanHulkStrip1.series.append(spidermanHulk)  # Link the stripboek to the serie
    spidermanHulkStrip1.karakters.append(spiderman)
    spidermanHulkStrip1.karakters.append(hulk)
    spidermanHulkStrip1.covers.append(softCover)
    session.add(spidermanHulkStrip1)

    spidermanHulkStrip2 = Stripboek(naam='Amazing Spider-Man Dallas Times Herald Giveaway #2', issueNummer=1, Uitgavedatum='1982-06-02', paginas=32, prijs=0)
    spidermanHulkStrip2.series.append(spidermanHulk)  # Link the stripboek to the serie
    spidermanHulkStrip2.karakters.append(spiderman)
    spidermanHulkStrip2.karakters.append(hulk)
    spidermanHulkStrip2.covers.append(softCover)
    session.add(spidermanHulkStrip2)

    # Commit the changes to the database
    commitAndCloseSession(session)

'''
-------------------------------------------------------------------
|                                                                  |
-------------------------------------------------------------------
'''
#populate DB door csv file dat gegenereerd is door chatgpt
#CSV format: uitgever|serienaam|seriegrootte|Stripboeknaam|issuenummer|uitgavedatum|paginas|prijs|karakternaam|coversoort

def csv_to_db(csv_file):

    # database connectie openen
    session = startSession()

    #csv bestand openen
    with open(csv_file) as file:

        #De header overslaan
        heading = next(file)

        #bestand omzetten naar een lees object om vervolgens te itereren
        reader = csv.reader(file, delimiter="|")

        #lijsten om objecten te onthouden, voor latere referenties
        uitgever_list = []
        serie_list = []
        karakter_list = []
        cover_list = []

        #database aanvullen met elke rij uit csv bestand
        for row in reader:


            #vul database aan als uitgever niet voorkomt
            if runSelectStatement(select(Uitgever).where(Uitgever.naam == row[0])) == []:
                uitgever =  Uitgever(naam=row[0])
                #onthoudt uitgever object
                uitgever_list.append(uitgever)
                session.add(uitgever)

            
            
            #vul database aan als serie niet voorkomt
            if runSelectStatement(select(Serie).where(Serie.naam == row[1])) == []:
                #zoek uitgever object op om vervolgens te linken met serie.
                for uitg in uitgever_list:
                    if uitg.naam == row[0]:
                        serie = Serie(naam=row[1], serieGrootte=int(row[2]), uitgever=uitg)
                        break
                #onthoudt serie object
                serie_list.append(serie)
                session.add(serie)


            
            #vul database aan als karakter niet voorkomt
            if runSelectStatement(select(Karakter).where(Karakter.naam == row[8])) == []:
                karakter = Karakter(naam=row[8])
                #onthoudt karakter object
                karakter_list.append(karakter)
                session.add(karakter)

            
            
            #vul database aan als cover niet voorkomt
            if runSelectStatement(select(Cover_soort).where(Cover_soort.naam == row[9])) == []:
                cover = Cover_soort(naam=row[9])
                #onthoudt cover object
                cover_list.append(cover)
                session.add(cover)


            # zet prijs om in float. als er value error ontstaat, haal dan prefix weg.
            try:
                prijs = float(row[7])
            except ValueError:
                prijs = float(row[7][1:])
            

            ##vul database aan als stripboek niet voorkomt
            if runSelectStatement(select(Stripboek).where(Stripboek.naam == row[3])) == []:
                
                #haal serie object op
                serie_obj
                for ser in serie_list:
                    if ser.naam == row[1]:
                        serie_obj = ser
                
                #haal karakter object op
                karakter_obj
                for kar in karakter_list:
                    if kar.naam == row[8]:
                        karakter_obj = kar
                
                #haal cover object op
                cover_obj
                for cov in cover_list:
                    if cov.naam == row[9]:
                        cover_obj = cov

                
                stripboek = Stripboek(naam=row[3], issueNummer=int(row[4]), Uitgavedatum=row[5], paginas=int(row[6]), prijs=prijs)
                stripboek.series.append(serie_obj)
                stripboek.karakters.append(karakter_obj)
                stripboek.covers.append(cover_obj)
                session.add(stripboek)
            
            
            # commit database aanvullingen, maar sluit connectie nog niet
            try:
                session.commit()
            except SQLAlchemyError as e:
                print(f"An error occurred: {e}")


    # sluit db connectie
    session.close()

'''
-------------------------------------------------------------------
|                                                                  |
-------------------------------------------------------------------
'''