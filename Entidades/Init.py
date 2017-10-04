from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///HistoriaClinica.db', echo=True)
Base = declarative_base()
# Session = sessionmaker(bind = engine)

def recreateTables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    recreateTables()