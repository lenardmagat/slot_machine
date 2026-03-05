import json

class player_repository:
    def __init__(self):
        self.FILE = "players.json"

    def load(self):
        with open(self.FILE, "r") as file:
            data = json.load(file)
        return data
    
    def save(self, player):
        try:
            with open(self.FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data[player["username"]] = {}
        data[player["username"]]["password"] = player["password"]
        data[player["username"]]["credits"] = player["credits"]
        with open(self.FILE, "w") as file:
            json.dump(data, file, indent = 4)

    def verify_login(self, username, password):
        with open(self.FILE, "r") as file:
            data = json.load(file)
        if username not in data or password != data[username]["password"]:
            return None
        
        return {
                "username" : username,
                "password" : data[username]["password"],
                "credits" : data[username]["credits"]
                }

    def verify_username(self, username):
        with open(self.FILE, "r") as file:
            data = json.load(file)
        verify = data.get(username, None)
        if verify == None:
            return True
        
        else:
            return False
        
    def create_account(self, username, password):
        account_data = {}
        account_data["username"] = username
        account_data["password"] = password
        account_data["credits"] = 0
        self.save(account_data)