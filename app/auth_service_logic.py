class auth_service:
    def __init__(self, repository):
        self.repository = repository

    def login(self, username, password):
        account_data = self.repository.verify_login(username, password)
        if account_data != None:
            from model.player import player_logic
            return player_logic(account_data)