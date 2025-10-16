import customtkinter as ctk
from tkinter import messagebox
from datetime import date

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def open_attendance_calculator():
    window = ctk.CTkToplevel(root)
    window.geometry("750x800")

    ctk.CTkLabel(window, text="Current Attendance %", font=("Segoe UI", 12)).pack(pady=10)
    current_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    current_entry.pack()

    ctk.CTkLabel(window, text="Target Attendance %", font=("Segoe UI", 12)).pack(pady=10)
    target_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    target_entry.pack()

    result_label = ctk.CTkLabel(window, text="", font=("Segoe UI", 12), wraplength=300, justify="left", text_color="#1e90ff")
    result_label.pack(pady=20)

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
            current_attended = current_percentage
            target_total_attendance = target_percentage * (current_total_classes + total_classes_left) / 100
            classes_needed = max(int(target_total_attendance - current_attended), 0)
            avg_classes_needed_per_week = round(classes_needed / weeks_left, 2)

            bunkable_classes = max(round(class_per_week - avg_classes_needed_per_week, 2), 0)
            total_bunkable_classes = f"{bunkable_classes * 7:.0f}"

            if avg_classes_needed_per_week > class_per_week:
                result_label.configure(text="ggs bro issa ova, better luck next time")
            elif current_percentage < target_percentage:
                result_label.configure(text=f"You need to attend {classes_needed}% of the classes left to reach {target_percentage}%.\n"
                                            f"That's about {avg_classes_needed_per_week:.0f} classes/week for {weeks_left} weeks.\n"
                                            f"You can bunk ~{bunkable_classes:.0f} classes/week, or about {total_bunkable_classes} classes total")
            else:
                result_label.configure(text=f"You're on track! To maintain {target_percentage}%:\n"
                                            f"Attend at least {classes_needed} more classes — about {avg_classes_needed_per_week} per week.\n"
                                            f"You can bunk ~{bunkable_classes} classes/week.")
        except ValueError:
            result_label.configure(text="Please enter valid numbers.")

    ctk.CTkButton(window, text="Calculate", command=calculate_attendance_plan,
                  fg_color="#1e1e1e", hover_color="#2e2e2e", text_color="#1e90ff").pack(pady=10)

def open_todo_list():
    todo_window = ctk.CTkToplevel()
    todo_window.geometry("400x400")

    def add_task():
        task = task_entry.get().strip()
        if task:
            task_listbox.insert("end", task)
            with open("Todolist.txt", "a") as file:
                file.write(task + "\n")
            task_entry.delete(0, "end")

    def clear_tasks():
        task_listbox.delete(0, "end")
        open("Todolist.txt", "w").close()

    def load_tasks():
        try:
            with open("Todolist.txt", "r") as file:
                for line in file:
                    task_listbox.insert("end", line.strip())
        except FileNotFoundError:
            pass

    def delete_selected():
        selected = task_listbox.curselection()
        if selected:
            task_listbox.delete(selected)
            with open("Todolist.txt", "w") as file:
                for i in range(task_listbox.size()):
                    file.write(task_listbox.get(i) + "\n")

    task_entry = ctk.CTkEntry(todo_window, font=("Segoe UI", 12), width=250)
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
    window = ctk.CTkToplevel(root)
    window.geometry("350x500")

    def label(text):
        ctk.CTkLabel(window, text=text, font=("Segoe UI", 12), text_color="#1e90ff").pack(pady=5)

    label("Subject Name")
    subject_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    subject_entry.pack()

    label("ISA 1 Score (out of 40)")
    isa1_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    isa1_entry.pack()

    label("ISA 2 Score (out of 40)")
    isa2_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    isa2_entry.pack()

    label("Assignment Score (out of 10)")
    assignment_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    assignment_entry.pack()

    label("ESA Score (out of 100)")
    esa_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    esa_entry.pack()

    label("Lab Score (only for Chemistry/Python/Physics)")
    lab_entry = ctk.CTkEntry(window, font=("Segoe UI", 12))
    lab_entry.pack()

    result_label = ctk.CTkLabel(window, text="", font=("Segoe UI", 12), wraplength=300, justify="left", text_color="#1e90ff")
    result_label.pack(pady=20)

    def calculate_gpa():
        try:
            subject = subject_entry.get().strip().lower()
            isa1 = min(int(isa1_entry.get()), 40) / 2
            isa2 = min(int(isa2_entry.get()), 40) / 2
            assignment = min(int(assignment_entry.get()), 10)
            esa = min(int(esa_entry.get()), 100) / 2
            lab = 0
            total = 0
            max_score = 100

            if subject in ["chem", "python", "cs", "chemistry", "computer", "phy", "physics"]:
                lab = min(int(lab_entry.get()), 20)
                max_score = 120

            total = isa1 + isa2 + assignment + esa + lab
            scaled_total = (total / max_score) * 100

            grade = (
                "S" if scaled_total >= 90 else
                "A" if scaled_total >= 80 else
                "B" if scaled_total >= 70 else
                "C" if scaled_total >= 60 else
                "D" if scaled_total >= 50 else
                "F"
            )

            result_label.configure(text=f"Raw Score: {total}/{max_score}\nScaled Score: {scaled_total:.2f}/100\nGrade: {grade}")
        except ValueError:
            result_label.configure(text="Please enter valid numbers.")

    ctk.CTkButton(window, text="Calculate GPA", command=calculate_gpa,
                  fg_color="#1e1e1e", hover_color="#2e2e2e", text_color="#1e90ff").pack(pady=10)

# Main Window
root = ctk.CTk()
root.geometry("400x500")
root.title("Student Toolkit")

ctk.CTkLabel(root, text="Student Toolkit", font=("Segoe UI", 18, "bold"), text_color="#1e90ff").pack(pady=40)

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)

button_style = {
    "font": ("Segoe UI", 14),
    "width": 200,
    "height": 40,
    "fg_color": "#1e1e1e",
}
""