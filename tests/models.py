from __future__ import absolute_import
import sqlalchemy
from sqlalchemy import *

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()

engine = create_engine('postgresql://postgres:@localhost/sqlagg_test')

Session = scoped_session(sessionmaker(bind=engine))
engine.execute(sqlalchemy.text('CREATE OR REPLACE VIEW "user_view" as SELECT * from user_table'))


class UserTable(Base):
    __tablename__ = 'user_table'

    user = Column(String(50), primary_key=True, autoincrement=False)
    date = Column(DATE, primary_key=True, autoincrement=False)
    indicator_a = Column(INT)
    indicator_b = Column(INT)
    indicator_c = Column(INT)


class RegionTable(Base):
    __tablename__ = 'region_table'

    region = Column(String(50), primary_key=True, autoincrement=False)
    sub_region = Column(String(50), primary_key=True, autoincrement=False)
    date = Column(DATE, primary_key=True, autoincrement=False)
    indicator_a = Column(INT)
    indicator_b = Column(INT)

Base.metadata.create_all(engine)
