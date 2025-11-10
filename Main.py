#all the imports
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from datetime import date
import time
import qrcode
from PIL import Image , ImageTk
import os
import ollama

#appearance and default background theme
ctk.set_appearance_mode("dark")   
ctk.set_default_color_theme("blue")


#Attendance calculator
def open_attendance_calculator():
    window = ctk.CTkToplevel(root)
    window.title("Attendance Predictor")
    window.geometry("900x600")
# labels and the butto
    ctk.CTkLabel(window, text="Current Attendance %", font=("Segoe UI", 18)).pack(pady=10)
    current_entry = ctk.CTkEntry(window, font=("Segoe UI", 18), corner_radius=15, height=40, width=200)
    current_entry.pack(pady=10)

    ctk.CTkLabel(window, text="Target Attendance %", font=("Segoe UI", 18)).pack(pady=10)
    target_entry = ctk.CTkEntry(window, font=("Segoe UI", 18), corner_radius=15, height=40, width=200)
    target_entry.pack(pady=10)

    result_label = ctk.CTkLabel(window, text="", font=("Segoe UI", 16), text_color="#1e90ff", wraplength=500, justify="left")
    result_label.pack(pady=10)


#-----------------Backend of the calculator-----------------------
    def calculate_attendance_plan():
        try:
            current_percentage = int(current_entry.get())
            target_percentage = int(target_entry.get())
            class_per_week = 7

            if not (0 <= current_percentage <= 100 and 0 < target_percentage <= 100): #Invalid entries 
                result_label.configure(text="Invalid input. Enter percentages between 0 and 100.")
                return

# All the variable names and predefined info needed for the code to run ( update the end sem when new data is found )

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

    ctk.CTkButton(window, text="Calculate", command=calculate_attendance_plan,  # Button colour and text that is displayed in the ui
                  text_color="#1e90ff", corner_radius=20, height=44, width=160).pack(pady=18)



#-----------------------Back end for the gpa plus calculator--------------------
def open_gpa_plus():
    
# window and frame shit needed
    gpa_plus_window = ctk.CTkToplevel(root)
    gpa_plus_window.title("GPA Calculator ++")
    gpa_plus_window.geometry("1000x720")
    gpa_plus_window.configure(fg_color="#232323")


#Buttons
    ctk.CTkLabel(gpa_plus_window, text="GPA Calculator ++",font=("Segoe UI", 34, "bold"),text_color="#1e90ff").pack(pady=25)

    
    navigation_frame = ctk.CTkFrame(gpa_plus_window, fg_color="transparent")
    navigation_frame.pack(pady=(10, 20))

    btn_style = {"corner_radius": 12,"width": 220,"height": 50,"font": ("Segoe UI", 16, "bold"),"fg_color": "#2a2a2a","text_color": "#1e90ff","hover_color": "#1e1e1e",}

    container = ctk.CTkFrame(gpa_plus_window, fg_color="#1e1e1e", corner_radius=12)
    container.pack(expand=True, padx=20, pady=20)

    letter_frame = ctk.CTkFrame(container, fg_color="#232323")
    marks_frame = ctk.CTkFrame(container, fg_color="#232323")
    cgpa_frame = ctk.CTkFrame(container, fg_color="#232323")

    for f in (letter_frame, marks_frame, cgpa_frame):
        f.grid(row=0, column=0, sticky="nsew")

    def show_frame(frame):
        frame.tkraise()

    ctk.CTkButton(navigation_frame, text="Letter Grades → SGPA", command=lambda: show_frame(letter_frame), **btn_style).pack(side="left", padx=10)
    ctk.CTkButton(navigation_frame, text="Marks → SGPA", command=lambda: show_frame(marks_frame), **btn_style).pack(side="left", padx=10)
    ctk.CTkButton(navigation_frame, text="SGPAs → CGPA", command=lambda: show_frame(cgpa_frame), **btn_style).pack(side="left", padx=10)


    ctk.CTkLabel(letter_frame, text="Letter Grades → SGPA", font=("Segoe UI", 28, "bold"), text_color="#1e90ff").pack(pady=(20, 10))
    ctk.CTkLabel(letter_frame, text="Number of Subjects:", font=("Segoe UI", 18)).pack()
    lg_entry = ctk.CTkEntry(letter_frame, width=120, height=40, font=("Segoe UI", 16), justify="center")
    lg_entry.pack(pady=8)

    lg_entries = []
    lg_scroll = ctk.CTkScrollableFrame(letter_frame, width=880, height=260, label_text="Enter Grades & Credits")
    lg_scroll.pack(pady=10)

