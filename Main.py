import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import date
import time
import qrcode
from PIL import Image , ImageTk
import os
from google import genai
import ollama

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def open_attendance_calculator():
    window = ctk.CTkToplevel(root)
    window.title("Attendance Predictor")
    window.geometry("900x600")

    ctk.CTkLabel(window, text="Current Attendance %", font=("Segoe UI", 18)).pack(pady=10)
    current_entry = ctk.CTkEntry(window, font=("Segoe UI", 18), corner_radius=15, height=40, width=200)
    current_entry.pack(pady=10)

    ctk.CTkLabel(window, text="Target Attendance %", font=("Segoe UI", 18)).pack(pady=10)
    target_entry = ctk.CTkEntry(window, font=("Segoe UI", 18), corner_radius=15, height=40, width=200)
    target_entry.pack(pady=10)

    result_label = ctk.CTkLabel(window, text="", font=("Segoe UI", 16), text_color="#1e90ff", wraplength=500, justify="left")
    result_label.pack(pady=10)

    def calculate_attendance_plan():
        try:
            current_percentage = int(current_entry.get())
            target_percentage = int(target_entry.get())
            class_per_week = 7

            if not (0 <= current_percentage <= 100 and 0 < target_percentage <= 100):
                result_label.configure(text="Invalid input. Enter percentages between 0 and 100.")
                return

            today = date.today()
            end_sem = date(2026, 1, 2)
            days_left = (end_sem - today).days
            weeks_left = max(days_left // 7, 1)
            total_classes_left = weeks_left * class_per_week
            current_total_classes = 100
            current_attended = (current_percentage / 100) * current_total_classes
            target_total_attendance = (target_percentage / 100) * (current_total_classes + total_classes_left)
            classes_needed = max(int(target_total_attendance - current_attended), 0)
            avg_classes_needed_per_week = round(classes_needed / weeks_left, 2)
            bunkable_classes = max(round(class_per_week - avg_classes_needed_per_week, 2), 0)
            total_bunkable_classes = f"{int(bunkable_classes * weeks_left)}"

            if avg_classes_needed_per_week > class_per_week:
                result_label.configure(text="ggs bro issa ova, better luck next time")
            elif current_percentage < target_percentage:
                result_label.configure(
                    text=f"You need to attend {classes_needed} classes out of the remaining {total_classes_left} classes to reach {target_percentage}%.\n"
                         f"That's about {avg_classes_needed_per_week:.0f} classes/week for {weeks_left} weeks.\n"
                         f"You can bunk ~{bunkable_classes:.0f} classes/week, or about {total_bunkable_classes} classes total."
                )
            else:
                result_label.configure(
                    text=f"You're on track! To maintain {target_percentage}%:\n"
                         f"Attend at least {classes_needed} more classes — about {avg_classes_needed_per_week} per week.\n"
                         f"You can bunk ~{bunkable_classes:.0f} classes/week."
                )
        except ValueError:
            result_label.configure(text="Please enter valid numbers.")

    ctk.CTkButton(window, text="Calculate", command=calculate_attendance_plan,
                  text_color="#1e90ff", corner_radius=20, height=44, width=160).pack(pady=18)


def open_todo_list():
    todo_window = ctk.CTkToplevel(root)
    todo_window.title("Your To-Do List")
    todo_window.geometry("500x400") 

    def add_task():
        task = task_entry.get().strip()
        if task:
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
        for index in reversed(selected):
            task_listbox.delete(index)
        with open("Todolist.txt", "w") as file:
            for i in range(task_listbox.size()):
                file.write(task_listbox.get(i) + "\n")

    task_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 18), width=280, corner_radius=15, height=36)
    task_entry.pack(pady=10)

    ctk.CTkButton(todo_window, text="Add Task", command=add_task,
                  text_color="white", corner_radius=18, height=36, width=130).pack(pady=5)

    task_listbox = tk.Listbox(todo_window, font=("Segoe UI", 15), width=40, height=12, selectbackground="#1e90ff", selectforeground="white")
    task_listbox.pack(pady=10)

    ctk.CTkButton(todo_window, text="Delete Selected", command=delete_selected,
                  text_color="#1e90ff", corner_radius=18, height=36, width=130).pack(pady=5)

    ctk.CTkButton(todo_window, text="Clear All", command=clear_tasks,
                  text_color="#1e90ff", corner_radius=18, height=36, width=130).pack(pady=5)

    load_tasks()

