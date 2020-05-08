from Class.Transaksi import Transaksi

class jualBeli(Transaksi):
    def __init__(self, NamaBarang, IdBarang, Tanggal, HargaBarang, JumlahBarang):
        self.__NamaBarang = NamaBarang
        self.__IdBarang = Id
        self.__Tanggal = Tanggal
        self.__HargaBarang = HargaBarang
        self.__JumlahBarang = JumlahBarang

    @property
    def NamaBarang(self):
        return self.__NamaBarang
    @NamaBarang.setter
    def NamaBarang(self, NamaBarang):
        self.__NamaBarang = NamaBarang

    @property
    def IdBarang(self):
        return self.__IdBarang
    @id.setter
    def IdBarang(self, IdBarang):
        self.__IdBarang = IdBarang

    @property
    def Tanggal(self):
        return self.__Tanggal
    @tglTransaksi.setter
    def Tanggal(self, Tanggal):
        self.__Tanggal = Tanggal

    @property
    def HargaBarang(self):
        return self.__HargaBarang
    @HargaBarang.setter
    def HargaBarang(self, HargaBarang):
        self.__HargaBarang = HargaBarang

    @property
    def JumlahBarang(self):
        return self.__JumlahBarang
    @JumlahBarang.setter
    def JumlahBarang(self, JummlahBarang):
        self.__JumlahBarang = JummlahBarang

    '''
    Terima kasih terlah mengakses. Silahkan lakukan transasksi ulang,
    jika ada yang kurang atau terlewat.

                                  Have a Nice Day                               
    '''

    def cetakNota(self) -> bool:
        pass