#Pre defined grades and their worth
    grade_points = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 0}
    lg_result = ctk.CTkLabel(letter_frame, text="", font=("Segoe UI", 22, "bold"), text_color="#1e90ff")

#Creating the fields and checking if there are pre existing entries available in the window
    def create_lg_fields():
        for w in lg_scroll.winfo_children():
            w.destroy()  #destroys the existing entries if any
        lg_entries.clear()
        try:
            n = int(lg_entry.get())
            if n <= 0: raise ValueError  #Error if the number entered is not applicable
        except ValueError:
            messagebox.showerror("Error", "Enter valid number of subjects!")
            return


# appending the number of the subjects entered
        for i in range(n):
            row = ctk.CTkFrame(lg_scroll, fg_color="#1e1e1e")
            row.pack(fill="x", padx=20, pady=6)
            ctk.CTkLabel(row, text=f"Subject {i+1}", font=("Segoe UI", 15, "bold"), width=120).pack(side="left", padx=10)
            grade_box = ctk.CTkComboBox(row, values=list(grade_points.keys()), width=100)
            grade_box.set("S")
            grade_box.pack(side="left", padx=10)
            credit_box = ctk.CTkEntry(row, width=100, placeholder_text="Credits", justify="center")
            credit_box.pack(side="left", padx=10)
            lg_entries.append((grade_box, credit_box))

    def calculate_lg_sgpa():
        try:
            total_points, total_credits = 0, 0  #predefining the variables for the calculation
            for gb, ce in lg_entries:
                grade = gb.get().upper()
                credit = float(ce.get())
                total_points += grade_points[grade] * credit
                total_credits += credit
            sgpa = round(total_points / total_credits, 2)  # sgpa formula maybe changed


# pop up for the result
            popup = ctk.CTkToplevel(gpa_plus_window)
            popup.title("SGPA Result")
            popup.geometry("300x150")
            popup.configure(fg_color="#232323")
            ctk.CTkLabel(popup, text=f"SGPA: {sgpa}", font=("Segoe UI", 28, "bold"), text_color="#1e90ff").pack(expand=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))


# UI button and labels
    btn_box = ctk.CTkFrame(letter_frame, fg_color="transparent")
    btn_box.pack(pady=10)
    ctk.CTkButton(btn_box, text="Create Fields", command=create_lg_fields, **btn_style).pack(side="left", padx=15)
    ctk.CTkButton(btn_box, text="Calculate SGPA", command=calculate_lg_sgpa, **btn_style).pack(side="left", padx=15)

    ctk.CTkLabel(marks_frame, text="Marks → SGPA", font=("Segoe UI", 28, "bold"), text_color="#1e90ff").pack(pady=(20, 10))
    ctk.CTkLabel(marks_frame, text="Number of Subjects:", font=("Segoe UI", 18)).pack()
    ms_entry = ctk.CTkEntry(marks_frame, width=120, height=40, font=("Segoe UI", 16), justify="center")
    ms_entry.pack(pady=8)


    ms_entries = []
    ms_scroll = ctk.CTkScrollableFrame(marks_frame, width=880, height=260, label_text="Enter Marks")
    ms_scroll.pack(pady=10)

    ms_result = ctk.CTkLabel(marks_frame, text="", font=("Segoe UI", 22, "bold"), text_color="#1e90ff")

#backend for the marks to sgpa calc
    def create_ms_fields():
        for w in ms_scroll.winfo_children():
            w.destroy()
        ms_entries.clear()
        try:
            n = int(ms_entry.get())
            if n <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter valid number of subjects!")
            return

        headers = ["ISA1", "ISA2", "Assign.", "ESA", "Lab", "Credits"]
        for i in range(n):
            row = ctk.CTkFrame(ms_scroll, fg_color="#1e1e1e")
            row.pack(fill="x", padx=20, pady=6)
            ctk.CTkLabel(row, text=f"Subject {i+1}", font=("Segoe UI", 15, "bold"), width=120).pack(side="left", padx=10)
            boxes = []
            for h in headers:
                box = ctk.CTkFrame(row, fg_color="transparent")
                box.pack(side="left", padx=6)
                ctk.CTkLabel(box, text=h).pack()
                e = ctk.CTkEntry(box, width=70, justify="center")
                e.pack()
                boxes.append(e)
            ms_entries.append(boxes)

