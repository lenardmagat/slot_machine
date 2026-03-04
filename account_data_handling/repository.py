import os
import json

class player_repository:
    FILE = "players.json"
    def load(self):
        with open(self.FILE, "r") as f:
            data = json.load(f)
        return data
    
    def save(self, player):
        try:
            with open(self.FILE, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        data[player.username] = {}
        data[player.username]["credits"] = player.credits
        with open(self.FILE, "w") as f:
            json.dump(data, f, indent = 4)

    def verify_login(self, username, password):
        with open(self.FILE, "r") as f:
            data = json.load(f)
        if username not in data or password != data[username][password]:
            return None
        return {
                "username" : username,
                "credits" : data[username]["credits"]
                }