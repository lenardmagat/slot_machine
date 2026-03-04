class player_logic:
    def __init__(self,account_data):
        self.account_data = account_data
        self.credits = int(account_data["credits"])
    def deduct(self, amount):

        if amount > credits or amount < 0:
            raise ValueError("Invalid ammount")
        self.credits  -= amount

    def add(self, amount):
        if amount < 0:
            raise ValueError("Invalid ammount")
        self.credits  += amount