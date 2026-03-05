from display.main_display import main_window
from mains import login_main, create_account
def main():
    while True:
        user_choice = main_window().login_screen()
        match user_choice:
            case "L":
                login_main.main_logic()
            case "C":
                create_account.create_user()
            case _:
                pass
            
if __name__ == "__main__":
    main()