class player_logic:
    def __init__(self,account_data):
        self.username = account_data["username"]
        self.credits = int(account_data["credits"])

    def deduct(self, amount):
        if amount > self.credits or amount < 0:
            raise ValueError("Invalid ammount")
        self.credits  -= amount

    def add(self, amount):
        if amount < 0:
            raise ValueError("Invalid ammount")
        self.credits  += amount