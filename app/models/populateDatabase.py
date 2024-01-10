from .models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover
from .dbFunctions import startSession, commitAndCloseSession


def populateDatabase(engine):
    session = startSession(engine)
    print('JAAAAAAAAAAAAAAAAAAA')
    print(session)
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
