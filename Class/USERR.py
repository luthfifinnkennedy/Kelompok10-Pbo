from enum import Enum, auto

class Ketua(Enum):
    username = auto()
    password = auto()

class Bendahara(Enum):
    username = auto()
    password = auto()

class Anggota(Enum):
    nama = auto()
    alamat = auto()
    nomor_telepon = auto()

class Pegawai(Enum):
    nama = auto()
    alamat = auto()
    nomor_telepon = auto()
    id_pegawai = auto()

class user:
    def __init__(self, ketua: Ketua, bendahara: Bendahara, anggota: Anggota, pegawai: Pegawai):
        self.ketua = ketua
        self.bendahara = bendahara
        self.anggota = anggota
        self.pegawai = pegawai

    @property
    def ketua(self):
        return self.__ketua
    @ketua.setter
    def ketua(self, ketua):
        self.__ketua = ketua

    @property
    def bendahara(self):
        return self.__bendahara
    @bendahara.setter
    def bendahara(self, bendahara):
        self.__bendahara = bendahara

    @property
    def anggota(self):
        return self.__anggota
    @anggota.setter
    def anggota(self, anggota):
        self.__anggota = anggota

    @property
    def pegawai(self):
        return self.__pegawai
    @pegawai.setter
    def pegawai(self, pegawai):
        self.__pegawai = pegawai






