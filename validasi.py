import json


def loginuser(username, password):
    file = open("users.json", "r")
    data = json.load(file)
    for a in data["akun"]:
        if a["username"] == username:
           if a["password"] == password:
            return a
        file.close()  

def register(username, password):
    file = open("users.json", "r")
    data = json.load(file)
    new_acc = {"username": str(username),
                "password": str(password),
                "saldo": 0,
                "riwayat":[]}
    with open("users.json", "r") as file:
        data = json.load(file)

    data["akun"].append(new_acc)

    with open("users.json", "w") as file:
        json.dump(data, file, indent=3)
    file.close()
          
