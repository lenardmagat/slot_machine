# gui/main_window.py
import tkinter as tk
from model.slot_machine_logic import slot_machine
from app.game_service_logic import game_service
from model.player import player_logic
from account_data_handling.repository import player_repository

def start_main_window():
    # Backend setup
    player_data = {
        "username" : "test",
        "credits" : 100
        }
    player = player_logic(player_data)
    repo = player_repository()
    service = game_service(player, repo)

    # GUI setup
    root = tk.Tk()
    root.title("Slot Machine")

    # Credits label
    credits_label = tk.Label(root, text=f"Credits: {player.credits}")
    credits_label.pack()

    # Reel labels
    reel_labels = [tk.Label(root, text="❓") for _ in range(3)]
    for lbl in reel_labels:
        lbl.pack(side=tk.LEFT)

    # Bet entry
    bet_entry = tk.Entry(root)
    bet_entry.pack()

    # Message label
    message_label = tk.Label(root, text="")
    message_label.pack()

    # Spin button
    def spin():
        try:
            bet = int(bet_entry.get())
        except ValueError:
            message_label.config(text="Invalid bet!")
            return
        result, payout, credits = service.play_round(bet)
        for lbl, symbol in zip(reel_labels, result):
            lbl.config(text=symbol)
        credits_label.config(text=f"Credits: {credits}")
        message_label.config(text=f"You won {payout}!")

    spin_button = tk.Button(root, text="Spin", command=spin)
    spin_button.pack()

    # Start GUI
    root.mainloop()