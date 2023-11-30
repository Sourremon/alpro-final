import json
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

def tabung(deposit, user):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == user["username"]:
            saldo = a["saldo"]
            saldo += int(deposit)
            a["saldo"] = saldo
            current_time = datetime.now()
            waktu = current_time.strftime("%d-%m-%Y, %H:%M:%S")
            a["riwayat"].append(f"deposit + Rp {deposit}, {waktu}")
            with open("users.json", "w") as file:
                json.dump(data, file, indent=3)
            
            return a["saldo"]
    file.close()

def tarik(deposit, user):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == user["username"]:
            saldo = a["saldo"]
            saldo -= int(deposit)
            if saldo >= 0:
                a["saldo"] = saldo
                current_time = datetime.now()
                waktu = current_time.strftime("%d-%m-%Y, %H:%M:%S")
                a["riwayat"].append(f"tarik - Rp {deposit}, {waktu}")
                with open("users.json", "w") as file:
                    json.dump(data, file, indent=3)
            else:
                msg = QMessageBox()
                msg.setText("Tidak bisa minus")
                msg.setWindowTitle("Peringatan")
                msg.exec_()
            
            return a["saldo"]
    file.close()
def riwayat(user):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == user["username"]:
            hist = ""
            for b in a["riwayat"]:
                hist += f"\n{b}"
            return hist
def hapusriwayat(user):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == user["username"]:
            a["riwayat"] = []
    with open("users.json", "w") as file:
        json.dump(data, file, indent=3)
    file.close()