from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def initialize_sql():
    Session = sessionmaker()
    engine = create_engine('sqlite:///mypoop.db', echo=True,
                           connect_args={'check_same_thread': False})
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    return Session
