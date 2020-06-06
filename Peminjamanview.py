from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from Model.AkunORM import Transaksi_Pinjam
import _sqlite3
import sys

class Pinjam(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Pinjam"
        self.top = 100
        self.left = 400
        self.widht = 800
        self.height = 600

        self.dataPinjam()

        self.setWindowIcon(QtGui.QIcon("sp.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.widht, self.height)

    def dataPinjam(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('bu4.png'))
        self.label.setGeometry(570, -100, 800, 400)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('bu2.png'))
        self.lbl.setGeometry(20, 300, 400, 400)

        self.datang = QLabel("Pinjam Koperasi.id", self)
        self.datang.setGeometry(20, -100, 800, 400)
        self.datang.setStyleSheet("color: #4682B4; font-size: 60px; font-style: calibri")

        #idUser
        self.id = QLabel("ID Customer", self)
        self.id.setGeometry(240, 170, 250, 30)
        self.id.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.idUser = QLineEdit(self)
        self.idUser.setPlaceholderText("Masukkan ID")
        self.idUser.setGeometry(350, 170, 250, 30)
        self.idUser.setStyleSheet("background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #username
        self.user = QLabel("ID Admin", self)
        self.user.setGeometry(240, 220, 250, 30)
        self.user.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Masukkan ID Admin")
        self.username.setGeometry(350, 220, 250, 30)
        self.username.setStyleSheet("background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #password
        self.pw = QLabel("Jumlah Pinjam", self)
        self.pw.setGeometry(240, 270, 250, 30)
        self.pw.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Masukkan Jumlah Pinjam")
        self.password.setGeometry(350, 270, 250, 30)
        self.password.setStyleSheet("background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #alamat
        self.almt = QLabel("Tanggal Pinjam", self)
        self.almt.setGeometry(240, 320, 250, 30)
        self.almt.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.alamat = QLineEdit(self)
        self.alamat.setPlaceholderText("Masukkan Tanggal Pinjam")
        self.alamat.setGeometry(350, 320, 250, 30)
        self.alamat.setStyleSheet("background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #tanggalLahir.
        self.tgl = QLabel("Tanggal Tempo", self)
        self.tgl.setGeometry(240, 370, 250, 30)
        self.tgl.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        #GANTI AJA TANGGAL NYA OTOMATIS
        self.tanggal = QLineEdit(self)
        self.tanggal.setPlaceholderText("Masukkan Tanggal Tempo ")
        self.tanggal.setGeometry(350, 370, 250, 30)
        self.tanggal.setStyleSheet("background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #kontak
        self.kntk = QLabel("Total Pinjam", self)
        self.kntk.setGeometry(240, 420, 250, 30)
        self.kntk.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.kontak = QLineEdit(self)
        self.kontak.setPlaceholderText("Masukkan Total Pinjam")
        self.kontak.setGeometry(350, 420, 250, 30)
        self.kontak.setStyleSheet("background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")


        # simpan button
        self.button = QPushButton("Simpan Data Peminjaman", self)
        self.button.setGeometry(QRect(350, 470, 250, 40))
        self.button.setStyleSheet("background-color: #00CED1; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")

        self.show()
    def isi(self, row):
        print(self.table.item(row,0).text())




App = QApplication(sys.argv)
pinjam = Pinjam()
sys.exit(App.exec())