#Actual math for the calc if its wrong pls change idk what the actual formula is bruh
    def ms_calc_total(isa1, isa2, assignment, esa, credit, lab=0):
        if credit == 2:
            return ((isa1 / 2) + (isa2 / 2) + ((esa*7)/10) )
        elif credit in [3, 4]:
            return ((isa1/2) + (isa2/2) + assignment + (esa/2))
        elif credit == 5:
            return ((((isa1/2) + (isa2/2) + assignment + (esa/2) + lab)*120)/100)
        else:
            raise ValueError("Credit must be 2-5")

    def ms_grade_point(total):
        if total >= 90: return 10
        elif total >= 80: return 9
        elif total >= 70: return 8
        elif total >= 60: return 7
        elif total >= 50: return 6
        elif total >= 40: return 5
        else: return 0
#the marks to sgpa function
    def calculate_ms_sgpa():
        try:
            total_points = 0
            total_credits = 0
            for row in ms_entries:
                isa1, isa2, assignment, esa, lab, credit = [float(x.get() or 0) for x in row]
                total = ms_calc_total(isa1, isa2, assignment, esa, credit, lab)
                gp = ms_grade_point(total)
                total_points += gp * credit
                total_credits += credit
            sgpa = round(total_points / total_credits, 2)

            popup = ctk.CTkToplevel(gpa_plus_window)
            popup.title("SGPA Result")
            popup.geometry("300x150")
            popup.configure(fg_color="#232323")
            ctk.CTkLabel(popup, text=f"SGPA: {sgpa}", font=("Segoe UI", 28, "bold"), text_color="#1e90ff").pack(expand=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))
#UI buttons to reconfigure if anyone wants to
    btn_box2 = ctk.CTkFrame(marks_frame, fg_color="transparent")
    btn_box2.pack(pady=10)
    ctk.CTkButton(btn_box2, text="Create Fields", command=create_ms_fields, **btn_style).pack(side="left", padx=15)
    ctk.CTkButton(btn_box2, text="Calculate SGPA", command=calculate_ms_sgpa, **btn_style).pack(side="left", padx=15)

    
    ctk.CTkLabel(cgpa_frame, text="SGPAs → CGPA", font=("Segoe UI", 28, "bold"), text_color="#1e90ff").pack(pady=(20, 10))
    ctk.CTkLabel(cgpa_frame, text="Number of Semesters:", font=("Segoe UI", 18)).pack()
    cg_entry = ctk.CTkEntry(cgpa_frame, width=120, height=40, font=("Segoe UI", 16), justify="center")
    cg_entry.pack(pady=8)

    cg_entries = []
    cg_scroll = ctk.CTkScrollableFrame(cgpa_frame, width=880, height=260, label_text="Enter SGPA for Each Semester")
    cg_scroll.pack(pady=10)


#actual code for the sgpa to cgpa
    def create_cg_fields():
        for w in cg_scroll.winfo_children():
            w.destroy()
        cg_entries.clear()
        try:
            n = int(cg_entry.get())
            if n <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter valid number of semesters!")
            return

        for i in range(n):
            row = ctk.CTkFrame(cg_scroll, fg_color="#1e1e1e")
            row.pack(fill="x", padx=20, pady=6)
            ctk.CTkLabel(row, text=f"Semester {i+1}", font=("Segoe UI", 15, "bold"), width=160).pack(side="left", padx=10)
            e = ctk.CTkEntry(row, width=200, height=36, justify="center", placeholder_text="Enter SGPA")
            e.pack(side="left", padx=10)
            cg_entries.append(e)

    def calculate_cgpa():
        try:
            total = 0
            count = 0
            for e in cg_entries:
                val = e.get().strip()
                if val == "": continue
                sg = float(val)
                if not (0 <= sg <= 10): raise ValueError("SGPA must be between 0 and 10.")  #Value errors 
                total += sg
                count += 1
            cgpa = round(total / count, 2) # Formula
            popup = ctk.CTkToplevel(gpa_plus_window)
            popup.title("CGPA Result")
            popup.geometry("300x150")
            popup.configure(fg_color="#232323")
            ctk.CTkLabel(popup, text=f"CGPA: {cgpa}", font=("Segoe UI", 28, "bold"), text_color="#1e90ff").pack(expand=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))
