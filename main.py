import sys
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi
# from qfluentwidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import validasi
import transaksi

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.setGeometry(20,50, 388, 409)
        self.setFixedSize(388, 409)
        self.setWindowTitle("MoMa App")
        self.stackedWidget.setCurrentIndex(0)
        self.login_btn.clicked.connect(lambda: self.tujuan("main_login"))
        self.register_btn.clicked.connect(lambda: self.tujuan("main_register"))
        self.register_btn2.clicked.connect(lambda: self.login("register"))
        self.login_btn2.clicked.connect(lambda: self.login("login"))
        self.kembali.clicked.connect(lambda: self.tujuan("balek"))
        self.kembali_2.clicked.connect(lambda: self.tujuan("balek"))
        self.logout_btn.clicked.connect(lambda: self.tujuan("balek"))
        
        

    def tujuan(self, role):
        if role == "main_login":
            self.stackedWidget.setCurrentIndex(1)
        elif role == "main_register":
            self.stackedWidget.setCurrentIndex(2)
        elif role == "balek":
            self.stackedWidget.setCurrentIndex(0)

    def login(self, role):
        if role == "login":
            user = self.ledit_user1.text()
            passw = self.ledit_pass1.text()
            try:
                data = validasi.loginuser(user, passw)
                self.label_9.setText(f"Selamat datang, {user} ")
                self.tabung_btn.clicked.connect(lambda: self.tabung(data))
                self.tarik_btn.clicked.connect(lambda: self.tarik(data))
                self.saldo_lbl.setText(str(data["saldo"]) + ",00")
                self.riwayat_btn.clicked.connect(lambda: self.riwayat(data))
                self.hapusriwayat_btn.clicked.connect(lambda: transaksi.hapusriwayat(data))
                self.stackedWidget.setCurrentIndex(3)
            except:
                msg = QMessageBox()
                msg.setText("username atau password salah")
                msg.setWindowTitle("Peringatan")
                msg.exec_()

        if role == "register":
            user = self.ledit_user.text()
            passw = self.ledit_pass.text()
            if user:
                if passw:
                    data = validasi.register(user, passw)
                    self.stackedWidget.setCurrentIndex(0)
                else:
                    msg = QMessageBox()
                    msg.setText("Tidak boleh kosong")
                    msg.setWindowTitle("Peringatan")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("Tidak boleh kosong")
                msg.setWindowTitle("Peringatan")
                msg.exec_()

    def tabung(self, user):
        deposit = self.ledit_tabung.text()
        try:
            data = transaksi.tabung(deposit, user)
            self.saldo_lbl.setText(str(data) + ",00")
        except:
            msg = QMessageBox()
            msg.setText("Masukan nominal")
            msg.setWindowTitle("Peringatan")
            msg.exec_()
    def tarik(self, user):
        try:
            deposit = self.ledit_tabung.text()
            data = transaksi.tarik(deposit, user)
            self.saldo_lbl.setText(str(data) + ",00")
        except:
            msg = QMessageBox()
            msg.setText("Masukan nominal")
            msg.setWindowTitle("Peringatan")
            msg.exec_()
    def riwayat(self, user):
        msg = QMessageBox()
        msg.setText(transaksi.riwayat(user))
        msg.setWindowTitle("Riwayat transaksi")
        msg.exec()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
