from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from Model.AkunORM import Transaksi_Simpan

class Simpan(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Penyimpanan"
        self.top = 100
        self.left = 400
        self.widht = 800
        self.height = 600

        self.penyimpanan()

        self.setWindowIcon(QtGui.QIcon("pj.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.widht, self.height)

    def penyimpanan(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('bu4.png'))
        self.label.setGeometry(570, -100, 800, 400)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('bu2.png'))
        self.lbl.setGeometry(20, 300, 400, 400)

        self.pinjam = QLabel("Simpan Koperasi.id", self)
        self.pinjam.setGeometry(20, -100, 800, 400)
        self.pinjam.setStyleSheet("color: #4682B4; font-size: 60px; font-style: calibri")

        # idUser
        self.id = QLabel("ID Customer", self)
        self.id.setGeometry(240, 170, 250, 30)
        self.id.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.idUser = QLineEdit(self)
        self.idUser.setPlaceholderText("Masukkan ID")
        self.idUser.setGeometry(360, 170, 250, 30)
        self.idUser.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # username
        self.user = QLabel("ID Admin", self)
        self.user.setGeometry(240, 220, 250, 30)
        self.user.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Masukkan ID Admin")
        self.username.setGeometry(360, 220, 250, 30)
        self.username.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # password
        self.pw = QLabel("Jumlah Penyimpanan", self)
        self.pw.setGeometry(240, 270, 250, 30)
        self.pw.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Masukkan Jumlah Penyimpanan")
        self.password.setGeometry(360, 270, 250, 30)
        self.password.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # alamat
        self.almt = QLabel("Tanggal Simpan", self)
        self.almt.setGeometry(240, 320, 250, 30)
        self.almt.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.alamat = QLineEdit(self)
        self.alamat.setPlaceholderText("Masukkan Tanggal Simpan")
        self.alamat.setGeometry(360, 320, 250, 30)
        self.alamat.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # tanggalLahir.
        self.tgl = QLabel("Total Simpan", self)
        self.tgl.setGeometry(240, 370, 250, 30)
        self.tgl.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        # GANTI AJA TANGGAL NYA OTOMATIS
        self.tanggal = QLineEdit(self)
        self.tanggal.setPlaceholderText("Masukkan Total Simpan")
        self.tanggal.setGeometry(360, 370, 250, 30)
        self.tanggal.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")


        # pinjam button
        self.button = QPushButton("Simpan Data Pinjaman", self)
        self.button.setGeometry(QRect(360, 420, 250, 40))
        self.button.setStyleSheet( "background-color: #00CED1; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")

        self.show()




App = QApplication(sys.argv)
simpan = Simpan()
sys.exit(App.exec())