#UI for the sgpa to cgpa
    btn_box3 = ctk.CTkFrame(cgpa_frame, fg_color="transparent")
    btn_box3.pack(pady=10)
    ctk.CTkButton(btn_box3, text="Create Fields", command=create_cg_fields, **btn_style).pack(side="left", padx=15)
    ctk.CTkButton(btn_box3, text="Calculate CGPA", command=calculate_cgpa, **btn_style).pack(side="left", padx=15)

    show_frame(letter_frame)


#todo list backend
def open_todo_list():
    todo_window = ctk.CTkToplevel(root)
    todo_window.title("Your To-Do List")
    todo_window.geometry("500x400") 


    def add_task():  #add tasks
        task = task_entry.get().strip()
        if task:
            task_listbox.insert(tk.END, task)
            with open("Todolist.txt", "a") as file:
                file.write(task + "\n")
            task_entry.delete(0, tk.END)

    def clear_tasks():  #delete all tasks
        task_listbox.delete(0, tk.END)
        open("Todolist.txt", "w").close()

    def load_tasks():  #check file if tasks exisst , if yes load said tasks
        try:
            with open("Todolist.txt", "r") as file:
                for line in file:
                    task_listbox.insert(tk.END, line.strip())
        except FileNotFoundError: # will just create a file when writing or adding a task so just pass the error raised
            pass

    def delete_selected():  # deleting tasks if selected (1 at a time)
        selected = task_listbox.curselection() # this selects the task clicked 
        for index in reversed(selected):
            task_listbox.delete(index)
        with open("Todolist.txt", "w") as file:
            for i in range(task_listbox.size()):
                file.write(task_listbox.get(i) + "\n")


# UI For the todo list
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


# code for the timer 
def open_ypt():
    ypt_window = ctk.CTkToplevel(root)
    ypt_window.title("Study Timer")
    ypt_window.geometry("650x520")

    ctk.CTkLabel(ypt_window, text="Study Timer", font=("Segoe UI", 24, "bold"), text_color="#1e90ff").pack(pady=20) # Button and colours if one wishes to change

    subjects = {}
    current_subject = tk.StringVar(value="Select Subject")

    subject_entry = ctk.CTkEntry(ypt_window, placeholder_text="Enter Subject", corner_radius=15,height=40, width=240,font=("Segoe UI", 16))
    subject_entry.pack(pady=10)

# fucntions for said buttons
    def add_subject():
        subject = subject_entry.get().strip()
        if subject and subject not in subjects:  # if not already in that list
            subjects[subject] = 0
            subject_menu.configure(values=list(subjects.keys()))  # configure cuz the button already is defined
            current_subject.set(subject)  # gets the subject ready to append
        subject_entry.delete(0, "end")  # clears the textbox for next entry

    ctk.CTkButton(ypt_window, text="Add Subject", command=add_subject, text_color="#1e90ff", corner_radius=20, height=40, width=140).pack(pady=5)

    subject_menu = ctk.CTkOptionMenu(ypt_window, values=["No subjects yet"], variable=current_subject)
    subject_menu.pack(pady=10) # option menu is like a drop down u can see it while selecting that thing

    time_label = ctk.CTkLabel(ypt_window, text="00:00:00", font=("Segoe UI", 28, "bold"), text_color="white")
    time_label.pack(pady=15)
# Pre defining the variables used for the timer
    running = False
    start_time = 0
    elapsed = 0

    def update_timer():
        nonlocal elapsed  # nonlocal as to be able to change said variable
        if running:  # checks if already there is sum elapsed time and if not if it is running or not
            elapsed = time.time() - start_time  # elapsed time formula
            formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed)) # this is just the formula ig dont ask em how it works
            time_label.configure(text=formatted)
            ypt_window.after(500, update_timer) # it updates after these many seconds ig ( its hardcoded dk why didnt question why)

    def start_timer():   # start running teh timer    adds elapsed time if any
        nonlocal running, start_time
        current = current_subject.get()
        if not running and current != "Select Subject" and current in subjects:
            running = True
            start_time = time.time() - subjects[current]
            update_timer()

    def stop_timer():    # stops the timers and displays the amy of time studied
        nonlocal running
        current = current_subject.get()
        if running and current in subjects:
            running = False
            subjects[current] = elapsed

    def reset_timer():
        nonlocal running, elapsed  # just deletes all the values for the elapsed and runnning timers
        running = False
        elapsed = 0
        current = current_subject.get()
        if current in subjects:
            subjects[current] = 0  
            time_label.configure(text="00:00:00")
    

