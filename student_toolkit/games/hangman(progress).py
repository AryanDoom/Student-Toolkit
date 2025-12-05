import tkinter as tk
import random

sentence = "Python makes programming fun"
word_list = sentence.upper().split()
secret_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x600")
root.config(bg="#1e1e2e")

def display_word():
    result = ""
    for letter in secret_word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    word_label.config(text=result)

def check_letter():
    global wrong_guesses
    letter = entry.get().upper()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        return

    if letter in guessed_letters:
        return

    guessed_letters.append(letter)

    if letter in secret_word:
        display_word()
        check_win()
    else:
        wrong_guesses += 1
        hangman_label.config(text=hangman_stages[wrong_guesses])
        if wrong_guesses == max_wrong:
            result_label.config(text=f"❌ You Lost! Word was: {secret_word}", fg="red")

def check_win():
    for letter in secret_word:
        if letter not in guessed_letters:
            return
    result_label.config(text="🎉 YOU WON! 🎉", fg="lime")
    start_celebration()

def start_celebration():
    canvas.pack()
    animate()

def animate():
    canvas.delete("all")
    for _ in range(30):
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        size = random.randint(5, 15)
        canvas.create_oval(x, y, x+size, y+size, fill=random.choice(["red","yellow","cyan","lime","orange"]))
    root.after(200, animate)

title = tk.Label(root, text="🎯 HANGMAN GAME 🎯", font=("Arial", 24, "bold"), bg="#1e1e2e", fg="cyan")
title.pack(pady=10)

sentence_label = tk.Label(root, text=f"Sentence Hint:\n{sentence}", font=("Arial", 12), bg="#1e1e2e", fg="white")
sentence_label.pack(pady=5)

word_label = tk.Label(root, font=("Courier", 28, "bold"), bg="#1e1e2e", fg="yellow")
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18), justify="center")
entry.pack(pady=10)

guess_btn = tk.Button(root, text="Guess Letter", font=("Arial", 14), command=check_letter)
guess_btn.pack(pady=5)

result_label = tk.Label(root, font=("Arial", 18, "bold"), bg="#1e1e2e")
result_label.pack(pady=20)

hangman_stages = [
    "",
    "😐",
    "😟",
    "😨",
    "😰",
    "😵",
    "💀"
]

hangman_label = tk.Label(root, font=("Arial", 60), bg="#1e1e2e", fg="white")
hangman_label.pack(pady=10)

canvas = tk.Canvas(root, width=600, height=200, bg="#1e1e2e", highlightthickness=0)

display_word()
root.mainloop()