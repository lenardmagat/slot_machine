class auth_service:
    def __init__(self, repository):
        self.repository = repository

    def login(self, username, password):
        accounts_data = self.repository.load()
        if username not in accounts_data:
            raise ValueError("invalid credential!")
        if password != accounts_data[username]:
            raise ValueError("Incorrect Password")
        from model.player import player_logic
        return player_logic(username, accounts_data["credits"])