# UI and buttons for the timer ( if u want to reconfigure)    
    btn_frame = ctk.CTkFrame(ypt_window)
    btn_frame.pack(pady=10)

    ctk.CTkButton(btn_frame, text="Start", command=start_timer,text_color="#1e90ff", corner_radius=20, width=90).pack(side="left", padx=10)

    ctk.CTkButton(btn_frame, text="Stop", command=stop_timer,text_color="#1e90ff", corner_radius=20, width=90).pack(side="left", padx=10)

    ctk.CTkButton(btn_frame, text="Reset", command=reset_timer,text_color="#1e90ff", corner_radius=20, width=90).pack(side="left", padx=10)

    
    ctk.CTkLabel(ypt_window, text="Study Time per Subject", font=("Segoe UI", 16), text_color="#1e90ff").pack(pady=10)

    stats_box = tk.Text(ypt_window, height=8, width=40, font=("Consolas", 13), bg="#1e1e1e", fg="white")
    stats_box.pack(pady=5)

    def update_stats():  # updates the stats like elapsed time and that type of things
        stats_box.delete("1.0", tk.END)
        for subj, secs in subjects.items():
            formatted = time.strftime("%H:%M:%S", time.gmtime(secs))
            stats_box.insert(tk.END, f"{subj}: {formatted}\n")
        ypt_window.after(1000, update_stats)

    update_stats()

# simples gpa calc code 
def open_gpa_calculator():
    gpa_window = ctk.CTkToplevel(root)
    gpa_window.title("GPA Calculator")
    gpa_window.geometry("520x550")
# UI and the textbox and lables for the marks and things
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


# Back end the acutal code for the calc ( simple stuff just look at the variable names)
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

# code for the qr code / book corner 
def open_qr_code():
    qr_window = ctk.CTkToplevel(root)
    qr_window.title("QR Code for Every TextBook Needed")
    qr_window.geometry("520x550")

    def label(text):
        ctk.CTkLabel(qr_window, text=text, font=("Segoe UI", 15), text_color="#1e90ff").pack(pady=4)

    label("Select the Subject you would like the book for")

    subject_var = tk.StringVar(value="")  #add the subjects here

    subjects = {      # storing the subjects and what they map to
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
#storing the mapped urls and subject we do offer
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


# QR code specificatios ( pls dont touch or change the version and box and border size configs)
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(book_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1e90ff", back_color="black")
        img = img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(img)
        qr_label.configure(image=tk_img, text="")
        qr_label.image = tk_img

    ctk.CTkButton(qr_window, text="Generate QR Code", command=generate_qr).pack(pady=10)


# Code for DOOM BOT
def open_llm():
    llm_window = ctk.CTkToplevel(root)
    llm_window.title("Any Doubts you might have gets solved")
    llm_window.geometry("1000x1000")

    def label(text):
        ctk.CTkLabel( llm_window, text=text,font=("Segoe UI", 15),text_color="#006d12").pack(pady=(15, 5))  
 
    label("Enter your doubt (Please enter exit if conversation is completed).")

# UI for the response box and the doubt text box
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
            response = ollama.chat(model="DOOM_BOT_ASSITANT",messages=[{"role": "user", "content": user_doubt}])  # Actual bot calling and chat setting up details ( could be replaced by genai if needed or seen necessary)

            reply = response["message"]["content"]

          
            response_box.insert("end", f" You: {user_doubt}\n\n=> Response: {reply}\n\n")
            response_box.see("end")  
            llm_entry.delete(0, "end") # clears the text (doubt ) box

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


# First Frame button style could be changed if needed to 
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


# grid and features buttons
ctk.CTkButton(frame, text="Attendance Calculator", command=open_attendance_calculator, **btn_style).grid(row=0, column=0, padx=10, pady=10)
ctk.CTkButton(frame, text="To-Do List", command=open_todo_list, **btn_style).grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(frame, text="Grade Calculator", command=open_gpa_calculator, **btn_style).grid(row=0, column=2, padx=10, pady=10)
ctk.CTkButton(frame, text="Study Timer", command=open_ypt, **btn_style).grid(row=2, column=1, padx=10, pady=10)
ctk.CTkButton(frame, text="Book Corner", command=open_qr_code, **btn_style ).grid(row=1, column=1 ,padx=10, pady=10)
ctk.CTkButton(frame, text="DOOM Bot", command=open_llm, **btn_style ).grid(row=1, column=2 ,padx=10, pady=10)
ctk.CTkButton(frame, text="GPA Calculator", command=open_gpa_plus, **btn_style).grid(row=1, column=0, padx=10, pady=10)

root.mainloop()