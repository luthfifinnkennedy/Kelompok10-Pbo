# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaksi.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 594)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 150, 161, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 150, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 131, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 180, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 220, 111, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(200, 220, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 150, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 150, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 250, 101, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 250, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 180, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 180, 161, 51))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(450, 240, 91, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 240, 121, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(100, 290, 101, 20))
        self.label_8.setObjectName("label_8")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(200, 290, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(110, 320, 61, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 340, 281, 51))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 510, 91, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 510, 101, 61))
        icon = QtGui.QIcon.fromTheme("x")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 510, 91, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 510, 91, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(80, 40, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Jenis Transaksi"))
        self.label_2.setText(_translate("Dialog", "Nominal"))
        self.label_3.setText(_translate("Dialog", "Tanggal Transaksi"))
        self.label_4.setText(_translate("Dialog", "No Telepon"))
        self.label_5.setText(_translate("Dialog", "Jenis Pembayaran"))
        self.label_6.setText(_translate("Dialog", "Alamat"))
        self.label_7.setText(_translate("Dialog", "Id"))
        self.label_8.setText(_translate("Dialog", "Jangka Waktu"))
        self.label_9.setText(_translate("Dialog", "Keterangan"))
        self.pushButton_2.setText(_translate("Dialog", "Simpan"))
        self.pushButton_3.setText(_translate("Dialog", "Keluar"))
        self.pushButton_4.setText(_translate("Dialog", "Simpan Tambah"))
        self.pushButton_5.setText(_translate("Dialog", "Hapus"))
        self.label_10.setText(_translate("Dialog", "Transaksi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())