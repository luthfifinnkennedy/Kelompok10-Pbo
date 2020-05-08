import Transaksi

class simpan():
    def __init__(self, IdCostumer, NamaCostumer, JumlahTransaksi, Saldo):
        self.__IdCostumer = IdCostumer
        self.Nama = Nama
        self.__JumlahTransaksi = JumlahTransaksi
        self.__Saldo = Saldo

    @property
    def IdCostumer(self):
        return self.__IdCostumer
    @IdCostumer.setter
    def IdCostumer(self, IdCostumer):
        self.__IdCostumer = IdCostumer

    @property
    def JumlahTransaksi(self):
        return self.__JumlahTransaksi
    @JumlahTransaksi.setter
    def JumlahTransaksi(self, JumlahTransaksi):
        self.__JumlahTransaksi = JumlahTransaksi

    @property
    def Saldo(self):
        return  self.__Saldo
    @Saldo.setter
    def Saldo(self, Saldo):
        self.__Saldo = Saldo
    
    '''
    Terimakasih untuk transaksi yang telah dilakukan.
    Silahkan transaksi ulang jika ada yang kurang atau salah

                                Have a Nice Day
    '''

    def cetakNota(self) -> bool:
        pass
