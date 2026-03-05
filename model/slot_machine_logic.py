import random
from account_data_handling.repository import player_repository
import time
SLOT_MACHINE_REEL = ["🍒"] * 5 + ["💎"] *2 + ["7"] *3

class slot_machine:        
    def slot_machine_spin(self):
        slot_machine_spin_result = []
        for i in range(3):
            time.sleep(2 * i)
            temp_result = random.choice(SLOT_MACHINE_REEL)
            slot_machine_spin_result.append(temp_result)
            print(temp_result, end= "  ")
        print("")
        print(slot_machine_spin_result)
        return slot_machine_spin_result

    def calculate_payout(self, spin_results, user_bet):
        if spin_results.count("🍒") == len(spin_results):
            payout = int(user_bet) * 3
            print("YOU WIN x3!")
            return payout
        elif spin_results.count("💎") == len(spin_results):
            payout = int(user_bet) * 100
            print("JACK POT!")
            return payout
        elif spin_results.count("7") == len(spin_results):
            payout = int(user_bet) * 10
            print("YOU WIN x10!")
            return payout
        elif spin_results.count("🍒") == 2:
            payout = int(user_bet)
            print("Bet return")
            return payout
        elif spin_results.count("💎") == 2:
            payout = int(user_bet) * 5
            print("YOU WIN x5!")
            return payout
        elif spin_results.count("7") == 2:
            payout = int(user_bet)
            print("Bet return")
            return payout
        else:
            payout = 0
            return payout

       
            
            
