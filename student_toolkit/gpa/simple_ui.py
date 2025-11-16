import customtkinter as ctk
from gpa.simple_logic import calculate_gpa

def open_gpa_calculator(root):
    gpa_window = ctk.CTkToplevel(root)
    gpa_window.title("GPA Calculator")
    gpa_window.geometry("520x550")
    gpa_window.configure(fg_colour="#000000")

    # UI and the textbox and labels for the marks and things
    def label(text):
        ctk.CTkLabel(gpa_window, text=text, font=("Segoe UI", 15), text_color="#ffffff").pack(pady=4)

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

    label("Lab Score (only for Chemistry/Python/Physics)(Out of 20)")
    lab_entry = ctk.CTkEntry(gpa_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    lab_entry.pack(pady=4)

    result_label = ctk.CTkLabel(gpa_window,text="",font=("Segoe UI", 15),wraplength=320,justify="left",text_color="#f4f4f4")
    result_label.pack(pady=10)

   
    def on_calculate():
        try:
            subject = subject_entry.get().strip().lower()
            isa1 = int(isa1_entry.get())
            isa2 = int(isa2_entry.get())
            assignment = int(assignment_entry.get())
            esa = int(esa_entry.get())
            lab = int(lab_entry.get() or 0)
            if 0>isa1>40 or 0>isa2>40 or 0>esa>100 or lab>20 or 0>assignment>10:
                result_label.configure(text="Marks entered are out of the defined values")
                return()
            

            total, max_score, scaled_total, grade = calculate_gpa(subject, isa1, isa2, assignment, esa, lab)

            result_label.configure(text=f"Raw Score: {total:.2f}/{max_score}\nScaled Score: {scaled_total:.2f}/100\nGrade: {grade}")

        except ValueError:
            result_label.configure(text="Please enter valid numbers.")

    ctk.CTkButton(gpa_window,text="Calculate GPA",command=on_calculate,text_color="#ffffff",corner_radius=8,height=40,width=160,hover_color= "#0E3C10",fg_color="#375638").pack(pady=10)
