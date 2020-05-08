import Transaksi

class pinjam():
    def __init__(self, NomorPinjam, IdCostumer, SisaBayar, Nama, Alamat, TanggalBayar, TanggalTempo):
        self.__NomorPinjam = NomorPinjam
        self.__IdCostumer= IdCostumer
        self.__SisaBayar = SisaBayar
        self.Nama = Nama
        self.__Alamat = Alamat
        self.__TanggalBayar = TanggalBayar
        self.__TanggalTempo = TanggalTempo

    @property
    def NomorPinjam(self):
        return self.__NomorPinjam
    @NomorPinjam.setter
    def NomorPinjam(self, NomorPinjam):
        self.__NomorPinjam = NomorPinjam

    @property
    def IdCostumer(self):
        return self.__IdCostumer
    @IdCostumer.setter
    def IdCostumer(self, IdCostumer):
        self.__IdCostumer = IdCostumer

    @property
    def SisaBayar(self):
        return self.__SisaBayar
    @SisaBayar.setter
    def SisaBayar(self, SisaBayar):
        self.__SisaBayar = SisaBayar

    @property
    def Alamat(self):
        return self.__Alamat
    @Alamat.setter
    def Alamat(self, Alamat):
        self.__Alamat = Alamat

    @property
    def TanggalBayar(self):
        return self.__TanggalBayar
    @TanggalBayar.setter
    def TanggalBayar(self, TanggalBayar):
        self.__TanggalBayar = TanggalBayar

    @property
    def TanggalTempo(self):
        return self.__TanggalTempo
    @TanggalTempo.setter
    def TanggalTempo(self, TanggalTempo):
        self.__TanggalTempo = TanggalTempo

    '''
    Terimakasih untuk transaksi yang telah dilakukan.
    Silahkan transaksi ulang jika ada yang kurang atau salah

                                Have a Nice Day
    '''

    def cetakNota(self) -> bool:
        pass
