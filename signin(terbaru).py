from PyQt5.QtWidgets import QMainWindow,QApplication , QLabel, QTextEdit, QPushButton,QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import QRect

import sys


class Signin(QMainWindow,):
    def __init__(self):
        super().__init__()



        self.title = "Sign in"
        self.top = 100
        self.left = 400
        self.widht = 800
        self.height = 600

        self.InitWindow()


    def InitWindow(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('flowers.jpg'))
        self.label.setGeometry(-2, -100, 800, 300)


        self.lbl = QLabel(self)
        self.lbl.setPixmap(QPixmap('unnamed.gif'))
        self.lbl.setGeometry(5, 120, 400, 400)

        self.datang = QLabel("Silahkan Sign in", self)
        self.datang.setGeometry(350, -150, 700, 400)
        self.datang.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")




        self.setWindowIcon(QtGui.QIcon("home.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.widht, self.height)


        #create field nama
        self.nama = QLabel("Nama :", self)
        self.nama.setGeometry(150, -60, 700, 400)
        self.nama.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")


        self.nama = QTextEdit(self)
        self.nama.setGeometry(230, 120, 250, 40)
        self.nama.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #create field Id
        self.id = QLabel("Id :", self)
        self.id.setGeometry(500, -60, 700, 400)
        self.id.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")

        self.id = QTextEdit(self)
        self.id.setGeometry(540, 120, 250, 40)
        self.id.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #create field Alamat
        self.alamat = QLabel("Alamat :", self)
        self.alamat.setGeometry(150, 0, 700, 400)
        self.alamat.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")

        self.alamat = QTextEdit(self)
        self.alamat.setGeometry(230, 180, 250, 40)
        self.alamat.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #create Email
        self.email = QLabel("Email :", self)
        self.email.setGeometry(150, 60, 700, 400)
        self.email.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")

        self.email = QTextEdit(self)
        self.email.setGeometry(240, 240, 250, 40)
        self.email.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #create UserName
        self.username = QLabel("Username :", self)
        self.username.setGeometry(150, 120, 700, 400)
        self.username.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")

        self.username = QTextEdit(self)
        self.username.setGeometry(260, 300, 250, 40)
        self.username.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")

        #create Password
        self.password = QLabel("Password :", self)
        self.password.setGeometry(150, 160, 700, 400)
        self.password.setStyleSheet("color: #DE7608; font-size: 20px; font-style: calibri")

        self.password = QTextEdit(self)
        self.password.setGeometry(260, 350, 250, 40)
        self.password.setStyleSheet("background-color: #f7f7f7; color: #8e8e8e; padding-top: 5px; font-size: 15px; padding-left: 10px")



        #login button
        self.button = QPushButton("Sign in", self)
        self.button.setGeometry(QRect(500, 500, 250, 40))
        self.button.setToolTip("Silahkan klik untuk Sign in")
        self.button.setStyleSheet("background-color: #38DE08; color: black; padding-top: 2px; font-size: 20px; padding-left: 10px")



        #Cancel button
        self.button = QPushButton("Cancel", self)
        self.button.setGeometry(QRect(100, 500, 250, 40))
        self.button.setToolTip("Silahkan klik untuk Sign in")
        self.button.setStyleSheet("background-color: #E10A0A; color: black; padding-top: 2px; font-size: 20px; padding-left:10px")

        self.show()


   













App = QApplication(sys.argv)
window = Signin()
sys.exit(App.exec())
