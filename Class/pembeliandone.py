from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sales.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pembelian(Base):
    __tablename__ = "pembelian"

    idBarang = Column(Integer, primary_key= True)
    namaBarang = Column(String)
    kategori = Column(String)
    tanggal = Column(DateTime)

    def __init__(self, idBarang, namaBarang, kategori, tanggal):
        self.idBarang = idBarang
        self.namaBarang = namaBarang
        self.kategori = kategori
        self.tanggal = tanggal

        @property
        def idBarang(self):
            pass

        @idBarang.getter
        def idBarang(self):
            return self.idBarang

        @idBarang.setter
        def idBarang(self, idBarang):
            self.idBarang = idBarang

        @property
        def namaBarang(self):
            pass

        @namaBarang.getter
        def namaBarang(self):
            return self.namaBarang

        @namaBarang.setter
        def namaBarang(self, namaBarang):
            self.namaBarang = namaBarang
        @property
        def kategori(self):
            pass

        @kategori.getter
        def kategori(self):
            return self.kategori

        @kategori.setter
        def kategori(self, kategori):
            self.kategori = kategori

        @property
        def tanggal(self):
            pass

        @tanggal.getter
        def tanggal(self):
            return self.tanggal

        @tanggal.setter
        def tanggal(self, tanggal):
            self.tanggal = tanggal


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

pembelian1 = Pembelian(idBarang=201, namaBarang= "nama", kategori="kategorinya", tanggal= 20-1-2020)

session.add(pembelian1)







