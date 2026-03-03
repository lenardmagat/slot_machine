from logic.slot_machine_logic import slot_machine

def main_entry():
    machine = slot_machine()
    while True:
        user_bet = machine.place_bet()
        print(f"You bet: {user_bet}")
