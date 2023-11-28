import json
file = open("users.json", "r")
data = json.load(file)

def loginuser(username, password):
        for a in data["akun"]:
            if a["username"] == username:
                if a["password"] == password:
                    return a
            else:
                return IndexError
            
def register(username, password):
    new_acc = {"username": str(username),
                "password": str(password)}
    
    with open("users.json", "r") as file:
        data = json.load(file)

    data["akun"].append(new_acc)

    with open("users.json", "w") as file:
        json.dump(data, file, indent=3)
    file.close()
          
file.close()