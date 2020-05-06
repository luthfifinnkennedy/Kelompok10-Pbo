from Koperasi.transaksi import transaksi

class simpan(transaksi):
    def __init__(self, id, nama, jumlahTransaksi, saldo):
        self.__id = id
        self.__nama = nama
        self.__jumlahTransaksi = jumlahTransaksi
        self.__saldo = saldo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def jumlahTransaksi(self):
        return self.__jumlahTransaksi
    @jumlahTransaksi.setter
    def jumlahTransaksi(self, jumlahTransaksi):
        self.__jumlahTransaksi = jumlahTransaksi

    @property
    def saldo(self):
        return  self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    