def open_ypt():
    ypt_window = ctk.CTkToplevel(root)
    ypt_window.title("Study Timer")
    ypt_window.geometry("650x520")

    ctk.CTkLabel(ypt_window, text="Study Timer", font=("Segoe UI", 24, "bold"), text_color="#1e90ff").pack(pady=20)

    subjects = {}
    current_subject = tk.StringVar(value="Select Subject")

    subject_entry = ctk.CTkEntry(ypt_window, placeholder_text="Enter Subject", corner_radius=15,height=40, width=240,font=("Segoe UI", 16))
    subject_entry.pack(pady=10)

    def add_subject():
        subject = subject_entry.get().strip()
        if subject and subject not in subjects:
            subjects[subject] = 0
            subject_menu.configure(values=list(subjects.keys()))
            current_subject.set(subject)
        subject_entry.delete(0, "end")

    ctk.CTkButton(ypt_window, text="Add Subject", command=add_subject, text_color="#1e90ff", corner_radius=20, height=40, width=140).pack(pady=5)

    subject_menu = ctk.CTkOptionMenu(ypt_window, values=["No subjects yet"], variable=current_subject)
    subject_menu.pack(pady=10)

    time_label = ctk.CTkLabel(ypt_window, text="00:00:00", font=("Segoe UI", 28, "bold"), text_color="white")
    time_label.pack(pady=15)

    running = False
    start_time = 0
    elapsed = 0

    def update_timer():
        nonlocal elapsed
        if running:
            elapsed = time.time() - start_time
            formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            time_label.configure(text=formatted)
            ypt_window.after(500, update_timer)

    def start_timer():
        nonlocal running, start_time
        current = current_subject.get()
        if not running and current != "Select Subject" and current in subjects:
            running = True
            start_time = time.time() - subjects[current]
            update_timer()

    def stop_timer():
        nonlocal running
        current = current_subject.get()
        if running and current in subjects:
            running = False
            subjects[current] = elapsed

    def reset_timer():
        nonlocal running, elapsed
        running = False
        elapsed = 0
        current = current_subject.get()
        if current in subjects:
            subjects[current] = 0  
            time_label.configure(text="00:00:00")
    
    btn_frame = ctk.CTkFrame(ypt_window)
    btn_frame.pack(pady=10)

    ctk.CTkButton(btn_frame, text="Start", command=start_timer,text_color="#1e90ff", corner_radius=20, width=90).pack(side="left", padx=10)

    ctk.CTkButton(btn_frame, text="Stop", command=stop_timer,text_color="#1e90ff", corner_radius=20, width=90).pack(side="left", padx=10)

    ctk.CTkButton(btn_frame, text="Reset", command=reset_timer,text_color="#1e90ff", corner_radius=20, width=90).pack(side="left", padx=10)

    
    ctk.CTkLabel(ypt_window, text="Study Time per Subject", font=("Segoe UI", 16), text_color="#1e90ff").pack(pady=10)

    stats_box = tk.Text(ypt_window, height=8, width=40, font=("Consolas", 13), bg="#1e1e1e", fg="white")
    stats_box.pack(pady=5)

    def update_stats():
        stats_box.delete("1.0", tk.END)
        for subj, secs in subjects.items():
            formatted = time.strftime("%H:%M:%S", time.gmtime(secs))
            stats_box.insert(tk.END, f"{subj}: {formatted}\n")
        ypt_window.after(1000, update_stats)

    update_stats()


