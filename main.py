import sys
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi
# from qfluentwidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import validasi

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
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
        elif role == "login":
            username = self.ledit_user.text()
            password = self.ledit_pass.text()
            try:
                data = validasi.loginuser(username, password)
                if data:
                    self.label_9.setText(f"Selamat datang, {data} ")
                    self.stackedWidget.setCurrentIndex(3)
            except:
                print(":P")
            # self.stackedWidget.setCurrentIndex(3)
        elif role == "balek":
            self.stackedWidget.setCurrentIndex(0)

    def login(self, role):
        if role == "login":
            user = self.ledit_user1.text()
            passw = self.ledit_pass1.text()
            try:
                data = validasi.loginuser(user, passw)
                if data:
                    self.label_9.setText(f"Selamat datang, {user} ")
                    self.stackedWidget.setCurrentIndex(3)
            except:
                print(":P")
        if role == "register":
            user = self.ledit_user.text()
            passw = self.ledit_pass.text()
            data = validasi.register(user, passw)
            self.label_9.setText(f"Selamat datang, {user}")
            self.stackedWidget.setCurrentIndex(3)

    def tabung(self, selected):
        with open("users.json", "r") as file:
            data = json.load(file)
        tabung_result = self.ledit_tabung(selected)
        update_data = self.update_data(data, tabung_result)
        with open("users.json", "w") as file:
            json.dump(update_data, file, indent=2)

    
    # def ledit_tabung(self, selected):
    #     if selected

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
