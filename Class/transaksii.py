class transaksi:
    def __init__(self, nama, nominal, tanggal_transaksi):
        self.nama = nama
        self.nominal = nominal
        self.tanggalTransaksi = tanggal_transaksi

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def nominal(self):
        return self.__nominal
    @nominal.setter
    def nominal(self, nominal):
        self.__nominal = nominal

    @property
    def tanggalTransaksi(self):
        return self.__tanggalTransaksi
    @tanggalTransaksi.setter
    def tanggalTransaksi(self, tanggalTransaksi):
        self.__tanggalTransaksi = tanggalTransaksi



class simpan(transaksi):
    def __init__(self, id, nama, jumlahTransaksi, tanggalTransaksi, saldo):
        self.__id = id
        self.__nama = nama
        self.__jumlahTransaksi = jumlahTransaksi
        self.__tanggalTransaksi = tanggalTransaksi
        self.__saldo = saldo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def jumlahTransaksi(self):
        return self.__jumlahTransaksi
    @jumlahTransaksi.setter
    def jumlahTransaksi(self, jumlahTransaksi):
        self.__jumlahTransaksi = jumlahTransaksi

    @property
    def tanggalTransaksi(self):
        return  self.__tanggalTransaksi
    @tanggalTransaksi.setter
    def tanggalTransaksi(self, tanggalTransaksi):
        self.__tanggalTransaksi = tanggalTransaksi

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo



class pinjam(transaksi):
    def __init__(self, no, id, nama, alamat, sisaBayar, tanggalPinjam, tanggalBayar, tanggalTempo):
        self.__no = no
        self.__id = id
        self.__nama = nama
        self.__alamat = alamat
        self.__sisaBayar = sisaBayar
        self.__tanggalPinjam = tanggalPinjam
        self.__tanggalBayar = tanggalBayar
        self.__tanggalTempo = tanggalTempo

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no):
        self.__no = no

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
    def sisaBayar(self):
        return self.__sisaBayar
    @sisaBayar.setter
    def sisaBayar(self, sisaBayar):
        self.__sisaBayar = sisaBayar

    @property
    def tanggalPinjam(self):
        return self.__tanggalPinjam
    @tanggalPinjam.setter
    def tanggalPinjam(self, tanggalPinjam):
        self.__tanggalPinjam = tanggalPinjam

    @property
    def tanggalBayar(self):
        return self.__tanggalBayar
    @tanggalBayar.setter
    def tanggalBayar(self, tanggalBayar):
        self.__tanggalBayar = tanggalBayar

    @property
    def tanggalTempo(self):
        return self.tanggalTempo
    @tanggalTempo.setter
    def tanggalTempo(self, tanggalTempo):
        self.__tanggalTempo = tanggalTempo



class jualBeli(transaksi):
    def __init__(self, idBarang, namaBarang, tanggal, hargaBarang, jumlahBarang):
        self.__idBarang = idBarang
        self.__namaBarang = namaBarang
        self.__tanggal = tanggal
        self.__hargaBarang = hargaBarang
        self.__jumlahBarang = jumlahBarang

    @property
    def idBarang(self):
        return self.__idBarang
    @idBarang.setter
    def idBarang(self, idBarang):
        self.__idBarang = idBarang

    @property
    def namaBarang(self):
        return self.__namaBarang
    @namaBarang.setter
    def namaBarang(self, namaBarang):
        self.__namaBarang = namaBarang

    @property
    def tanggal(self):
        return self.__tanggal
    @tanggal.setter
    def tanggal(self, tanggal):
        self.__tanggal = tanggal

    @property
    def hargaBarang(self):
        return self.__hargaBarang
    @hargaBarang.setter
    def hargaBarang(self, hargaBarang):
        self.__hargaBarang = hargaBarang

    @property
    def jumlahBarang(self):
        return self.__jumlahBarang
    @jumlahBarang.setter
    def jumlahBarang(self, jumlahBarang):
        self.__jumlahBarang = jumlahBarang
