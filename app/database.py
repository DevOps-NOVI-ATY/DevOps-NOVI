from sqlalchemy_utils import database_exists, create_database
from app.models.models import Base
#Haal db url uit environment variable. Deze is ingesteld in docker-compose.yml
import os


SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user-name:strong-password@localhost:5433/api')

#Maak een connection engine aan
from sqlalchemy import create_engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Controle op db. als het niet bestaat, maakt het de db aan.
from app.models.populateDatabase import csv_to_db


if not database_exists(engine.url):
    create_database(engine.url)
    
#maak de tabellen aan die gedefinieerd zijn in models.py
Base.metadata.create_all(engine)

#database hardcoded aanvullen
#populateDatabase(engine) 

#database aanvullen met csv file
csv_to_db("app/models/dataset.csv")

