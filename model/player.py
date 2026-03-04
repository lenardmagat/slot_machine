class player_logic:
    def __init__(self, username, credits):
        self.usernmae = username
        self.credits = credits

    def deduct(self, amount):
        if amount > self.credits | amount < 0:
            raise ValueError("Invalid ammount")
        self.credits -= amount

    def add(self, amount):
        if amount < 0:
            raise ValueError("Invalid ammount")
        self.credits += amount