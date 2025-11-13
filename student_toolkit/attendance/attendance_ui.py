import customtkinter as ctk
from attendance.attendance_logic import calculate_attendance

def open_attendance_calculator(root):
    window = ctk.CTkToplevel(root)
    window.title("Attendance Predictor")
    window.geometry("900x600")

    # labels and the button
    ctk.CTkLabel(window, text="Current Attendance %", font=("Segoe UI", 18)).pack(pady=10)
    current_entry = ctk.CTkEntry(window, font=("Segoe UI", 18), corner_radius=15, height=40, width=200)
    current_entry.pack(pady=10)

    ctk.CTkLabel(window, text="Target Attendance %", font=("Segoe UI", 18)).pack(pady=10)
    target_entry = ctk.CTkEntry(window, font=("Segoe UI", 18), corner_radius=15, height=40, width=200)
    target_entry.pack(pady=10)

    result_label = ctk.CTkLabel(
        window,
        text="",
        font=("Segoe UI", 16),
        text_color="#1e90ff",
        wraplength=500,
        justify="left"
    )
    result_label.pack(pady=10)

    #-----------------Backend of the calculator-----------------------
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

    ctk.CTkButton(
        window,
        text="Calculate",
        command=calculate_attendance_plan,
        text_color="#1e90ff",
        corner_radius=20,
        height=44,
        width=160
    ).pack(pady=18)
