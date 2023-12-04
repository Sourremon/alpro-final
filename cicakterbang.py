# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cicakterbang.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 413)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 761, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(240, 80, 291, 100))
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(217, 184, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.login_btn = QtWidgets.QPushButton(self.page)
        self.login_btn.setGeometry(QtCore.QRect(240, 290, 75, 23))
        self.login_btn.setObjectName("login_btn")
        self.registe_btn = QtWidgets.QPushButton(self.page)
        self.registe_btn.setGeometry(QtCore.QRect(440, 290, 75, 23))
        self.registe_btn.setObjectName("registe_btn")
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 771, 411))
        self.frame_4.setStyleSheet("background-color: rgb(86, 98, 113);\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.login_btn.raise_()
        self.registe_btn.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.login_btn2 = QtWidgets.QPushButton(self.page_2)
        self.login_btn2.setGeometry(QtCore.QRect(360, 260, 75, 23))
        self.login_btn2.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"\n"
"")
        self.login_btn2.setObjectName("login_btn2")
        self.ledit_pass1 = QtWidgets.QLineEdit(self.page_2)
        self.ledit_pass1.setGeometry(QtCore.QRect(340, 200, 113, 20))
        self.ledit_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ledit_pass1.setObjectName("ledit_pass1")
        self.kembali = QtWidgets.QPushButton(self.page_2)
        self.kembali.setGeometry(QtCore.QRect(360, 290, 75, 23))
        self.kembali.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"")
        self.kembali.setObjectName("kembali")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(370, 80, 47, 13))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.ledit_user1 = QtWidgets.QLineEdit(self.page_2)
        self.ledit_user1.setGeometry(QtCore.QRect(340, 110, 113, 20))
        self.ledit_user1.setObjectName("ledit_user1")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(370, 170, 47, 13))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(380, 40, 47, 13))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 771, 411))
        self.frame_3.setStyleSheet("background-color: rgb(86, 98, 113);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.login_btn2.raise_()
        self.ledit_pass1.raise_()
        self.kembali.raise_()
        self.label_3.raise_()
        self.ledit_user1.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(370, 40, 47, 13))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 771, 411))
        self.frame_2.setStyleSheet("background-color: rgb(86, 98, 113);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ledit_user1_2 = QtWidgets.QLineEdit(self.frame_2)
        self.ledit_user1_2.setGeometry(QtCore.QRect(340, 110, 113, 20))
        self.ledit_user1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ledit_user1_2.setObjectName("ledit_user1_2")
        self.ledit_pass1_2 = QtWidgets.QLineEdit(self.frame_2)
        self.ledit_pass1_2.setGeometry(QtCore.QRect(340, 200, 113, 20))
        self.ledit_pass1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ledit_pass1_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ledit_pass1_2.setObjectName("ledit_pass1_2")
        self.kembali_2 = QtWidgets.QPushButton(self.frame_2)
        self.kembali_2.setGeometry(QtCore.QRect(360, 290, 75, 23))
        self.kembali_2.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"")
        self.kembali_2.setObjectName("kembali_2")
        self.register_btn2 = QtWidgets.QPushButton(self.frame_2)
        self.register_btn2.setGeometry(QtCore.QRect(360, 260, 75, 23))
        self.register_btn2.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"")
        self.register_btn2.setObjectName("register_btn2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(350, 80, 101, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(340, 170, 121, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.frame_2.raise_()
        self.label_6.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame = QtWidgets.QFrame(self.page_4)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 771, 411))
        self.frame.setStyleSheet("background-color: rgb(86, 98, 113);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(10, 0, 120, 411))
        self.frame_5.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(30, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_15.setFont(font)
        self.label_15.setMouseTracking(True)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setLineWidth(0)
        self.label_15.setMidLineWidth(0)
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.widget = QtWidgets.QWidget(self.frame_5)
        self.widget.setGeometry(QtCore.QRect(10, 80, 101, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.transaksipage_btn = QtWidgets.QPushButton(self.widget)
        self.transaksipage_btn.setMouseTracking(True)
        self.transaksipage_btn.setStyleSheet("background-color: rgb(146, 146, 217);")
        self.transaksipage_btn.setObjectName("transaksipage_btn")
        self.verticalLayout.addWidget(self.transaksipage_btn)
        self.riwayatpage_btn = QtWidgets.QPushButton(self.widget)
        self.riwayatpage_btn.setMouseTracking(True)
        self.riwayatpage_btn.setStyleSheet("background-color: rgb(146, 146, 217);")
        self.riwayatpage_btn.setObjectName("riwayatpage_btn")
        self.verticalLayout.addWidget(self.riwayatpage_btn)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet("background-color: rgb(146, 146, 217);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_2.setGeometry(QtCore.QRect(140, 10, 621, 391))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_6 = QtWidgets.QFrame(self.page_7)
        self.frame_6.setGeometry(QtCore.QRect(50, 110, 501, 251))
        self.frame_6.setMouseTracking(True)
        self.frame_6.setStyleSheet("background-color: rgb(117, 117, 173);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.ledit_tabung = QtWidgets.QLineEdit(self.frame_6)
        self.ledit_tabung.setGeometry(QtCore.QRect(150, 70, 201, 20))
        self.ledit_tabung.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"")
        self.ledit_tabung.setObjectName("ledit_tabung")
        self.tarik_btn = QtWidgets.QPushButton(self.frame_6)
        self.tarik_btn.setGeometry(QtCore.QRect(260, 130, 75, 23))
        self.tarik_btn.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"")
        self.tarik_btn.setObjectName("tarik_btn")
        self.tabung_btn = QtWidgets.QPushButton(self.frame_6)
        self.tabung_btn.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.tabung_btn.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"\n"
"")
        self.tabung_btn.setObjectName("tabung_btn")
        self.label_9 = QtWidgets.QLabel(self.page_7)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.page_7)
        self.label_12.setGeometry(QtCore.QRect(0, 60, 111, 41))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.saldo_lbl = QtWidgets.QLabel(self.page_7)
        self.saldo_lbl.setGeometry(QtCore.QRect(120, 60, 111, 41))
        self.saldo_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.saldo_lbl.setObjectName("saldo_lbl")
        self.label_9.raise_()
        self.frame_6.raise_()
        self.label_12.raise_()
        self.saldo_lbl.raise_()
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_13 = QtWidgets.QLabel(self.page_8)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 581, 281))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_8)
        self.label_14.setGeometry(QtCore.QRect(0, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.hapusriwayat_btn = QtWidgets.QPushButton(self.page_8)
        self.hapusriwayat_btn.setGeometry(QtCore.QRect(520, 360, 80, 23))
        self.hapusriwayat_btn.setStyleSheet("background-color: rgb(204, 255, 185);\n"
"")
        self.hapusriwayat_btn.setObjectName("hapusriwayat_btn")
        self.stackedWidget_2.addWidget(self.page_8)
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "MoMa"))
        self.label_2.setText(_translate("Form", "Money Manager in an app"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.registe_btn.setText(_translate("Form", "Register"))
        self.login_btn2.setText(_translate("Form", "Login"))
        self.login_btn2.setShortcut(_translate("Form", "Ctrl+S"))
        self.kembali.setText(_translate("Form", "Kembali"))
        self.label_3.setText(_translate("Form", "Username"))
        self.label_4.setText(_translate("Form", "Password"))
        self.label_5.setText(_translate("Form", "Login"))
        self.label_6.setText(_translate("Form", "Register"))
        self.kembali_2.setText(_translate("Form", "Kembali"))
        self.register_btn2.setText(_translate("Form", "Sign up"))
        self.label_8.setText(_translate("Form", "Masukan Username"))
        self.label_7.setText(_translate("Form", "Masukan password baru"))
        self.label_15.setText(_translate("Form", "MM"))
        self.transaksipage_btn.setText(_translate("Form", "Transaksi"))
        self.riwayatpage_btn.setText(_translate("Form", "Riwayat"))
        self.pushButton_3.setText(_translate("Form", "Logout"))
        self.tarik_btn.setText(_translate("Form", "Tarik"))
        self.tabung_btn.setText(_translate("Form", "Tabung"))
        self.label_9.setText(_translate("Form", "Selamat datang, user"))
        self.label_12.setText(_translate("Form", "saldo anda saat ini : Rp"))
        self.saldo_lbl.setText(_translate("Form", "0,00"))
        self.label_13.setText(_translate("Form", "TextLabel"))
        self.label_14.setText(_translate("Form", "Riwayat Transaksi"))
        self.hapusriwayat_btn.setText(_translate("Form", "Hapus Riwayat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
