def open_qr_code():
    qr_window= ctk.CTkToplevel(root)
    qr_window.title("QR Code for Every TextBook Needed")
    qr_window.geometry("520x550")

    def label(text):
        ctk.CTkLabel(qr_window, text=text, font=("Segoe UI", 15), text_color="#1e90ff").pack(pady=4)

    label("Enter the Subject you would like the book for")
    book_entry=  ctk.CTkEntry(qr_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=190)
    book_entry.pack(pady=4)  
    qr_label = ctk.CTkLabel(qr_window, text="")  
    qr_label.pack(pady=10)

    def generate_qr():
        subject = book_entry.get().strip().lower()
        if subject=="":
            qr_label.configure(text="Please enter a subject name.")
            return

        elif subject=="maths1":
            book_url = f"https://drive.google.com/drive/folders/1gYFT1RvJD5XmsquB99-vXC5xBWV9EzZZ{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  

        elif subject=="maths2":
            book_url = f"https://drive.google.com/drive/folders/1iaewOilIhQZZgfCKqDJeFC2lty7g9AQk{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        elif subject=="chemistry": 
            book_url = f"https://drive.google.com/drive/folders/1yHNKMxDFvf_FopJ-ZCDNKRlGleTFQZcN{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        elif subject=="mechanics": 
            book_url = f"https://drive.google.com/drive/folders/1JGEaaw-j-tzMTEhRoxM7gmtSEaK2ZT5j{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        elif subject=="epd": 
            book_url = f"https://drive.google.com/drive/folders/1rkUuM3-W249sFgl1Eqn6zbx29AaTCHLB{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img 


        elif subject=="placeholder": 
            book_url = f"https://textbooks.example.com/{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        elif subject=="python": 
            book_url = f"https://drive.google.com/file/d/17cVJ_8MPCULzXPcgt4if4O6fBAsfy1Uc/view{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img 


        elif subject=="physics": 
            book_url = f"https://drive.google.com/file/d/1KwxEcR4klXQwS-uKcO16PXHQPMmHDCAj/view{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img    


        elif subject=="electrical": 
            book_url = f"https://drive.google.com/drive/folders/16UDSJJ4c4N3StFjDbvdwRFuV-gFfWT3S{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        elif subject=="physicslab": 
            book_url = f"https://drive.google.com/file/d/1GMoZGnNMitVkx-VvcuIWr3qAQD7fnhqK/view{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img   


        elif subject=="constitution": 
            book_url = f"https://drive.google.com/drive/folders/1viBbRv-CGnwFGfJLcC2os6t90fpMwQuG{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        elif subject=="evs": 
            book_url = f"https://drive.google.com/file/d/1IKXMDt1LeoBH4uyD7LiQx_8BmQaLbR0K/view?usp=drive_link{subject.replace(' ', '_').lower()}"

            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(book_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e90ff", back_color="black")

        
            img = img.resize((200, 200))
            tk_img = ImageTk.PhotoImage(img)
            qr_label.configure(image=tk_img, text="")
            qr_label.image = tk_img  


        else:
             qr_label.configure(text="We dont have said subjects book (I am working tirelessly to add it )")
             return 
        













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




