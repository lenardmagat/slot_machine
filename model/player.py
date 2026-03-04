class player_logic:
    def __init__(self,account_data):
        self.account_data = account_data
        self.credits = credits

    def deduct(self, amount):
        if amount > self.account_data["credits"] | amount < 0:
            raise ValueError("Invalid ammount")
        self.account_data[credits] -= amount

    def add(self, amount):
        if amount < 0:
            raise ValueError("Invalid ammount")
        self.account_data["credits"] += amount