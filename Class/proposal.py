class poposal:

    def __init__(self, nama, pengaju, tanggalPengajuan, balasanProposal):
        self.__nama = nama
        self.__pengaju = pengaju
        self.__tanggalPengajuan = tanggalPengajuan
        self.__balasan = balasanProposal

    @property
    def nama(self):
        pass
    @nama.getter
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def pengaju(self):
        return self.__pengaju
    @pengaju.setter
    def pengaju(self, pengaju):
        self.__pengaju = pengaju

    @property
    def tanggalPengaju(self):
        return self.__tanggalPengajuan
    @tanggalPengaju.setter
    def tanggalPengaju(self, tanggalPengaju):
        self.__tanggalPengajuan = tanggalPengaju

    @property
    def balasan(self):
        return self.__balasan
    @balasan.setter
    def balasan(self, balasan):
        self.__balasan = balasan



