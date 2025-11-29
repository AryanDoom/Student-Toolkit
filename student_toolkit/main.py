import customtkinter as ctk
import tkinter as tk

# ---------------- Imports of all the functions --------------------------------------------------
from attendance.attendance_ui import open_attendance_calculator
from gpa.simple_ui import open_gpa_calculator
from gpa.plus_ui import open_gpa_plus
from todo.todo_ui import open_todo_list
from timer.timer_ui import open_ypt
from qr.qr_ui import open_qr_code
from llm.llm_ui import open_llm
from quiz.quiz_ui import open_quiz
from games.games_ui import open_game

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Main window and config-----------------------------------------
main_window = ctk.CTk()
main_window.title("Student Toolkit")
main_window.geometry("1090x650")
main_window.configure(fg_color="#000000")


# ---------------- side buttons -----------------------------------
sidebar = ctk.CTkFrame(main_window, fg_color="#1a1a1a", corner_radius=0, width=220)
sidebar.pack(side="left", fill="y")

title_label = ctk.CTkLabel(sidebar,text="Buttons",font=("Agency FB", 28, "bold"),text_color="#ffffff")
title_label.pack(pady=(20, 30))


def sidebar_btn(text, command):
    return ctk.CTkButton(sidebar,text=text,command=command,fg_color="transparent",hover_color="#2d2d2d",font=("Agency FB", 18),anchor="w",text_color="#cccccc")


sidebar_btn("Dashboard", lambda: None).pack(fill="x", pady=8, padx=15)
sidebar_btn("Attendance", lambda: open_attendance_calculator(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("GPA Calculator", lambda: open_gpa_calculator(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("To-Do List", lambda: open_todo_list(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("Book Corner", lambda: open_qr_code(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("Study Timer", lambda: open_ypt(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("DOOM Bot", lambda: open_llm(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("Quiz Centre",lambda: open_llm(main_window)).pack(fill="x", pady=8, padx=15)
sidebar_btn("GPA++",lambda: open_gpa_plus(main_window)).pack(fill="x", pady=8, padx=15)


# ---------------- Main buttons----------------------------------------
content = ctk.CTkFrame(main_window,fg_color="#141414",corner_radius=20)
content.pack(side="left", fill="both", expand=True, padx=20, pady=20)

header = ctk.CTkLabel(content,text="Welcome to Student Toolkit",font=("Agency FB", 30, "bold"),text_color="#ffffff")
header.pack(pady=20)


# floating grid container
grid_frame = ctk.CTkFrame(content,fg_color="#1f1f1f",corner_radius=18)
grid_frame.pack(pady=10, padx=20, fill="both", expand=True)


#buttons style
btn_style = {"corner_radius": 18,"height": 110,"width": 240,"font": ("Agency FB", 20, "bold"),"fg_color": "#080707","hover_color": "#0E3C10","text_color": "#ffffff"}




ctk.CTkButton(grid_frame, text="Attendance", command=lambda: open_attendance_calculator(main_window),**btn_style).grid(row=0, column=0, padx=20, pady=20)

ctk.CTkButton(grid_frame, text= "To-Do List", command=lambda: open_todo_list(main_window),**btn_style).grid(row=0, column=1, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="Grade Calculator",  command=lambda: open_gpa_calculator(main_window),**btn_style).grid(row=0, column=2, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="Book Corner", command=lambda: open_qr_code(main_window),**btn_style).grid(row=1, column=0, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="DOOM Bot", command=lambda: open_llm(main_window),**btn_style).grid(row=1, column=1, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="Study Timer", command=lambda: open_ypt(main_window),**btn_style).grid(row=1, column=2, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="GPA Calculator ++", command=lambda: open_gpa_plus(main_window),**btn_style).grid(row=2, column=1, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="Quiz Centre", command=lambda: open_quiz(main_window),**btn_style).grid(row=2, column=0, padx=20, pady=20)

ctk.CTkButton(grid_frame, text="Brain Teasers", command=lambda: open_game(main_window),**btn_style).grid(row=2, column=2, padx=20, pady=20)

main_window.mainloop()
