from .models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover
from sqlalchemy.orm import sessionmaker


def populateDatabase(engine):
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    # 1. Add records to the Uitgever table
    uitgever1 = Uitgever(naam='Uitgever1')
    session.add(uitgever1)

    # 2. Add records to the Serie table
    serie1 = Serie(naam='Serie1', serieGrootte=10, uitgever=uitgever1)
    session.add(serie1)

    # 3. Add records to the Stripboek table
    stripboek1 = Stripboek(naam='Stripboek1', issueNummer=1, Uitgavedatum='2022-01-01', paginas=100, prijs=19.99)
    stripboek1.series.append(serie1)  # Link the stripboek to the serie
    session.add(stripboek1)

    # 4. Add records to the Karakter table
    karakter1 = Karakter(naam='Karakter1')
    session.add(karakter1)
    # 4. Add records to the Karakter table
    karakter2 = Karakter(naam='Karakter12')
    session.add(karakter2)
    # 4. Add records to the Karakter table
    karakter3 = Karakter(naam='Karakter123')
    session.add(karakter3)

    # 5. Add records to the Cover_soort table
    cover_soort1 = Cover_soort(naam='CoverSoort1')
    session.add(cover_soort1)

    # Commit the changes to the database
    session.commit()

    # Query the database to verify the records have been added
    uitgever_query = session.query(Uitgever).first()
    print("Uitgever:", uitgever_query.naam)

    serie_query = session.query(Serie).first()
    print("Serie:", serie_query.naam)

    stripboek_query = session.query(Stripboek).first()
    print("Stripboek:", stripboek_query.naam)

    karakter_query = session.query(Karakter).first()
    print("Karakter:", karakter_query.naam)

    cover_soort_query = session.query(Cover_soort).first()
    print("Cover Soort:", cover_soort_query.naam)