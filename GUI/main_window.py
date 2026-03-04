# gui/main_window.py
import tkinter as tk
from model.slot_machine_logic import slot_machine
from app.game_service_logic import game_service
from model.player import player_logic
from account_data_handling.repository import player_repository

def start_main_window():
    repo = player_repository()
    players_data = repo.load()
    player_data = {
        "username" : "test",
        "credits" : players_data["test"]["credits"]
    }
    player = player_logic(player_data)
    service = game_service(player, repo)
    root = tk.Tk()
    root.title("Slot Machine")
    credits_label = tk.Label(root, text=f"Credits: {player.credits}")
    credits_label.pack()
    reel_labels = [tk.Label(root, text="❓") for _ in range(3)]
    for lbl in reel_labels:
        lbl.pack(side=tk.LEFT)
    bet_entry = tk.Entry(root)
    bet_entry.pack()
    message_label = tk.Label(root, text="")
    message_label.pack()

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
    root.mainloop()