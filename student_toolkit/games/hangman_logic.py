import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import csv
import os
from PIL import Image,ImageTk


def open_hangman(root):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    base = os.path.dirname(__file__)  

    doom_img=None

    def draw_doom_mask():
        global doom_img

        img = Image.open(os.path.join(base,"doom_mask4.png")).convert("RGBA")

        img = img.resize((36, 55), Image.LANCZOS)

        doom_img = ImageTk.PhotoImage(img)

        canvas.create_image(100, 62, image=doom_img)


    solutions_path = os.path.join(base, "words_250000_train.csv")

    with open(solutions_path, "r") as f:
        WORDS = [row1[0].upper() for row1 in csv.reader(f)]
    SOLUTION = random.choice(WORDS)
    while len(SOLUTION)>6 or len(SOLUTION)<3 :
        SOLUTION = random.choice(WORDS)

    print(SOLUTION)

    def initialize_game():
        word = SOLUTION.lower()
        display = ["_"] * len(word)
        guessed = set()
        attempts = 6
        return word,display, guessed, attempts

    def check_guess(word, display, guessed, guess):
        if guess in guessed:
            return False

        guessed.add(guess)
        correct = False
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
                correct = True
        return correct

    def redraw():
        canvas.delete("all")
        draw_gallows()
        draw_stickman(attempts)

    def is_won(display):
        return "_" not in display

    def draw_gallows():
        canvas.create_line(20, 200, 120, 200, width=2)   # base
        canvas.create_line(40, 200, 40, 20, width=2)     # pole
        canvas.create_line(40, 20, 100, 20, width=2)     # top bar
        canvas.create_line(100, 20, 100, 35, width=2)    # rope


    def draw_stickman(attempts):

        if attempts <= 5:
            #canvas.create_oval(80, 35, 120, 75, width=2, fill="#0F5F0C")
            draw_doom_mask()

        
        if attempts <= 4:
            canvas.create_line(100, 75, 100, 135, width=2, fill="#0F5F0C")

        if attempts <= 3:
            canvas.create_line(100, 95, 70, 115, width=2, fill="#0F5F0C")

        if attempts <= 2:
            canvas.create_line(100, 95, 130, 115, width=2, fill="#0F5F0C")

        if attempts <= 1:
            canvas.create_line(100, 135, 75, 175, width=2, fill="#0F5F0C")

        if attempts <= 0:
            canvas.create_line(100, 135, 125, 175, width=2, fill="#0F5F0C")




    def update_display():
        word_label.configure(text=" ".join(display))
        attempts_label.configure(text=f"Attempts left: {attempts}")
        guessed_label.configure(text="Guessed: " + " ".join(sorted(guessed_letters)))

    def handle_key(event):
        global attempts

        guess = event.char.lower()
        if not guess.isalpha() or len(guess) != 1:
            return

        correct = check_guess(word, display, guessed_letters, guess)

        if not correct:
            attempts -= 1
            draw_stickman(attempts)

        update_display()

        if is_won(display):
            messagebox.showinfo("Hangman","You won!")
            hangman_window.destroy()

        if attempts == 0:
            messagebox.showinfo("Hangman", f"Game Over!\nWord was: {word}")
            hangman_window.destroy()


    # ---------- INIT ----------
    word, display, guessed_letters, attempts = initialize_game()
    hangman_window = ctk.CTk()
    hangman_window.title("Hangman with Gallows")
    hangman_window.geometry("540x380")
    hangman_window.configure(fg_colour="#000000")

    toplabel = ctk.CTkFrame(hangman_window,fg_color="#000000",corner_radius=20)
    toplabel.pack(pady=4,padx=20,fill="x")

    title = ctk.CTkLabel(toplabel,text="HANGMAN",font=("Agency FB", 26, "bold"))
    title.pack(pady=8)


    content = ctk.CTkFrame(hangman_window,fg_color="#000000",corner_radius=20)
    content.pack(side="left", fill="both", expand=True, padx=20, pady=7)

    word_label = ctk.CTkLabel(content,text=" ".join(display),font=("Agency FB", 30))
    word_label.pack(pady=12)

    attempts_label = ctk.CTkLabel(content,text=f"Attempts left: {attempts}",font=("Agency FB", 15))
    attempts_label.pack()

    guessed_label = ctk.CTkLabel(content,text="Guessed: ",font=("Agency FB",15))
    guessed_label.pack(pady=6)

    canvas = tk.Canvas(content,width=160,height=220,bg="#353434",highlightthickness=0)
    canvas.pack(anchor="center", padx=20)

    draw_gallows()
    redraw()


    hangman_window.bind("<Key>", handle_key)
    hangman_window.focus_set()
    hangman_window.mainloop()
open_hangman