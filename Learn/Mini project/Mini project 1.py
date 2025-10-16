import tkinter as tk
from tkinter import messagebox

#saare imports here pls
from datetime import date


#every funtion ko inke niche dalne tab samajh ayega (not under the root.main())
def open_attendance_calculator():
    window = tk.Toplevel(root)
    window.title("Attendance Predictor")
    window.geometry("350x400")
    window.configure(bg="#0a0a0a")

    tk.Label(window, text="Current Attendance %", font=("Segoe UI", 12), bg="#0a0a0a", fg="white").pack(pady=10)
    current_entry = tk.Entry(window, font=("Segoe UI", 12))
    current_entry.pack()

    tk.Label(window, text="Target Attendance %", font=("Segoe UI", 12), bg="#0a0a0a", fg="white").pack(pady=10)
    target_entry = tk.Entry(window, font=("Segoe UI", 12))
    target_entry.pack()

    result_label = tk.Label(window, text="", font=("Segoe UI", 12), bg="#0a0a0a", fg="#1e90ff", wraplength=300, justify="left")
    result_label.pack(pady=20)

    def calculate_attendance_plan():
        try:
            current_percentage = int(current_entry.get())
            target_percentage = int(target_entry.get())
            class_per_week = 7

            if not (0 <= current_percentage <= 100 and 0 < target_percentage <= 100):
                result_label.config(text="Invalid input. Enter percentages between 0 and 100.")
                return

            today = date.today()
            end_sem = date(2026, 1, 2)
            days_left = (end_sem - today).days
            weeks_left = max(days_left // 7, 1)

            total_classes_left = weeks_left * class_per_week
            current_total_classes = 100
            current_attended = current_percentage
            target_total_attendance = target_percentage * (current_total_classes + total_classes_left) / 100
            classes_needed = max(int(target_total_attendance - current_attended), 0)
            avg_classes_needed_per_week = round(classes_needed / weeks_left, 2)

            if avg_classes_needed_per_week == round(classes_needed / weeks_left, 2):
                bunkable_classes = max(round(class_per_week - avg_classes_needed_per_week, 2), 0)

            if avg_classes_needed_per_week > class_per_week:
                result_label.config(text="ggs bro issa ova, better luck next time")
            elif current_percentage < target_percentage:
                result_label.config(text=f"You need to attend {classes_needed}% of the classes left to reach {target_percentage}%.\n"
                             f"That's about {avg_classes_needed_per_week} classes/week for {weeks_left} weeks.\n"
                             f"You can bunk ~{bunkable_classes} classes/week.")

            else:
                 result_label.config(text=f"You're on track! To maintain {target_percentage}%:\n"
                             f"Attend at least {classes_needed} more classes — about {avg_classes_needed_per_week} per week.\n"
                             f"You can bunk ~{bunkable_classes} classes/week.")
        except ValueError:
            result_label.config(text="Please enter valid numbers.")

    tk.Button(window, text="Calculate", command=calculate_attendance_plan, font=("Segoe UI", 12),
              bg="#1e1e1e", fg="#1e90ff", activebackground="#2e2e2e", activeforeground="#00bfff",
              bd=0, highlightthickness=0).pack(pady=10)

def open_todo_list():
    messagebox.showinfo("To-Do List", "This will open the To-Do List.")

def open_timetable():
    messagebox.showinfo("Time Table", "This will open the Time Table.")

def open_gpa_calculator():
    messagebox.showinfo("GPA Calculator", "This will open the GPA Calculator.")

#main
root = tk.Tk()
root.title("Student Toolkit")
root.geometry("400x500")
root.configure(bg="#0a0a0a")

#title
title = tk.Label(
    root,
    text="Student Toolkit",
    font=("Segoe UI", 18, "bold"),
    bg="#0a0a0a",
    fg="#1e90ff"  
)
title.pack(pady=40)

#accha dikhna chahiye na
button_style = {
    "font": ("Segoe UI", 14),
    "width": 20,
    "height": 2,
    "bg": "#1e1e1e",  
    "fg": "#1e90ff",  
    "activebackground": "#2e2e2e",
    "activeforeground": "#00bfff",  
    "bd": 0,
    "highlightthickness": 0
}


button_frame = tk.Frame(root, bg="#0a0a0a")
button_frame.pack(pady=10)

#button
tk.Button(button_frame, text="Attendance Calculator", command=open_attendance_calculator, **button_style).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="To-Do List", command=open_todo_list, **button_style).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Time Table", command=open_timetable, **button_style).grid(row=1, column=0, padx=10, pady=10)
tk.Button(button_frame, text="GPA Calculator", command=open_gpa_calculator, **button_style).grid(row=1, column=1, padx=10, pady=10)

#finish(kill me)
root.mainloop()

