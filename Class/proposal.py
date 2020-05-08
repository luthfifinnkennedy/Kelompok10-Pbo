import admin

class proposal:
    def __init__(self, Nama, Pengaju, TanggalPengajuan, BalasanProposal):
        self.__NamaPengaju = NamaPengaju
        self.__TanggalPengajuan = TanggalPengajuan
        self.__BalasanProposal = BalasanProposal

    @property
    def Namapengaju(self):
        pass
    @Namapengaju.getter
    def NamaPengaju(self):
        return self.__NamaPengaju
    @Namapengaju.setter
    def NamaPengaju(self, NamaPengaju):
        self.__NamaPengaju = NamaPengaju

    @property
    def TanggalPengajuan(self):
        return self.__tanggalPengajuan
    @TanggalPengajuan.setter
    def TanggalPengajuan(self, TanggalPengajuan):
        self.__TanggalPengajuan = TanggalPengajuan

    @property
    def Balasan(self):
        return self.__Balasan
    @Balasan.setter
    def Balasan(self, Balasan):
        self.__Balasan = Balasan
