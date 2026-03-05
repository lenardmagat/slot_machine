from account_data_handling.repository import player_repository
def create_user():
    while True:
        username = input("Enter your username: ")
        verify = player_repository().verify_username(username)
        if not verify:
            print("Username already exist")
            continue
        
        password = input("Enter your password: ")
        re_enter_pass = input("Re-enter your password: ")
        if password == re_enter_pass:
            player_repository().create_account(username, password)
            print("suces creating an account")
            return
        
        else:
            print("password does not match")
            continue
        