from abc import ABC, abstractmethod, abstractproperty

class transaksi(ABC):

    @abstractproperty
    def nama(self):
        pass

    @abstractproperty
    def nominal(self):
        pass

    @abstractproperty
    def tglTransaksi(self):
        pass