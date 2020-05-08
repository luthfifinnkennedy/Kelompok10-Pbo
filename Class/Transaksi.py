class Transaksi:
    def __init__(self, namaTransaksi, nominal, tanggal):
        self.__namaTransaksi = nama
        self.__nominal = nominal
        self.__tanggal = tanggal

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def nominal(self):
        return self.__nominal
    @nominal.setter
    def nominal(self, nominal):
        self.__nominal = nominal

    @property
    def tanggal(self):
        return self.__tanggal
    @tanggal.setter
    def tanggal(self, tanggal):
        self.__tanggal = tanggal

