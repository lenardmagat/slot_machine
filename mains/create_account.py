from account_data_handling.repository import player_repository
from helper.utils import function_helper

def create_user():
    while True:
        username = input("Enter your username: ")
        verify_username_exist = player_repository().verify_username(username)
        if not verify_username_exist:
            print("Username already exist")
            continue
        
        password = function_helper().input_password()
        re_enter_pass = function_helper().input_password()
        if password == re_enter_pass:
            player_repository().create_account(username, password)
            print("suces creating an account")
            return
        
        else:
            print("password does not match")
            continue
        