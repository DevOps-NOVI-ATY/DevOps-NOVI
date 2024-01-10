from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

def startSession():
    from ..database import engine
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try: 
        session = Session()
        return session
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

def commitAndCloseSession(session):
    try: 
        session.commit()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def closeSession(session):
    try: 
        session.close()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

def runSelectStatement(statement):
    session = startSession()

    result_objects  = session.execute(statement).fetchall()

    # Use SQLAlchemy's built-in to_dict() method to convert the objects to dictionaries
    result_dicts = [row._asdict() for row in result_objects]
    
    closeSession(session)

    return result_dicts

def runInsertStatement(insertableObject):
    session = startSession()

    session.add(insertableObject)

    commitAndCloseSession(session)
