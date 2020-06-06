#from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
import pymysql
import Model.admin as mdb
from Model.Data_Base import *
from Model.admin import *
from Class.Admin import *
from Class.Hak_akses import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Login"
        self.top = 100
        self.left = 400
        self.widht = 800
        self.height = 600

        self.InitWindow()
        self.login()


    def InitWindow(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('bu4.png'))
        self.label.setGeometry(570, -100, 800, 400)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('bu2.png'))
        self.lbl.setGeometry(20, 300, 400, 400)

        self.datang = QLabel("Selamat Datang", self)
        self.datang.setGeometry(20, -100, 800, 400)
        self.datang.setStyleSheet("color: #4682B4; font-size: 70px; font-style: calibri")

        self.koperasi = QLabel("di Koperasi.id", self)
        self.koperasi.setGeometry(20, -30, 800, 400)
        self.koperasi.setStyleSheet("color: #4682B4; font-size: 40px; font-style: calibri")

        self.setWindowIcon(QtGui.QIcon("home.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.widht, self.height)


        #field user
        '''
        vbox = QVBoxLayout()
        self.user = QComboBox(self)
        self.user.addItem("Ketua")
        self.user.addItem("Bendahara")
        self.user.addItem("Anggota")
        self.user.addItem("Pegawai")
        self.user.setGeometry(300, 250, 250, 40)
        vbox.addWidget(self.user)
        self.setLayout(vbox)
        self.user.setStyleSheet("color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")
        '''
        #create field username
        self.username = QLineEdit(self)
        self.username.setGeometry(300, 230, 250, 40)
        self.username.setPlaceholderText("Masukkan Username")
        self.username.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #field password
        self.password = QLineEdit(self)
        self.password.setGeometry(300, 300, 250, 40)
        self.password.setPlaceholderText("Masukkan Password")
        self.password.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #field id
        self.id = QLineEdit(self)
        self.id.setGeometry(300, 370, 250, 40)
        self.id.setPlaceholderText("Masukkan id")
        self.id.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #field hak akses
        self.hak = QLineEdit(self)
        self.hak.setGeometry(300, 440, 250, 40)
        self.hak.setPlaceholderText("Hak Akses Sebagai :")
        self.hak.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #login button
        self.button = QPushButton("Login", self)
        self.button.setGeometry(QRect(300, 510, 250, 40))
        self.button.setToolTip("Silahkan klik untuk Login")
        self.button.setStyleSheet("background-color: #00ffff; color: black; padding-top: 2px; font-size: 15px; padding-left: 10px")
        self.button.clicked.connect(self.login)

        self.show()

    def login(self):
        con = pymysql.connect(db='Koperasi.db', user ='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("koneksi", "koneksi berhasil")
        else:
            self.messagebox("koneksi", "koneksi gagal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    '''
    def mesaageBox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()
    '''

    '''
     def login(self):
        con = AdminOrm.connect('localhost', 'root', '', 'pyqt5')
        with con:
            cur = con.cursor()

            cur.execute("INSERT INTO Admin(username, password, id, Hak_akses)"
                        "VALUES('%s', '%s', '%s', '%s')" % (''.join(self.username.text()),
                                                            ''.join(self.password.text()),
                                                            ''.join(self.id.text()),
                                                            ''.join(self.hak.text()))

        QMessageBox.about(self, 'Connection', 'Login Berhasil')
        self.show()
    '''





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())