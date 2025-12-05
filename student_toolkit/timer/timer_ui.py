import customtkinter as ctk
import tkinter as tk
import time
from timer.timer_logic import (start_timer_logic,stop_timer_logic,reset_timer_logic,format_time)


#Main window
def open_ypt(root):
    ypt_window = ctk.CTkToplevel(root)
    ypt_window.title("Study Timer")
    ypt_window.geometry("650x520")
    ypt_window.configure(fg_color="#111111")

    ypt_window.lift()
    ypt_window.focus_force()
    ypt_window.grab_set()


    ctk.CTkLabel(ypt_window, text="Study Timer", font=("Agency FB", 24, "bold"),text_color="#ffffff").pack(pady=20)  # Button and colours if one wishes to change

    subjects = {}
    current_subject = tk.StringVar(value="Select Subject")

    subject_entry = ctk.CTkEntry(ypt_window,placeholder_text="Enter Subject",corner_radius=8,height=40,width=240,font=("Agency FB", 16))
    subject_entry.pack(pady=10)

    # fucntions for said buttons
    def add_subject():
        subject = subject_entry.get().strip()
        if subject and subject not in subjects:  # if not already in that list
            subjects[subject] = 0
            subject_menu.configure(values=list(subjects.keys()))  # configure cuz the button already is defined
            current_subject.set(subject)  # gets the subject ready to append
        subject_entry.delete(0, "end")  # clears the textbox for next entry

    ctk.CTkButton(ypt_window,text="Add Subject",command=add_subject,text_color="#ffffff",corner_radius=8,height=40,width=140,hover_color= "#0E3C10",fg_color="#375638").pack(pady=5)

    subject_menu = ctk.CTkOptionMenu(
        ypt_window, values=["No subjects yet"], variable=current_subject
    )
    subject_menu.pack(pady=10)  # option menu is like a drop down u can see it while selecting that thing

    time_label = ctk.CTkLabel(ypt_window,text="00:00:00",font=("Agency FB", 28, "bold"),text_color="white")
    time_label.pack(pady=15)

    # Pre defining the variables used for the timer
    running = False
    start_time = 0
    elapsed = 0

    def update_timer():
        nonlocal elapsed
        if running:  # checks if already there is sum elapsed time and if not if it is running or not
            elapsed = time.time() - start_time  # elapsed time formula
            formatted = format_time(elapsed)  # this is just the formula ig dont ask em how it works
            time_label.configure(text=formatted)
            ypt_window.after(500, update_timer)  # it updates after these many seconds ig ( its hardcoded dk why didnt question why)

    def start_timer():
        nonlocal running, start_time
        current = current_subject.get()
        running, start_time = start_timer_logic(running, current, subjects, start_time)
        if running:
            update_timer()

    def stop_timer():
        nonlocal running
        current = current_subject.get()
        running, subjects_updated = stop_timer_logic(running, current, subjects, elapsed)
        subjects.update(subjects_updated)

    def reset_timer():
        nonlocal running, elapsed
        current = current_subject.get()
        running, elapsed, subjects_updated = reset_timer_logic(running, elapsed, current, subjects)
        subjects.update(subjects_updated)
        time_label.configure(text="00:00:00")

    # UI and buttons for the timer ( if u want to reconfigure)
    btn_frame = ctk.CTkFrame(ypt_window,fg_color="#111111")
    btn_frame.pack(pady=10)

    ctk.CTkButton(btn_frame,text="Start",command=start_timer,text_color="#ffffff",corner_radius=8,width=90,hover_color= "#0E3C10",fg_color="#375638").pack(side="left", padx=10)

    ctk.CTkButton(btn_frame,text="Stop",command=stop_timer,text_color="#ffffff",corner_radius=8,width=90,hover_color= "#0E3C10",fg_color="#375638").pack(side="left", padx=10)

    ctk.CTkButton(btn_frame,text="Reset",command=reset_timer,text_color="#ffffff",corner_radius=8,width=90,hover_color= "#0E3C10",fg_color="#375638").pack(side="left", padx=10)

    ctk.CTkLabel(ypt_window,text="Study Time per Subject",font=("Agency FB", 16),text_color="#ffffff").pack(pady=10)

    stats_box = tk.Text(ypt_window,height=8,width=40,font=("Consolas", 13),bg="#1e1e1e",fg="white")
    stats_box.pack(pady=5)

    # updates the stats like elapsed time and that type of things
    def update_stats():
        stats_box.delete("1.0", tk.END)
        for subj, secs in subjects.items():
            formatted = format_time(secs)
            stats_box.insert(tk.END, f"{subj}: {formatted}\n")
        ypt_window.after(1000, update_stats)

    update_stats()
