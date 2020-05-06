from Koperasi.transaksi import transaksi

class pinjam(transaksi):
    def __init__(self, nomorPinjam, id, sisaBayar, alamat, tanggalBayar, tanggalTempo):
        self.__nomor = nomorPinjam
        self.__id = id
        self.__sisaBayar = sisaBayar
        self.__alamat = alamat
        self.__tanggalBayar = tanggalBayar
        self.__tanggalTempo = tanggalTempo

    @property
    def nomor(self):
        return self.__nomor
    @nomor.setter
    def nomor(self, nomor):
        self.__nomor = nomor

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def sisaBayar(self):
        return self.__sisaBayar
    @sisaBayar.setter
    def sisaBayar(self, sisaBayar):
        self.__sisaBayar = sisaBayar

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat

    @property
    def tanggalBayar(self):
        return self.__tanggalBayar
    @tanggalBayar.setter
    def tanggalBayar(self, tanggalBayar):
        self.__tanggalBayar = tanggalBayar

    @property
    def tanggalTempo(self):
        return self.__tanggalTempo
    @tanggalTempo.setter
    def tanggalTempo(self, tanggalTempo):
        self.__tanggalTempo = tanggalTempo



