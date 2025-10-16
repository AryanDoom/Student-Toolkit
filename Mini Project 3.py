import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

#saare imports here pls
from datetime import date


#every funtion ko inke niche dalne tab samajh ayega (not under the root.main())
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def open_attendance_calculator():
    window = ctk.CTkToplevel(root)
    window.title("Attendance Predictor")
    window.geometry("750x800")
    

    ctk.CTkLabel(window, text="Current Attendance %", font=("Segoe UI", 12), bg="#0a0a0a", fg="white").pack(pady=10)
    current_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    current_entry.pack()

    ctk.CTkLabel(window, text="Target Attendance %", font=("Segoe UI", 12), bg="#0a0a0a", fg="white").pack(pady=10)
    target_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    target_entry.pack()

    result_label = ctk.CTkLabel(window, text="", font=("Segoe UI", 12), bg="#0a0a0a", fg="#1e90ff", wraplength=300, justify="left")
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
            total_bunkable_classes=f"{bunkable_classes*7:.0f}"
            if avg_classes_needed_per_week > class_per_week:
                result_label.config(text="ggs bro issa ova, better luck next time")
            elif current_percentage < target_percentage:
                result_label.config(text=f"You need to attend {classes_needed}% of the classes left to reach {target_percentage}%.\n"
                             f"That's about {avg_classes_needed_per_week:.0f} classes/week for {weeks_left} weeks.\n"
                             f"You can bunk ~{bunkable_classes:.0f} classes/week,or about {total_bunkable_classes} classes total")

            else:
                 result_label.config(text=f"You're on track! To maintain {target_percentage}%:\n"
                             f"Attend at least {classes_needed} more classes — about {avg_classes_needed_per_week} per week.\n"
                             f"You can bunk ~{bunkable_classes} classes/week.")
        except ValueError:
            result_label.config(text="Please enter valid numbers.")

    ctk.CTkButton(window, text="Calculate", command=calculate_attendance_plan,
                  fg_color="#1e1e1e", hover_color="#2e2e2e", text_color="#1e90ff").pack(pady=10)



def open_todo_list():
    todo_window = ctk.CTkToplevel()
    todo_window.title("Your To-Do List")
    todo_window.geometry("400x400")
    

    def add_task():
        task = task_entry.get().strip()
        if task!=0:
            task_listbox.insert(tk.END, task)
            with open("Todolist.txt", "a") as file:
                file.write(task + "\n")
            task_entry.delete(0, tk.END)

    def clear_tasks():
        task_listbox.delete(0, tk.END)
        open("Todolist.txt", "w").close()

    def load_tasks():
        try:
            with open("Todolist.txt", "r") as file:
                for line in file:
                    task_listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

    def delete_selected():
        selected = task_listbox.curselection()
        if selected!=0:
            task_listbox.delete(selected)
            with open("Todolist.txt", "w") as file:
                for i in range(task_listbox.size()):
                    file.write(task_listbox.get(i) + "\n")

    task_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12), width=25)
    task_entry.pack(pady=10)

    ctk.CTkButton(todo_window, text="Add Task", command=add_task,
                  fg_color="#1e90ff", text_color="white").pack(pady=5)



    task_listbox = ctk.CTkTextbox(todo_window, font=("Segoe UI", 12), width=300, height=200)
    task_listbox.pack(pady=10)

    ctk.CTkButton(todo_window, text="Delete Selected", command=delete_selected,
                  fg_color="#ff6347", text_color="#1e90ff").pack(pady=5)

    ctk.CTkButton(todo_window, text="Clear All", command=clear_tasks,
                  fg_color="#ff4500", text_color="#1e90ff").pack(pady=5)



    load_tasks()

def open_timetable():
    messagebox.showinfo("Time Table", "This will open the Time Table.")

def open_gpa_calculator():
    todo_window = ctk.CTkToplevel(root)
    todo_window.title("GPA Calculator")
    todo_window.geometry("350x500")
    
def label(text):
        ctk.CTkLabel(todo_window, text=text, font=("Segoe UI", 12), text_color="#1e90ff").pack(pady=5)

label("Subject Name")
subject_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12))
subject_entry.pack()

label("ISA 1 Score (out of 40)")
isa1_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12))
isa1_entry.pack()

label("ISA 2 Score (out of 40)")
isa2_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12))
isa2_entry.pack()

label("Assignment Score (out of 10)")
assignment_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12))
assignment_entry.pack()

label("ESA Score (out of 100)")
esa_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12))
esa_entry.pack()

label("Lab Score (only for Chemistry/Python/Physics)")
lab_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12))
lab_entry.pack()

result_label = ctk.CTkLabel(window, text="", font=("Segoe UI", 12), wraplength=300, justify="left", text_color="#1e90ff")
result_label.pack(pady=20)



def calculate_gpa():
      try:
        subject = subject_entry.get().strip().lower()
        isa1 = min(int(isa1_entry.get()), 40) / 2  # out of 20
        isa2 = min(int(isa2_entry.get()), 40) / 2  # out of 20
        assignment = min(int(assignment_entry.get()), 10)  # out of 10
        esa = min(int(esa_entry.get()), 100) / 2  # out of 50
        lab = 0
        total = 0
        max_score = 100  # default max

        if subject in ["chem", "python","cs","chemistry","computer","phy","physics"]:
            lab = min(int(lab_entry.get()), 20)  # out of 20
            max_score = 120  # new max for these subjects

        total = isa1 + isa2 + assignment + esa + lab
        scaled_total = (total / max_score) * 100  # scale to 100

        if scaled_total >= 90:
            grade = "S"
        elif scaled_total >= 80:
            grade = "A"
        elif scaled_total >= 70:
            grade = "B"
        elif scaled_total >= 60:
            grade = "C"
        elif scaled_total >= 50:
            grade = "D"
        else:
            grade = "F"

        result_label.config(
            text=f"Raw Score: {total}/{max_score}\nScaled Score: {scaled_total:.2f}/100\nGrade: {grade}"
        )
      except ValueError:
        result_label.config(text="Please enter valid numbers.")



tk.Button(window, text="Calculate GPA", command=calculate_gpa, font=("Segoe UI", 12),
              bg="#1e1e1e", fg="#1e90ff", activebackground="#2e2e2e", activeforeground="#00bfff",
              bd=0, highlightthickness=0).pack(pady=10)

#main
root = ctk.CTk()
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

