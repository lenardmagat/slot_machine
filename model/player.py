from account_data_handling.repository import player_repository
class player_logic:
    def __init__(self, account_data):
        self.account_data = account_data


    def bet(self):
        while True:
            amount = input("Enter amount you want to bet [Q] to quit: ")
            if amount == "Q" or amount == "q":
                return None
            
            if not amount.isdigit() or int(amount) > self.account_data["credits"] or  int(amount) < 0 or int(amount) == 0:
                print("Invalid amount!")
                continue

            self.account_data["credits"] -=  int(amount)
            print("You success fully bet %s" %amount)
            player_repository().save(self.account_data)
            return amount

    def add(self):
        while True:
            amount = input("Enter the amount you want to cash in [Q] to quit: ")
            if amount == "Q" or amount == "q":
                return None

            if not amount.isdigit() or int(amount) < 0:
                print("invalid amount")
                continue

            self.account_data["credits"] += int(amount)
            player_repository().save(self.account_data)
            print("You successfully cash in %d. Total credits %d" %(int(amount), self.account_data["credits"]))
            return
        
    def deduct(self):
        while True:
            amount = input("Enter the amount you want to cash out [Q] to quit: ")
            if amount == "Q" or amount == "q":
                return None
            
            if not amount.isdigit() or int(amount) > self.account_data["credits"] or  int(amount) < 0 or int(amount) == 0:
                print("Invalid amount!")
                continue

            self.account_data["credits"] -=  int(amount)
            print("You success fully cash out %s" %amount)
            player_repository().save(self.account_data)
            return