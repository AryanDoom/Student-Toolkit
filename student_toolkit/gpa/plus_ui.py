import customtkinter as ctk
from tkinter import messagebox
from gpa.plus_logic import (calculate_sgpa_letter,calculate_sgpa_marks,calculate_cgpa,ms_calc_total,grade_points)

def open_gpa_plus(root):

    # window and frame shit needed
    gpa_plus_window = ctk.CTkToplevel(root)
    gpa_plus_window.title("GPA Calculator ++")
    gpa_plus_window.geometry("1000x720")
    gpa_plus_window.configure(fg_color="#000000")

    gpa_plus_window.lift()
    gpa_plus_window.focus_force()
    gpa_plus_window.grab_set()


    #Buttons
    ctk.CTkLabel(gpa_plus_window, text="GPA Calculator ++",font=("Agency FB", 34, "bold"), text_color="#ffffff").pack(pady=25)
#frame for the buttons
    navigation_frame = ctk.CTkFrame(gpa_plus_window, fg_color="transparent")
    navigation_frame.pack(pady=(10, 20))

#button style 
    btn_style = {"corner_radius": 8,"width": 220,"height": 50,"font": ("Agency FB", 16, "bold"),'hover_color': "#0E3C10",'fg_color':"#375638","text_color": "#ffffff",}

#frame for the frame
    container =ctk.CTkFrame(gpa_plus_window, fg_color="#232323", corner_radius=8)
    container.pack(expand=True, padx=20, pady=20)

#frames for the info
    letter_frame = ctk.CTkFrame(container, fg_color="#000000")
    marks_frame = ctk.CTkFrame(container, fg_color="#000000")
    cgpa_frame = ctk.CTkFrame(container, fg_color="#000000")

    for f in (letter_frame, marks_frame, cgpa_frame):
        f.grid(row=0, column=0, sticky="nsew") #grid setting for the info inner frames

    def show_frame(f):
        f.tkraise()#brings out the clicked frame above all 

