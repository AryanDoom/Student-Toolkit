import customtkinter as ctk
from tkinter import StringVar
from PIL import ImageTk
import webbrowser
from qr.qr_logic import generate_qr_image
from qr.qr_logic import url_map

#The main window for the application
def open_qr_code(root):
    qr_window = ctk.CTkToplevel(root)
    qr_window.title("QR Code Library")
    qr_window.geometry("520x700")
    qr_window.configure(fg_color="#1a1a1a")

    # ---------- HEADER ----------
    title = ctk.CTkLabel(qr_window,text=" Textbook QR Generator",font=("Segoe UI", 24, "bold"),text_color="#1e90ff")
    title.pack(pady=(20, 10))

    # ---------- Subject selecting frame----------
    select_frame = ctk.CTkFrame(qr_window, fg_color="#232323", corner_radius=15)
    select_frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(select_frame,text="Select the subject:",font=("Segoe UI", 16, "bold"),text_color="#e0e0e0").pack(pady=(10, 5))

    subject_var = StringVar(value="")

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

#frame for the radio buttons
    scroll_frame = ctk.CTkScrollableFrame(select_frame,fg_color="#232323",corner_radius=15,width=450,height=220)
    scroll_frame.pack(pady=10, padx=10, fill="x")

    for label_text, value in subjects.items():
        ctk.CTkRadioButton(
            scroll_frame,
            text=label_text,
            variable=subject_var,
            value=value,
            font=("Segoe UI", 14),
            text_color="#c9c9c9",
        ).pack(anchor="center", pady=4, padx=10)



    qr_display_frame = ctk.CTkFrame(qr_window,fg_color="#232323",corner_radius=15)
    qr_display_frame.pack(pady=20, padx=20, fill="both", expand=True)

    qr_label = ctk.CTkLabel(qr_display_frame,text="",anchor="center")
    qr_label.pack(pady=15)   

    # ---------- the link -------------------
    link_label = ctk.CTkLabel( qr_window, text="", font=("Segoe UI", 14), text_color="#1e90ff", cursor="hand2")
    link_label.pack(pady=5)

    def open_link(event):
        webbrowser.open(link_label.cget("text"))

    link_label.bind("<Button-1>", open_link)

    # ---------- BUTTON ----------
    def generate_qr():
        subject = subject_var.get()

        if subject == "":
            qr_label.configure(text="Please select a subject.",font=("Segoe UI", 16),text_color="#1e90ff")
            link_label.configure(text="")
            return

        # making the qr code
        img = generate_qr_image(subject)
        tk_img = ImageTk.PhotoImage(img)

        qr_label.configure(image=tk_img, text="")
        qr_label.image = tk_img

        # configuring the link after its selected
        link_label.configure(text=url_map.get(subject, ""))

    btn_frame = ctk.CTkFrame(qr_window, fg_color="#1a1a1a")
    btn_frame.pack(pady=(5, 20))

    ctk.CTkButton(btn_frame,text="Generate QR Code",command=generate_qr,corner_radius=12,height=40,fg_color="#1e90ff",hover_color="#1877cc",text_color="#000001",font=("Segoe UI", 16)
    ).pack(padx=2)

