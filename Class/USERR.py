from enum import Enum, auto

class Admin(Enum):
    username = auto()
    password = auto()
    id_admin = auto()

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
    
class Penjual(Enum):
    kode_penjualan = auto()
    id_penjual = auto()

class user:
    def __init__(self, admin: Admin, ketua: Ketua, bendahara: Bendahara, anggota: Anggota, pegawai: Pegawai, penjual: Penjual):
        self.admin = admin
        self.ketua = ketua
        self.bendahara = bendahara
        self.anggota = anggota
        self.pegawai = pegawai
        self.penjual = penjual

    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin):
        self.__admin = admin
        
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

    @property
    def penjual(self):
        return self.__penjual
    @penjual.setter
    def penjual(self, penjual):
        self.__penjual = penjual




