class penjual:
    def __init__(self, kodePenjualan, id, tanggal):
        self.__kodePenjualan = kode
        self.__id = id
        self.__tanggal = tanggal

    @property
    def kode(self):
        return self.__kode
    @kode.setter
    def kode(self, kode):
        self.__kode = kode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tanggal(self):
        return self.__tanggal
    @tanggal.setter
    def tanggal(self, tanggal):
        self.__tanggal = tanggal

