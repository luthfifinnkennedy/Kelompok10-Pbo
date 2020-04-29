from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class LoginCustomer(Base):

    __tablename__= 'Customer'

    Username = Column(Integer, Primary_key=True)
    Password = Column(string)

engine = craete_engine('sqlite:///:memory', echo=True)
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)

session= Session()

session.close()
