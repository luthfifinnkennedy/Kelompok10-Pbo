import penjual
from transaksii import jualBeli

class stokBarang(jualBeli):
    def __init__(self, nama, kodeBarang, hargaSatuan, stock):
        self.__nama = nama
        self.__kodeBarang = kodeBarang
        self.__hargaSatuan = hargaSatuan
        self.__stock = stock

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def kodeBarang(self):
        return self.__kodeBarang
    @kodeBarang.setter
    def kodeBarang(self, kodeBarang):
        self.__kodeBarang = kodeBarang

    @property
    def hargaSatuan(self):
        return self.__hargaSatuan
    @hargaSatuan.setter
    def hargaSatuan(self, hargaSatuan):
        self.__hargaSatuan = hargaSatuan

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock):
        self.__stock = stock

