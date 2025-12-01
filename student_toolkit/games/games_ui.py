import customtkinter as ctk
from games.wordle_logic import open_wordle
from games.leetcode_logic import open_leetcode


def open_game(root):
    game_window = ctk.CTkToplevel(root)
    game_window.title("Brain Teasers")
    game_window.geometry("600x400")
    game_window.configure(fg_color="#111111")

    ctk.CTkLabel(game_window, text="Brain Teasers", font=("Agency FB", 30, "bold"),text_color="#ffffff").pack(pady=20)

    game_frame = ctk.CTkFrame(game_window,fg_color="#1f1f1f",corner_radius=18)
    game_frame.pack(pady=10, padx=20, fill="both", expand=True)

    btn_style = {"corner_radius": 18,"height": 110,"width": 240,"font": ("Agency FB", 20, "bold"),"fg_color": "#080707","hover_color": "#0E3C10","text_color": "#ffffff"}

    ctk.CTkButton(game_frame, text="Wordle", command=lambda: open_wordle(game_window),**btn_style).grid(row=0, column=0, padx=20, pady=20)

    ctk.CTkButton(game_frame, text="DSA Questions", command=lambda:open_leetcode(game_window),**btn_style).grid(row=0, column=1, padx=20, pady=20)

    
