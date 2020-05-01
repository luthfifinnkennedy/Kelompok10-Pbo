from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sales.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Kategori(Base):
    __tablename__ = "kategori"

    Kode_Kategori = Column(Integer, primary_key=True)
    Nama_Kategori = Column(String)
    Deskripsi = Column(String)

    def __init__(self, Kode_Kategori, Nama_Kategori, Deskripsi):
        self.Kode_Kategori = Kode_Kategori
        self.Nama_Kategori = Nama_Kategori
        self.Deskripsi = Deskripsi

        @property
        def kodeKategori(self):
            pass

        @kodeKategori.getter
        def kodeKategori(self):
            return self.kodeKategori

        @kodeKategori.setter
        def kodeKategori(self, kodeKategori):
            self.kodeKategori = kodeKategori

        @property
        def namaKategori(self):
            pass

        @namaKategori.getter
        def namaKategori(self):
            return self.namaKategori

        @namaKategori.setter
        def namaKategori(self, namaKategori):
            self.namaKategori = namaKategori
        @property
        def deskripsi(self):
            pass

        @deskripsi.getter
        def deskripsi(self):
            return self.deskripsi

        @deskripsi.setter
        def deskripsi(self, deskripsi):
            self.deskripsi = deskripsi


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

kategori1 = Kategori(Kode_Kategori=201, Nama_Kategori="namaa", Deskripsi="desc aja")

session.add(kategori1)







