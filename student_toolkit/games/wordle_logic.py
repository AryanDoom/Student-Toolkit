import customtkinter as ctk
import tkinter as tk
import random
import csv


def open_wordle(root):
        #data as to only allow valid words
        with open(r"C:\Users\aryan\OneDrive\Documents\Code\Student-Toolkit\student_toolkit\games\valid_solutions.csv", "r") as f:
            words = [row1[0].upper() for row1 in csv.reader(f)]

        with open(r"C:\Users\aryan\OneDrive\Documents\Code\Student-Toolkit\student_toolkit\games\valid_guesses.csv", "r") as h:
            words_sol = [row2[0].upper() for row2 in csv.reader(h)]    

        SOLUTION = random.choice(words)
        VALID_WORDS = set(words_sol)|set(words)

        ROWS = 6  #predefined number of coloumns and rows
        COLS = 5

        COLOR_CORRECT = "#558e50"
        COLOR_PRESENT = "#c4b572"
        COLOR_ABSENT  = "#787c7e"
        COLOR_EMPTY   = "#232325"

        current_row = 0 #as to traverse through the rows and coloumns
        current_col = 0
        grid = []
        keyboard_buttons = {}

        ctk.set_appearance_mode("dark")
        wordle_window = ctk.CTk()
        wordle_window.title("Wordle")



        msg_label = ctk.CTkLabel(wordle_window, text="", text_color="red")
        msg_label.grid(row=2, column=0, pady=5)

        #building the grid for the letters 
        def build_grid():
            frame = ctk.CTkFrame(wordle_window, fg_color="#000000")
            frame.grid(row=0, column=0, pady=10)

            for r in range(ROWS):
                row_cells = []
                for c in range(COLS):
                    lbl = ctk.CTkLabel(frame, text="", width=60, height=60,corner_radius=6, fg_color=COLOR_EMPTY,font=("Agency FB", 28, "bold"))
                    lbl.grid(row=r, column=c, padx=5, pady=5)
                    row_cells.append(lbl)
                grid.append(row_cells)



        #pressing key on the actual physical keyboard
        def handle_keypress(event):
            ch = event.char.upper()

            if ch.isalpha() and len(ch) == 1:
                press_key(ch)
            elif event.keysym == "Return":
                submit_word()
            elif event.keysym == "BackSpace":
                delete_letter()

        wordle_window.bind("<Key>", handle_keypress)


        # pressing the key on virtual keyboard
        def press_key(ch):
            nonlocal current_col
            nonlocal current_row
            if current_row >= ROWS:
                return
            if current_col < COLS:
                grid[current_row][current_col].configure(text=ch)
                current_col += 1
                msg_label.configure(text="") #clears the msgs (dont move this cuz idk where else to put this)

        #config the delete button
        def delete_letter():
            nonlocal current_col
            nonlocal current_row
            if current_row >= ROWS:
                return
            if current_col > 0:
                current_col -= 1
                grid[current_row][current_col].configure(text="")
                msg_label.configure(text="")

        #check if the guess is correct or even if it has any  of the correct letters
        def check_guess(guess):
            nonlocal current_row
            nonlocal current_col
            solution = list(SOLUTION)
            guess_list = list(guess)

            colors = [""] * COLS
            used = [False] * COLS

        #leetcode god logic (what do u mean nested for's are bad)
            for i in range(COLS):#checks for greens
                if guess_list[i] == solution[i]:
                    colors[i] = COLOR_CORRECT
                    used[i] = True

            for i in range(COLS):#checks for yellows and greys
                if colors[i] == "":
                    if guess_list[i] in solution:
                        for j in range(COLS):
                            if not used[j] and solution[j] == guess_list[i]:
                                colors[i] = COLOR_PRESENT
                                used[j] = True
                                break
                    if colors[i] == "":
                        colors[i] = COLOR_ABSENT

            for i in range(COLS):
                lbl = grid[current_row][i]
                lbl.configure(fg_color=colors[i], text_color="white")

                ch = guess_list[i]
                btn = keyboard_buttons.get(ch)

                if btn:  #putting colours in the keyboards (im the goat for thinking about the priority system)
                    priority = {COLOR_ABSENT: 0, COLOR_PRESENT: 1, COLOR_CORRECT: 2}
                    current = btn.cget("fg_color")
                    if isinstance(current, list):
                        current = current[0]

                    if current not in priority or priority[colors[i]] > priority.get(current, -1):
                        btn.configure(fg_color=colors[i], text_color="white")

            if guess_list == solution:
                show_popup("You win! Word = ",SOLUTION)
                return

            current_row += 1
            current_col = 0

            if current_row == ROWS:
                show_popup(f"You lose! Word = {SOLUTION}")

        def submit_word():
            nonlocal current_row
            nonlocal current_col

            if current_col < COLS:
                msg_label.configure(text="Not enough letters!")
                return

            guess = "".join(grid[current_row][c].cget("text") for c in range(COLS)).upper()

            if guess not in VALID_WORDS:
                msg_label.configure(text="Not in word list!")

                return

            check_guess(guess)

        def show_popup(msg):
            win = ctk.CTkToplevel(wordle_window)
            ctk.CTkLabel(win, text=msg, font=("Agency FB", 20, "bold")).pack(pady=20)
            ctk.CTkButton(win, text="OK", command=win.destroy).pack(pady=10)

        #virtual keyboard
        def build_keyboard():
            layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

            keyboard_frame = ctk.CTkFrame(wordle_window, fg_color="transparent")
            keyboard_frame.grid(row=1, column=0)

            for row in layout:
                f = ctk.CTkFrame(keyboard_frame, fg_color="transparent")
                f.pack(pady=4)
                for ch in row:
                    btn = ctk.CTkButton(
                        f, text=ch,
                        width=45, height=45,
                        command=lambda x=ch: press_key(x)
                    )
                    btn.pack(side="left", padx=3)
                    keyboard_buttons[ch] = btn

            bottom = ctk.CTkFrame(keyboard_frame, fg_color="transparent")
            bottom.pack(pady=5)

            ctk.CTkButton(bottom, text="Enter", width=80, command=submit_word,hover_color= "#0E3C10",fg_color="#375638",corner_radius=5).pack(side="left", padx=5)
            ctk.CTkButton(bottom, text="Delete", width=80, command=delete_letter,hover_color= "#0E3C10",fg_color="#375638",corner_radius=6).pack(side="left", padx=5)

        # runing the function for development process
        build_grid()
        build_keyboard()
        wordle_window.mainloop()
