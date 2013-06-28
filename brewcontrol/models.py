from sqlalchemy import (
    Column,
    Integer,
    Float, 
    Integer,
    Text,
    DateTime,
    Unicode,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class TempSample(Base):
    __tablename__ = 'tempsamples'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    sensor = Column(Unicode)
    temp = Column(Float)
    target = Column(Float)
    
    def __init__(self, date, sensor, temp, target):
        super(TempSample, self).__init__()
        self.date = date
        self.sensor = sensor
        self.temp = temp
        self.target = target
        

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value
