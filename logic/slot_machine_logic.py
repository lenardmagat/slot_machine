import random
SLOT_MACHINE_REEL = ["🍒"] * 6 + ["🍋"] * 4 + ["💎"] + ["7️⃣"]*2 + ["🔔"]*3

class slot_machine:
    def place_bet(self):
        while True:
            user_bet = input("Place your bet: ")
            if not user_bet.isdigit():
                continue
            return user_bet
        
    def slot_machine_spin(self):
        slot_machine_spin_result = []
        for i in range(5):
            temp_result = random.choice(SLOT_MACHINE_REEL)
            slot_machine_spin_result.append(temp_result)
        return slot_machine_spin_result

    def bet_result(self):
        pass
