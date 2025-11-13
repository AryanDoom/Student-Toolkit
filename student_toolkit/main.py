import customtkinter as ctk
import tkinter as tk

from attendance.attendance_ui import open_attendance_calculator
from gpa.simple_ui import open_gpa_calculator
from gpa.plus_ui import open_gpa_plus
from todo.todo_ui import open_todo_list
from timer.timer_ui import open_ypt
from qr.qr_ui import open_qr_code
from llm.llm_ui import open_llm

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Student Toolkit")
root.geometry("670x760")
root.configure(bg="#232323")

title = ctk.CTkLabel(
    root,
    text="Student Toolkit",
    font=("Segoe UI", 24, "bold"),
    text_color="#034807"
)
title.pack(pady=30)

button_frame = tk.Frame(root)
button_frame.pack(pady=12)

btn_style = {
    "corner_radius": 25,
    "height": 70,
    "width": 260,
    "font": ("Segoe UI", 22),
    "fg_color": "#232323",
    "text_color": "#1e90ff",
    "hover_color": "#1e1e1e"
}

frame = ctk.CTkFrame(root)
frame.pack(pady=20)

ctk.CTkButton(frame, text="Attendance Calculator",
              command=lambda: open_attendance_calculator(root), **btn_style).grid(row=0, column=0, padx=10, pady=10)

ctk.CTkButton(frame, text="To-Do List",
              command=lambda: open_todo_list(root), **btn_style).grid(row=0, column=1, padx=10, pady=10)

ctk.CTkButton(frame, text="Grade Calculator",
              command=lambda: open_gpa_calculator(root), **btn_style).grid(row=0, column=2, padx=10, pady=10)

ctk.CTkButton(frame, text="Study Timer",
              command=lambda: open_ypt(root), **btn_style).grid(row=2, column=1, padx=10, pady=10)

ctk.CTkButton(frame, text="Book Corner",
              command=lambda: open_qr_code(root), **btn_style).grid(row=1, column=1, padx=10, pady=10)

ctk.CTkButton(frame, text="DOOM Bot",
              command=lambda: open_llm(root), **btn_style).grid(row=1, column=2, padx=10, pady=10)

ctk.CTkButton(frame, text="GPA Calculator ++",
              command=lambda: open_gpa_plus(root), **btn_style).grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
