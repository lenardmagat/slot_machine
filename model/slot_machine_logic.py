import random
SLOT_MACHINE_REEL = ["🍒"] * 5 + ["💎"] *2 + ["7️⃣"]*3

class slot_machine:        
    def slot_machine_spin(self):
        slot_machine_spin_result = []
        for i in range(3):
            temp_result = random.choice(SLOT_MACHINE_REEL)
            slot_machine_spin_result.append(temp_result)
        return slot_machine_spin_result

    def calculate_payout(self, spin_results, user_bet):
        if spin_results.count("🍒") == len(spin_results):
            payout = int(user_bet) * 3
            return payout
        
        elif spin_results.count("💎") == len(spin_results):
            payout = int(user_bet) * 100
            return payout
        
        elif spin_results.count("7️⃣") == len(spin_results):
            payout = int(user_bet) * 10
            return payout
        
        else:
            payout = 0
            return payout
            
            
