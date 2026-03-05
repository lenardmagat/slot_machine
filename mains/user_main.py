from display.main_display import main_window as screen
from .user_main_controller import main_controller
from model.player import player_logic
def user_main(user_data):
    while True:
        user_choice = screen().main_screen(user_data["credits"])
        match user_choice:
            case "B":
                main_controller(user_data).betting()
            case "I":
                player_logic(user_data).add()
            case "O":
                player_logic(user_data).deduct()
            case _:
                pass

    