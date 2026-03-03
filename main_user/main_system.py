from logic.slot_machine_logic import slot_machine

def main_entry():
    machine = slot_machine()
    while True:
        user_bet = machine.place_bet()
        print(f"You bet: {user_bet}")
        slot_machine_result = machine.slot_machine_spin()
        print(slot_machine_result)
        bet_reward = machine.bet_result(slot_machine_result, user_bet)
        if bet_reward is None:
            print("Better Luck Next Time!")
        else:
            print(f"You win: {bet_reward}")