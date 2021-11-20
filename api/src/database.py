
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import config


base = declarative_base()


class Alert(base):
    __tablename__ = 'alerts'




engine = create_engine(URL(**config.db_connect_data))
base.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)