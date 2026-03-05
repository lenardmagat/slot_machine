from model import player, slot_machine_logic
class main_controller:
    def __init__(self, user_data):
        self.user_data = user_data

    def betting(self):
        while True:
            bet_amount = player.player_logic(self.user_data).bet()
            slot_machine_result = slot_machine_logic.slot_machine().slot_machine_spin()
            pay_out = slot_machine_logic.slot_machine().calculate_payout(slot_machine_result, bet_amount)
            if(pay_out > 0):
                self.user_data["credits"] += pay_out
                
            else:
                print("Better luck nextime!")