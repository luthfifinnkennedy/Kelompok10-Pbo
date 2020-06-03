from transaksii import pinjam

class Denda(pinjam):
    def __init__(self, id, tanggalPinjam, jumlahDenda):
        self.__id = id
        self.__tanggalPinjam = tanggalPinjam
        self.__jumlahDenda = jumlahDenda

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tanggalPinjam(self):
        return self.__tanggalPinjam
    @tanggalPinjam.setter
    def tanggalPinjam(self, tanggalPinjam):
        self.__tanggalPinjam = tanggalPinjam

    @property
    def jumlahDenda(self):
        return self.__jumlahDenda
    @jumlahDenda.setter
    def jumlahDenda(self, jumlahDenda):
        self.__jumlahDenda = jumlahDenda


    def cetakBukti(self, bool):
        pass

