class login(object):
    def __init__(self, *args, **kwargs):
        self.__username = kwargs.get('username', 'mimin')
        self.__password = kwargs.get('password', '1111')

        @property
        def username(self):
            return self.__username

        @username.setter
        def username(self, username):
            self.__username = username

        @property
        def password(self):
            return self.__password

        @password.setter
        def password(self, password):
            self.__password = password

    def login_autentikator(self):
        pass
        
        
class admin(object):
    def __init__(self, *args, **kwargs):
        self.__id = kwargs.get('id', '111')
    def __init__(self, *args, **kwargs):
        self.__proposal = kwargs.get('proposal', 'nomor 1')
    def __init__(self, *args, **kwargs):
        self.__stokBarang = kwargs.get('stokBarang', '01')
    def __init__(self, *args, **kwargs):
        self.__pembelian = kwargs.get('pembelian', 'namaBarang')	

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def proposal(self):
        return self.__proposal

    @proposal.setter
    def proposal(self, proposal):
        self.__proposal = proposal

    @property
    def stokBarang(self):
        return self.__stokBarang

    @stokBarang.setter
    def stokBarang(self, stokBarang):
        self.__stokBarang = stokBarang
        
    @property
    def pembelian(self):
        return self.__pembelian

    @pembelian.setter
    def pembelian(self, pembelian):
        self.__pembelian = pembelian
              
class penjual(object):
    def __init__(self, *args, **kwargs):
        self.__id_client = kwargs.get('id_client', '11')
        self.__date = kwargs.get('date')
        self.__transaksi = kwargs.get ('transaksi', '01')
    def __Transaksi(self, *args, **kwargs):
        return self.__transaksi
    def __Transaksi(self, *args, **kwargs):
        self.__transaksi = kwargs.get ('baru')

    @property
    def id_client (self):
        return self.__id_client
    @id_client.setter
    def id_client (self):
        return self.__id_client
    
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self):
        return self.__date

    @property
    def transaksi(self):
        return self._transasksi
    @date.setter
    def transaksi(self):
        return self._transasksi

    
class customer(object):
    def __init__(self,*args, **kwargs ):
        self.__id_user = kwargs.get ('id_user','Nadiah')
        self.__simpanan = kwargs.get ('simpanan', '11')
        self.__pinjaman = kwargs.get ('pinjaman''111')
        self.__angsuran = kwargs.get ('angsuran', '1111')
        self__.denda = kwargs.get ('denda','11111')

    @property
    def id_user (self):
        return self.__id_user
    @id_user.setter
    def id_user (self):
        return self.__id_user

    @property
    def Simpanan(self):
        return self.__simpanan
    @Simpanan.setter
    def Simpanan(self):
        return self.__simpanan
    
    @property
    def Pinjaman(self):
        return self.__pinjaman
    @Pinjaman.setter
    def Pinjaman(self, baru):
        return self.__pinjaman 

    @property
    def Angsuran(self):
        return self.__angsuran
    @Angsuran.setter
    def Angsuran(self, baru):
        return self.__angsuran 

    @property
    def Denda(self):
        return self.__denda
    @Denda.setter
    def Denda(self, baru):
        return self.__denda 