from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///../HistoriaClinica.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
innerSession = Session()

def recreateTables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def getSession():
    return innerSession

if __name__ == '__main__':
    recreateTables()