#All the buttons for the 3 things
    ctk.CTkButton(navigation_frame, text="Letter Grades → SGPA",
                  command=lambda: show_frame(letter_frame), **btn_style).pack(side="left", padx=10)

    ctk.CTkButton(navigation_frame, text="Marks → SGPA",
                  command=lambda: show_frame(marks_frame), **btn_style).pack(side="left", padx=10)

    ctk.CTkButton(navigation_frame, text="SGPAs → CGPA",
                  command=lambda: show_frame(cgpa_frame), **btn_style).pack(side="left", padx=10)

    # LETTER GRADES UI
    ctk.CTkLabel(letter_frame, text="Letter Grades → SGPA",font=("Agency FB", 28, "bold"), text_color="#ffffff").pack(pady=(20, 10))

    ctk.CTkLabel(letter_frame, text="Number of Subjects:", font=("Agency FB", 18)).pack()

    #letter grade and credits textbox
    lg_entry = ctk.CTkEntry(letter_frame, width=120, height=40,font=("Agency FB", 16), justify="center")
    lg_entry.pack(pady=8)

    lg_entries = []
    lg_scroll = ctk.CTkScrollableFrame(letter_frame, width=880, height=260,label_text="Enter Grades and Credits")
    lg_scroll.pack(pady=10)

    #Creating the fields and checking if there are pre existing entries available in the window
    def create_lg_fields():
        for w in lg_scroll.winfo_children():
            w.destroy()
        lg_entries.clear()

        try:
            n = int(lg_entry.get())
            if n <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter valid number of subjects!")
            return

        for i in range(n):
            row = ctk.CTkFrame(lg_scroll, fg_color="#111111")
            row.pack(fill="x", padx=20, pady=6)

            ctk.CTkLabel(row, text=f"Subject {i+1}",font=("Agency FB", 15, "bold"), width=120).pack(side="left", padx=10)

            grade_box = ctk.CTkComboBox(row, values=list(grade_points.keys()), width=100)
            grade_box.set("S")
            grade_box.pack(side="left", padx=10)

            credit_box = ctk.CTkEntry(row, width=100,placeholder_text="Credits", justify="center")
            credit_box.pack(side="left", padx=10)

            lg_entries.append((grade_box, credit_box))

    def calculate_lg_sgpa():
        try:
            entries = []
            for gb, ce in lg_entries:
                grade = gb.get().upper()
                credit = float(ce.get())
                entries.append((grade, credit))

            sgpa = calculate_sgpa_letter(entries)

            popup = ctk.CTkToplevel(gpa_plus_window)
            popup.title("SGPA Result")
            popup.geometry("300x150")
            popup.configure(fg_color="#000000")
            ctk.CTkLabel(popup, text=f"SGPA: {sgpa}",font=("Agency FB", 28, "bold"),text_color="#ffffff").pack(expand=True)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    btn_box = ctk.CTkFrame(letter_frame, fg_color="transparent")
    btn_box.pack(pady=10)

    ctk.CTkButton(btn_box, text="Create Fields",
                  command=create_lg_fields, **btn_style).pack(side="left", padx=15)

    ctk.CTkButton(btn_box, text="Calculate SGPA",
                  command=calculate_lg_sgpa, **btn_style).pack(side="left", padx=15)

    # MARKS UI
    ctk.CTkLabel(marks_frame, text="Marks → SGPA",font=("Agency FB", 28, "bold"), text_color="#ffffff").pack(pady=(20, 10))

    ctk.CTkLabel(marks_frame, text="Number of Subjects:", font=("Agency FB", 18)).pack()
    ms_entry = ctk.CTkEntry(marks_frame, width=120, height=40,
                            font=("Agency FB", 16), justify="center")
    ms_entry.pack(pady=8)

    ms_entries = []
    ms_scroll = ctk.CTkScrollableFrame(marks_frame, width=880, height=260, label_text="Enter Marks")
    ms_scroll.pack(pady=10)

    # backend for the marks to sgpa calc
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

            ctk.CTkLabel(row, text=f"Subject {i+1}",font=("Agency FB", 15, "bold"), width=120).pack(side="left", padx=10)

            boxes = []
            for h in headers:
                box = ctk.CTkFrame(row, fg_color="transparent")
                box.pack(side="left", padx=6)
                ctk.CTkLabel(box, text=h).pack()
                e = ctk.CTkEntry(box, width=70, justify="center")
                e.pack()
                boxes.append(e)

            ms_entries.append(boxes)

    def calculate_ms_sgpa():
        try:
            rows = []
            for row in ms_entries:
                isa1, isa2, assignment, esa, lab, credit = [float(x.get() or 0) for x in row]
                rows.append((isa1, isa2, assignment, esa, lab, credit))

            sgpa = calculate_sgpa_marks(rows)

            popup = ctk.CTkToplevel(gpa_plus_window)
            popup.title("SGPA Result")
            popup.geometry("300x150")
            popup.configure(fg_color="#232323")
            ctk.CTkLabel(popup, text=f"SGPA: {sgpa}",font=("Agency FB", 28, "bold"),text_color="#ffffff").pack(expand=True)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    btn_box2 = ctk.CTkFrame(marks_frame, fg_color="transparent")
    btn_box2.pack(pady=10)

    ctk.CTkButton(btn_box2, text="Create Fields",
                  command=create_ms_fields, **btn_style).pack(side="left", padx=15)

    ctk.CTkButton(btn_box2, text="Calculate SGPA",
                  command=calculate_ms_sgpa, **btn_style).pack(side="left", padx=15)

    # CGPA UI
    ctk.CTkLabel(cgpa_frame, text="SGPAs → CGPA",font=("Agency FB", 28, "bold"), text_color="#ffffff").pack(pady=(20, 10))

    ctk.CTkLabel(cgpa_frame, text="Number of Semesters:", font=("Agency FB", 18)).pack()
    cg_entry = ctk.CTkEntry(cgpa_frame, width=120, height=40,
                            font=("Agency FB", 16), justify="center")
    cg_entry.pack(pady=8)

    cg_entries = []
    cg_scroll = ctk.CTkScrollableFrame(cgpa_frame, width=880, height=260,label_text="Enter SGPA for Each Semester")
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
            row = ctk.CTkFrame(cg_scroll, fg_color="#111111")
            row.pack(fill="x", padx=20, pady=6)

            ctk.CTkLabel(row, text=f"Semester {i+1}",font=("Agency FB", 15, "bold"), width=160).pack(side="left", padx=10)

            e = ctk.CTkEntry(row, width=200, height=36,justify="center", placeholder_text="Enter SGPA")
            e.pack(side="left", padx=10)
            cg_entries.append(e)

    def calculate_cgpa_ui():
        try:
            values = []
            for e in cg_entries:
                val = e.get().strip()
                if val == "":
                    continue
                sg = float(val)
                if not (0 <= sg <= 10):
                    raise ValueError("SGPA must be between 0 and 10.")
                values.append(sg)

            cgpa = calculate_cgpa(values)

            popup = ctk.CTkToplevel(gpa_plus_window)
            popup.title("CGPA Result")
            popup.geometry("300x150")
            popup.configure(fg_color="#000000")
            ctk.CTkLabel(popup, text=f"CGPA: {cgpa}",font=("Agency FB", 28, "bold"),text_color="#1e90ff").pack(expand=True)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    btn_box3 = ctk.CTkFrame(cgpa_frame, fg_color="transparent")
    btn_box3.pack(pady=10)

    ctk.CTkButton(btn_box3, text="Create Fields",
                  command=create_cg_fields, **btn_style).pack(side="left", padx=15)

    ctk.CTkButton(btn_box3, text="Calculate CGPA",
                  command=calculate_cgpa_ui, **btn_style).pack(side="left", padx=15)

    show_frame(letter_frame)
