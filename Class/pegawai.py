class pegawai:
    def __init__(self, nama, id, alamat, nomorTelepon):
        self.__nama = nama
        self.__id = id
        self.__alamat = alamat
        self.__nomorTelepon = nomorTelepon

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat

    @property
    def nomorTelepon(self):
        return self.__nomorTelepon
    @nomorTelepon.setter
    def nomorTelepon(self, nomorTelepon):
        self.__nomorTelepon = nomorTelepon