def open_gpa_calculator():
    gpa_window = ctk.CTkToplevel(root)
    gpa_window.title("GPA Calculator")
    gpa_window.geometry("520x550")

    def label(text):
        ctk.CTkLabel(gpa_window, text=text, font=("Segoe UI", 15), text_color="#1e90ff").pack(pady=4)

    label("Subject Name")
    subject_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    subject_entry.pack(pady=4)

    label("ISA 1 Score (out of 40)")
    isa1_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    isa1_entry.pack(pady=4)

    label("ISA 2 Score (out of 40)")
    isa2_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    isa2_entry.pack(pady=4)

    label("Assignment Score (out of 10)")
    assignment_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    assignment_entry.pack(pady=4)

    label("ESA Score (out of 100)")
    esa_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    esa_entry.pack(pady=4)

    label("Lab Score (only for Chemistry/Python/Physics)")
    lab_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    lab_entry.pack(pady=4)

    result_label = ctk.CTkLabel(gpa_window, text="", font=("Segoe UI", 15), wraplength=320, justify="left", text_color="#1e90ff")
    result_label.pack(pady=10)

    def calculate_gpa():
        try:
            subject = subject_entry.get().strip().lower()
            isa1 = min(int(isa1_entry.get()), 40) / 2
            isa2 = min(int(isa2_entry.get()), 40) / 2
            assignment = min(int(assignment_entry.get()), 10)
            esa = min(int(esa_entry.get()), 100) / 2
            lab = 0
            max_score = 100

            if subject in ["chem", "python", "cs", "chemistry", "computer", "phy", "physics"]:
                lab = min(int(lab_entry.get()), 20)
                max_score = 120

            total = isa1 + isa2 + assignment + esa + lab
            scaled_total = (total / max_score) * 100

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

            result_label.configure(
                text=f"Raw Score: {total:.2f}/{max_score}\nScaled Score: {scaled_total:.2f}/100\nGrade: {grade}"
            )
        except ValueError:
            result_label.configure(text="Please enter valid numbers.")

    ctk.CTkButton(gpa_window, text="Calculate GPA", command=calculate_gpa,
                  text_color="#1e90ff", corner_radius=15, height=40, width=160).pack(pady=10)


