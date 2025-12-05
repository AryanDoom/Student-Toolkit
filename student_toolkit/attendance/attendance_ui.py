import customtkinter as ctk
from attendance.attendance_logic import calculate_attendance

def open_attendance_calculator(root):
    window_attendance = ctk.CTkToplevel(root)
    window_attendance.title("Attendance Predictor")
    window_attendance.geometry("900x600")
    window_attendance.configure(fg_color="#111111")

    window_attendance.lift()
    window_attendance.focus_force()
    window_attendance.grab_set()


    # labels and the button
    ctk.CTkLabel(window_attendance, text="Current Attendance %", font=("Agency FB", 18)).pack(pady=10)
    current_entry = ctk.CTkEntry(window_attendance, font=("Agency FB", 18), corner_radius=8, height=40, width=200)
    current_entry.pack(pady=10)

    ctk.CTkLabel(window_attendance, text="Target Attendance %", font=("Agency FB", 18)).pack(pady=10)
    target_entry = ctk.CTkEntry(window_attendance, font=("Agency FB", 18), corner_radius=8, height=40, width=200)
    target_entry.pack(pady=10)

    result_label = ctk.CTkLabel(window_attendance,text="",font=("Agency FB", 16),text_color="#ffffff",wraplength=500,justify="left")
    result_label.pack(pady=10)

    #-----------------Backend of the calculator--------------------------------------------
    def calculate_attendance_plan():
        try:
            current_percentage = int(current_entry.get())  # getting the info from the text boxes
            target_percentage = int(target_entry.get())

            result = calculate_attendance(current_percentage, target_percentage)

            if "error" in result:
                result_label.configure(text=result["error"])
                return

            if "warning" in result:
                result_label.configure(text=result["warning"])
                return

            # configured to show the label change when needed
            txt = (
                f"You need to attend {result['classes_needed']} classes out of the remaining {result['total_left']} classes to reach {target_percentage}%.\n"
                f"That's about {result['avg_week']:.0f} classes/week.\n"
                f"You can bunk ~{result['bunk_week']:.0f} classes/week, or about {result['bunk_total']} classes total."
            )

            result_label.configure(text=txt)

        except ValueError:
            result_label.configure(text="Please enter valid numbers.")  # to catch all the error and out of bound values

    ctk.CTkButton(window_attendance,text="Calculate",command=calculate_attendance_plan,text_color="#ffffff",corner_radius=20,height=44,width=160,hover_color= "#0E3C10",fg_color="#375638").pack(pady=18)
