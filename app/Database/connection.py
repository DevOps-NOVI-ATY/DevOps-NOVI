import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from ..Models.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import csv


#Get DB URL from environment variables. if not available, use sqlite
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user-name:strong-password@localhost:5433/api')


#Create connection engine
engine = create_engine(DATABASE_URL)

start_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Initialize database
def init_db():
    #Create database if it doesn't exist
    if not database_exists(engine.url):
        create_database(engine.url)


    #Create tables based on the models
    base.metadata.create_all(engine)

    #populate database
    csv_to_db("app/Database/dataset.csv")


#populate database with a csv file
def csv_to_db(csv_file):

    #open database connection
    db = start_session()

    #Open CSV file
    with open(csv_file) as file:

        #Skip the header
        heading = next(file)

        #convert file to reader object
        reader = csv.reader(file, delimiter="|")

        #lists of objects to reference later on
        publishers_list =[]
        series_list = []
        characters_list = []
        covers_list = []


        for row in reader:
            
            #add publisher to database if it doesn't exits
            
            if db.query(publishers).filter(publishers.name == row[0]).first() is None:
                publisher = publishers(name=row[0])
                #save publisher object
                publishers_list.append(publisher)
                db.add(publisher)


            

            #add serie to database if it doesn't exits
            if db.query(series).filter(series.name ==  row[1]).first() is None:
                #find publisher object for reference
                for pub in publishers_list:
                    if pub.name == row[0]:
                        serie = series(name=row[1], size=int(row[2]), publishers=pub)
                        series_list.append(serie)
                        db.add(serie)
                        break
                

            #add character to database if it doesn't exits
            if db.query(characters).filter(characters.name ==  row[8]).first() is None:
                character = characters(name=row[8])
                characters_list.append(character)
                db.add(character)


            #add cover to database if it doesn't exits
            if db.query(covers).filter(covers.type ==  row[9]).first() is None:
                cover = covers(type=row[9])
                covers_list.append(cover)
                db.add(cover)


            try:
                price = float(row[7])
            except ValueError:
                price = float(row[7][1:])


            #add comic to database if it doesn't exits
            if db.query(comics).filter(comics.name ==  row[3]).first() is None:
                #get series object
                for ser in series_list:
                    if ser.name == row[1]:
                        #get characters object
                        for char in characters_list:
                            if char.name == row[8]:
                                #get cover object
                                for cov in covers_list:
                                    if cov.type == row[9]:

                                        comic = comics(name=row[3], issue=int(row[4]), release=row[5], pages=int(row[6]), price=price)
                                        comic.series.append(ser)
                                        comic.characters.append(char)
                                        comic.covers.append(cov)
                                        db.add(comic)
                                        break
                                break
                        break
            
            #commit changes
            db.commit()
            
    
    #close database connection
    db.close()





            
            







