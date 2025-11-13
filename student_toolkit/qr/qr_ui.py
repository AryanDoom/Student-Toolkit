import customtkinter as ctk
from tkinter import StringVar
from PIL import ImageTk
from qr.qr_logic import generate_qr_image

def open_qr_code(root):
    qr_window = ctk.CTkToplevel(root)
    qr_window.title("QR Code for Every TextBook Needed")
    qr_window.geometry("520x550")

    def label(text):
        ctk.CTkLabel(qr_window, text=text, font=("Segoe UI", 15), text_color="#1e90ff").pack(pady=4)

    label("Select the Subject you would like the book for")

    subject_var = StringVar(value="")  #add the subjects here

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
        ctk.CTkRadioButton(
            qr_window,
            text=label_text,
            variable=subject_var,
            value=value
        ).pack(anchor="center", padx=20)

    qr_label = ctk.CTkLabel(qr_window, text="")
    qr_label.pack(pady=10)

    def generate_qr():
        subject = subject_var.get()

        if subject == "":
            qr_label.configure(text="Please select a subject.")
            return

        img = generate_qr_image(subject)
        tk_img = ImageTk.PhotoImage(img)

        qr_label.configure(image=tk_img, text="")
        qr_label.image = tk_img

    ctk.CTkButton(qr_window, text="Generate QR Code", command=generate_qr).pack(pady=10)
