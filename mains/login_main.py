from display.main_display import main_window
from helper.utils import function_helper 
from account_data_handling.repository import player_repository
from . import user_main
screen = main_window()
def main_logic():
    while True:
        username = input("Enter your username: ")
        password = function_helper().input_password()
        user_data = player_repository().verify_login(username, password)
        if(user_data != None):
            user_main.user_main(user_data)

        else:
            continue