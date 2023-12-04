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
import json

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("cicakterbang.ui", self)
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
            self.transaksipage_btn.clicked.connect(lambda: self.pages("transaksi", user))
            self.riwayatpage_btn.clicked.connect(lambda: self.pages("riwayat", user)) 
            self.hapusriwayat_btn.clicked.connect(lambda: self.hapus(user))  
            try:
                data = validasi.loginuser(user, passw)
                if data:
                    self.label_9.setText(f"Selamat datang, {user} ")
                    self.stackedWidget.setCurrentIndex(3)
                    self.tabung_btn.clicked.connect(lambda: self.tabung(data))
                    self.tarik_btn.clicked.connect(lambda: self.tarik(data))
                    self.saldo_lbl.setText(str(data["saldo"]))
                    # self.riwayat_btn.clicked.connect(lambda: self.riwayat(data))
                    
                    
        
            except:
                print(":P")
            

    def tabung(self, user):
        deposit = self.ledit_tabung.text()
        try:
            data = transaksi.tabung(deposit, user)
            self.saldo_lbl.setText(str(data))
        except:
            print("mau berapa")
    def tarik(self, user):
        try:
            deposit = self.ledit_tabung.text()
            data = transaksi.tarik(deposit, user)
            self.saldo_lbl.setText(str(data))
        except:
            print("mau berapa cok")

    def pages(self, role, user):
        if role == "riwayat":
            self.stackedWidget_2.setCurrentIndex(1)
            rwyt = transaksi.riwayat(user)
            self.label_13.setText(rwyt)
        elif role == "transaksi":
            self.stackedWidget_2.setCurrentIndex(0)
    
    def hapus(self, user):
        transaksi.hapusriwayat(user)
        rwyt = transaksi.riwayat(user)
        self.label_13.setText(rwyt)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
