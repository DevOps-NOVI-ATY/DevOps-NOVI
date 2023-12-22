from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy_utils import database_exists, create_database
from app.models.models import Base


#Haal db url uit environment variable. Deze is ingesteld in docker-compose.yml
SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

#Maak een connection engine aan
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Controle op db. als het niet bestaat, maakt het de db aan.
if not database_exists(engine.url):
    create_database(engine.url)

#maak de tabellen aan die gedefinieerd zijn in models.py
Base.metadata.create_all(engine)
