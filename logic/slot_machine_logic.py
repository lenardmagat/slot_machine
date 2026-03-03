import random
SLOT_MACHINE_REEL = ["🍒"] * 7 + ["💎"] + ["7️⃣"]*2

class slot_machine:
    def place_bet(self):
        while True:
            user_bet = input("Place your bet: ")
            if not user_bet.isdigit():
                continue
            return user_bet
        
    def slot_machine_spin(self):
        slot_machine_spin_result = []
        for i in range(3):
            temp_result = random.choice(SLOT_MACHINE_REEL)
            slot_machine_spin_result.append(temp_result)
        return slot_machine_spin_result

    def bet_result(self, spin_results, user_bet):
        if spin_results.count("🍒") == len(spin_results):
            user_bet = int(user_bet) * 3
            return user_bet
        
        if spin_results.count("💎") == len(spin_results):
            user_bet = int(user_bet) * 10
            return user_bet
        
        if spin_results.count("7️⃣") == len(spin_results):
            user_bet = int(user_bet) * 5
            return user_bet
