from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from Model.AkunORM import Transaksi_JualBeli

class JualBeli(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Jual Beli"
        self.top = 100
        self.left = 400
        self.widht = 800
        self.height = 600

        self.peminjaman()

        self.setWindowIcon(QtGui.QIcon("jb.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.widht, self.height)

    def peminjaman(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('bu4.png'))
        self.label.setGeometry(570, -100, 800, 400)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('bu2.png'))
        self.lbl.setGeometry(20, 300, 400, 400)

        self.pinjam = QLabel("JualBeli di Koperasi.id", self)
        self.pinjam.setGeometry(20, -100, 800, 400)
        self.pinjam.setStyleSheet("color: #4682B4; font-size: 60px; font-style: calibri")

        # idUser
        self.id = QLabel("ID", self)
        self.id.setGeometry(250, 170, 250, 30)
        self.id.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.idUser = QLineEdit(self)
        self.idUser.setPlaceholderText("Masukkan ID")
        self.idUser.setGeometry(330, 170, 250, 30)
        self.idUser.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # username
        self.user = QLabel("Username", self)
        self.user.setGeometry(240, 220, 250, 30)
        self.user.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Masukkan Username")
        self.username.setGeometry(330, 220, 250, 30)
        self.username.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # password
        self.pw = QLabel("Password", self)
        self.pw.setGeometry(240, 270, 250, 30)
        self.pw.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Masukkan Password")
        self.password.setGeometry(330, 270, 250, 30)
        self.password.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # alamat
        self.almt = QLabel("Alamat", self)
        self.almt.setGeometry(240, 320, 250, 30)
        self.almt.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.alamat = QLineEdit(self)
        self.alamat.setPlaceholderText("Masukkan Alamat")
        self.alamat.setGeometry(330, 320, 250, 30)
        self.alamat.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # tanggalLahir.
        self.tgl = QLabel("Tanggal Lahir", self)
        self.tgl.setGeometry(240, 370, 250, 30)
        self.tgl.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        # GANTI AJA TANGGAL NYA OTOMATIS
        self.tanggal = QLineEdit(self)
        self.tanggal.setPlaceholderText("Masukkan Tanggal Lahir ")
        self.tanggal.setGeometry(330, 370, 250, 30)
        self.tanggal.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # kontak
        self.kntk = QLabel("Kontak", self)
        self.kntk.setGeometry(240, 420, 250, 30)
        self.kntk.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.kontak = QLineEdit(self)
        self.kontak.setText("+62 8")
        self.kontak.setGeometry(330, 420, 250, 30)
        self.kontak.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # job
        self.jb = QLabel("Job", self)
        self.jb.setGeometry(240, 470, 250, 30)
        self.jb.setStyleSheet("color: black; font-size: 15px; font-style: calibri")
        self.job = QLineEdit(self)
        self.job.setPlaceholderText("Masukkan Pekerjaan")
        self.job.setGeometry(330, 470, 250, 30)
        self.job.setStyleSheet(
            "background-color: #f7f7f7; color: black; padding-top: 5px; font-size: 15px; padding-left: 10px")

        # pinjam button
        self.button = QPushButton("Simpan Data Jual Beli", self)
        self.button.setGeometry(QRect(330, 520, 250, 40))
        self.button.setStyleSheet( "background-color: #00CED1; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")

        self.show()


App = QApplication(sys.argv)
jualBeli = JualBeli()
sys.exit(App.exec())