class slot_machine:
    def place_bet(self):
        while True:
            user_bet = input("Place your bet: ")
            if not user_bet.isdigit():
                continue
            return user_bet

    def bet_result(self):
        pass
