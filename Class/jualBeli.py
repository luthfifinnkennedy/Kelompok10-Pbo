from Koperasi.transaksi import transaksi

class jualBeli(transaksi):
    def __init__(self, namaBarang, id, hargaBarang, jumlahBarang, discount):
        self.__namaBarang = namaBarang
        self.__id = id
        self.__hargaBarang = hargaBarang
        self.__jumlahBarang = jumlahBarang
        self.__discount = discount

    @property
    def namaBarang(self):
        return self.__namaBarang
    @namaBarang.setter
    def namaBarang(self, namaBarang):
        self.__namaBarang = namaBarang

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def hargaBarang(self):
        return self.__hargaBarang
    @hargaBarang.setter
    def hargaBarang(self, hargaBarang):
        self.__hargaBarang = hargaBarang

    @property
    def jumlahBarang(self):
        return self.__jumlahBarang
    @jumlahBarang.setter
    def jumlahBarang(self, jummlahBarang):
        self.__jumlahBarang = jummlahBarang

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount):
        self.__discount = discount