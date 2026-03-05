from display.main_display import main_window as screen
from .user_main_controller import main_controller
def user_main(user_data):
    while True:
        user_choice = screen().main_screen()
        match user_choice:
            case "B":
                main_controller(user_data).betting()
            case "I":
                pass
            case "O":
                pass
            case _:
                pass

    