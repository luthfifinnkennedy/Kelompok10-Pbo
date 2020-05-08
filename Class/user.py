class user:
    def __init__(self, namaUser, idUser):
        self.__namaUser = nama
        self.__idUser = id

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


