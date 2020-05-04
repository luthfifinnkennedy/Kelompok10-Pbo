from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Koperasi.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gudang(Base):
    __tablename__ = 'Gudang'

    kode_barang = Column(String, primary_key=True)
    nama_barang = Column(String)
    satuan = Column(Integer)
    harga = Column(Integer)
    stock = Column(Integer)


Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.close()





