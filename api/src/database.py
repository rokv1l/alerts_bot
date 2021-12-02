
from sqlalchemy import types
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import config


base = declarative_base()


class User(base):
    __tabelname__ = 'users'

    id = Column(types.Integer, primary_key=True)
    active = Column(types.Boolean, default=True)


class Alert(base):
    __tablename__ = 'alerts'
    
    id = Column(types.Integer, primary_key=True, autoincrement=True)
    message = Column(types.Text)
    datetime = Column(types.DateTime)
    sent = Column(types.Boolean, default=False)


engine = create_engine(URL(**config.db_connect_data))
base.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)