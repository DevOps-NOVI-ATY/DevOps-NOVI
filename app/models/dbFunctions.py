from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


def startSession(engine):
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try: 
        session = Session()
        return session
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

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

    resultObjects = []
    for result in session.scalars(statement):
        resultObjects.append(result)

    closeSession(session)

    return resultObjects

def runInsertStatement(insertableObject):
    session = startSession()

    session.add(insertableObject)

    commitAndCloseSession(session)
