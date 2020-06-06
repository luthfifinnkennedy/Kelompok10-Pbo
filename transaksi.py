from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QDialog
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtGui

class Transaksi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Transaksi"
        self.top = 100
        self.left = 400
        self.widht = 800
        self.height = 600

        self.text()

        self.setWindowIcon(QtGui.QIcon("tra.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.widht, self.height)

    def text(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('bu4.png'))
        self.label.setGeometry(570, -100, 800, 400)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('bu2.png'))
        self.lbl.setGeometry(20, 300, 400, 400)

        self.datang = QLabel("Transaksi Koperasi.id", self)
        self.datang.setGeometry(20, -100, 800, 400)
        self.datang.setStyleSheet("color: #4682B4; font-size: 60px; font-style: calibri")

        self.btn1 = QPushButton("Simpan", self)
        self.btn1.setGeometry(200, 200, 350, 50)
        self.btn1.setToolTip("Klik untuk melakukan transaksi Simpan")
        self.btn1.setStyleSheet("background-color: #00CED1; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")
        self.btn1.clicked.connect(self.openBtn1)

        self.btn2 = QPushButton("Pinjam", self)
        self.btn2.setGeometry(300, 300, 350, 50)
        self.btn2.setToolTip("Klik untuk melakukan transaksi Pinjam")
        self.btn2.setStyleSheet("background-color: #6495ED; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")
        self.btn2.clicked.connect(self.openBtn2)

        self.btn3 = QPushButton("Jual Beli", self)
        self.btn3.setGeometry(400, 400, 350, 50)
        self.btn3.setToolTip("Klik untuk melakukan transaksi Jual Beli")
        self.btn3.setStyleSheet("background-color: 	#8FBC8F; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")
        self.btn3.clicked.connect(self.openBtn3)

        self.show()




    def openBtn1(self):
        from GUI import Peminjamanview
        #mybtn1 = QDialog()
        #mybtn1.setModal(True)
        #mybtn1.exec()

    def openBtn2(self):
        from GUI import Penyimpananview
        mybtn2 = QDialog()
        mybtn2.setModal(True)
        mybtn2.exec()

    def openBtn3(self):
        from GUI import jualBeli
        mybtn3 = QDialog()
        mybtn3.setModal(True)
        mybtn3.exec()

App = QApplication(sys.argv)
transaksi = Transaksi()
sys.exit(App.exec())