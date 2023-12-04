import json
from datetime import datetime

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
                print("minus")
            
            return a["saldo"]
    file.close()
def riwayat(user):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == user:
            hist = ""
            for b in a["riwayat"]:
                hist += f"{b}\n"
            return hist
def hapusriwayat(user):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == user:
            a["riwayat"] = []
    with open("users.json", "w") as file:
        json.dump(data, file, indent=3)
    file.close()