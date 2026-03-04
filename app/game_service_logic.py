from model.slot_machine_logic import slot_machine
class game_service:
    def __init__(self, player, repository):
        self.player = player
        self.repository = repository
        self.machine = slot_machine()

    def play_round(self, bet):
        self.player.deduct(bet)
        result = self.machine.slot_machine_spin()
        payout = self.machine.calculate_payout(result, bet)
        self.player.add(payout)
        self.repository.save(self.player)