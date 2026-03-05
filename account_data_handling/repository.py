import os
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
        data[player["username"]][player["password"]] = player["password"]
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