def open_qr_code():
    qr_window = ctk.CTkToplevel(root)
    qr_window.title("QR Code for Every TextBook Needed")
    qr_window.geometry("520x550")

    def label(text):
        ctk.CTkLabel(qr_window, text=text, font=("Segoe UI", 15), text_color="#1e90ff").pack(pady=4)

    label("Select the Subject you would like the book for")

    subject_var = tk.StringVar(value="")  # Holds selected subject

    subjects = {
        "Maths 1": "maths1",
        "Maths 2": "maths2",
        "Chemistry": "chemistry",
        "Mechanics": "mechanics",
        "EPD": "epd",
        "Python": "python",
        "Physics": "physics",
        "Electrical": "electrical",
        "Physics Lab": "physicslab",
        "Constitution": "constitution",
        "EVS": "evs",
        "Placeholder": "placeholder"
    }

    for label_text, value in subjects.items():
        ctk.CTkRadioButton(qr_window, text=label_text, variable=subject_var, value=value).pack(anchor="center", padx=20)

    qr_label = ctk.CTkLabel(qr_window, text="")
    qr_label.pack(pady=10)

    def generate_qr():
        subject = subject_var.get()
        if subject == "":
            qr_label.configure(text="Please select a subject.")
            return

        url_map = {
            "maths1": "https://drive.google.com/drive/folders/1gYFT1RvJD5XmsquB99-vXC5xBWV9EzZZ",
            "maths2": "https://drive.google.com/drive/folders/1iaewOilIhQZZgfCKqDJeFC2lty7g9AQk",
            "chemistry": "https://drive.google.com/drive/folders/1yHNKMxDFvf_FopJ-ZCDNKRlGleTFQZcN",
            "mechanics": "https://drive.google.com/drive/folders/1JGEaaw-j-tzMTEhRoxM7gmtSEaK2ZT5j",
            "epd": "https://drive.google.com/drive/folders/1rkUuM3-W249sFgl1Eqn6zbx29AaTCHLB",
            "placeholder": "https://textbooks.example.com/",
            "python": "https://drive.google.com/file/d/17cVJ_8MPCULzXPcgt4if4O6fBAsfy1Uc/view",
            "physics": "https://drive.google.com/file/d/1KwxEcR4klXQwS-uKcO16PXHQPMmHDCAj/view",
            "electrical": "https://drive.google.com/drive/folders/16UDSJJ4c4N3StFjDbvdwRFuV-gFfWT3S",
            "physicslab": "https://drive.google.com/file/d/1GMoZGnNMitVkx-VvcuIWr3qAQD7fnhqK/view",
            "constitution": "https://drive.google.com/drive/folders/1viBbRv-CGnwFGfJLcC2os6t90fpMwQuG",
            "evs": "https://drive.google.com/file/d/1IKXMDt1LeoBH4uyD7LiQx_8BmQaLbR0K/view?usp=drive_link"
        }

        book_url = url_map.get(subject, "") + subject.replace(" ", "_").lower()

        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(book_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1e90ff", back_color="black")
        img = img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(img)
        qr_label.configure(image=tk_img, text="")
        qr_label.image = tk_img

    ctk.CTkButton(qr_window, text="Generate QR Code", command=generate_qr).pack(pady=10)



def open_llm():
    llm_window = ctk.CTkToplevel(root)
    llm_window.title("Any Doubts you might have gets solved")
    llm_window.geometry("1000x1000")

    def label(text):
        ctk.CTkLabel( llm_window, text=text,font=("Segoe UI", 15),text_color="#006d12").pack(pady=(15, 5))  
 
    label("Enter your doubt (Please enter exit if conversation is completed).")


    llm_entry = ctk.CTkEntry(llm_window,font=("Segoe UI", 15),corner_radius=12,height=33,width=500)
    llm_entry.pack(pady=(12, 6))
    

    response_box = ctk.CTkTextbox(llm_window,width=850, height=400, wrap="word", font=("Segoe UI", 15) )
    response_box.pack(pady=15)

    def get_answer():
        user_doubt = llm_entry.get().strip()
        if user_doubt.lower() == "exit":
            llm_window.destroy()
            return

        if user_doubt=="":
            response_box.insert("end", " Please enter a question.\n\n")
            return

        try:
            response = ollama.chat(model="DOOM_BOT_ASSITANT",messages=[{"role": "user", "content": user_doubt}])

            reply = response["message"]["content"]

          
            response_box.insert("end", f" You: {user_doubt}\n\n=> Response: {reply}\n\n")
            response_box.see("end")  
            llm_entry.delete(0, "end")

        except Exception as e:
            response_box.insert("end", f" Error: {e}\n\n")

  
    ctk.CTkButton(llm_window,text="Calculate Response",command=get_answer,text_color="#000000",corner_radius=15,height=40,width=160).pack(pady=10)


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

ctk.CTkButton(frame, text="Attendance Calculator", command=open_attendance_calculator, **btn_style).grid(row=0, column=0, padx=10, pady=10)
ctk.CTkButton(frame, text="To-Do List", command=open_todo_list, **btn_style).grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(frame, text="GPA Calculator", command=open_gpa_calculator, **btn_style).grid(row=1, column=0, padx=10, pady=10)
ctk.CTkButton(frame, text="Study Timer", command=open_ypt, **btn_style).grid(row=1, column=1, padx=10, pady=10)
ctk.CTkButton(frame, text="Book Corner", command=open_qr_code, **btn_style ).grid(row=3, column=1 ,padx=10, pady=10)
ctk.CTkButton(frame, text="DOOM Bot", command=open_llm, **btn_style ).grid(row=3, column=0 ,padx=10, pady=10)


root.mainloop()