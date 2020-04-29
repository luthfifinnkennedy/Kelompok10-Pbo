from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Gudang(Base):
                         
    __tablename__= 'Gudang'

    kode_barang = Column(String, Primary_Key=True
    nama_barang = Column(String)
    satuan = Column(Integer)
    harga = Column(Integer)
    stock = Column (integer)
                         
engine = craete_engine('sqlite:///:memory', echo=True)
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)

session= Session()

session.close()





