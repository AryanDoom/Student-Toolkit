import customtkinter as ctk
import tkinter as tk


#----------------ALL THE IMPORTS FROM THE FILES IN THIS FOLDER ( do not mess with these)---------------
from attendance.attendance_ui import open_attendance_calculator
from gpa.simple_ui import open_gpa_calculator
from gpa.plus_ui import open_gpa_plus
from todo.todo_ui import open_todo_list
from timer.timer_ui import open_ypt
from qr.qr_ui import open_qr_code
from llm.llm_ui import open_llm

ctk.set_appearance_mode("dark")  #Maim appearance of the ctk window can be changed when needed( the default colour is just the colour of buttons until stated otherwise)
ctk.set_default_color_theme("blue")


#Main window settings and colour and stuff
main_window = ctk.CTk() 
main_window.title("Student Toolkit")
main_window.geometry("670x760")
main_window.configure(bg="#232323")

title = ctk.CTkLabel(main_window,text="Student Toolkit",font=("Segoe UI", 24, "bold"),text_color="#09820F")# Main title
title.pack(pady=30)

button_frame = ctk.CTkFrame(main_window,fg_color="#35383A",corner_radius=7)# Main button frame
button_frame.pack(pady=20)

#How the buttons look like
btn_style = {"corner_radius": 25,"height": 70,"width": 260,"font": ("Segoe UI", 22),"fg_color": "#292828","text_color": "#1e90ff","hover_color": "#1e1e1e"}

#All The buttons and stuff ( change for the appearance)
ctk.CTkButton(button_frame, text="Attendance Calculator",command=lambda: open_attendance_calculator(main_window), **btn_style).grid(row=0, column=0, padx=10, pady=10)

ctk.CTkButton(button_frame, text="To-Do List",command=lambda: open_todo_list(main_window), **btn_style).grid(row=0, column=1, padx=10, pady=10)

ctk.CTkButton(button_frame, text="Grade Calculator",command=lambda: open_gpa_calculator(main_window), **btn_style).grid(row=0, column=2, padx=10, pady=10)

ctk.CTkButton(button_frame, text="Study Timer",command=lambda: open_ypt(main_window), **btn_style).grid(row=2, column=1, padx=10, pady=10)

ctk.CTkButton(button_frame, text="Book Corner",command=lambda: open_qr_code(main_window), **btn_style).grid(row=1, column=1, padx=10, pady=10)

ctk.CTkButton(button_frame, text="DOOM Bot",command=lambda: open_llm(main_window), **btn_style).grid(row=1, column=2, padx=10, pady=10)

ctk.CTkButton(button_frame, text="GPA Calculator ++",command=lambda: open_gpa_plus(main_window), **btn_style).grid(row=1, column=0, padx=10, pady=10)

main_window.mainloop()
