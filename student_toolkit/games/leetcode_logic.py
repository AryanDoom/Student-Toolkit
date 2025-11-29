import customtkinter as ctk
import pandas as pd


def open_leetcode(root):
# load said dataset
    questions = pd.read_csv(r"C:\Users\aryan\OneDrive\Documents\Code\Student-Toolkit\student_toolkit\games\leetcode_dataset - lc.csv") #has about 1875 leetcode questions

    # Global index
    current_index = 0 #traversing through the dataset

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    #main window 
    q_window = ctk.CTk()
    q_window.title("DSA related problems")
    q_window.geometry("1100x700")
    q_window.configure(fg_colour="#000000")

    #main frame
    main = ctk.CTkFrame(q_window, fg_color="#000000", corner_radius=18)
    main.pack(fill="both", expand=True, padx=20, pady=20)

    # question title
    title_label = ctk.CTkLabel(main, text="", font=("Agency FB", 26, "bold"),text_color="white", anchor="w", justify="left")
    title_label.pack(pady=10,anchor="c")

    #difficulty badge
    diff_label = ctk.CTkLabel(main, text="", font=("Agency FB", 18, "bold"),corner_radius=12,fg_color="#333333",text_color="white",padx=10, pady=5)
    diff_label.pack(anchor="w",padx=10,pady=5)

    #acceptance rate
    acc_label = ctk.CTkLabel(main, text="", font=("Agency FB", 16), text_color="#ffffff")
    acc_label.pack(anchor="w", pady=10,padx=5)

    #question
    desc_box = ctk.CTkTextbox(main, width=1000, height=450,font=("Agency FB", 15),wrap="word")
    desc_box.pack(pady=10,padx=5)


    #to show the quetion
    def show_question():
        nonlocal current_index

        q = questions.iloc[current_index]

        #showing the title of the question
        title_label.configure(text=f"{q['id']}. {q['title']}")

        #showing the difficulty badge
        diff = q["difficulty"]
        if diff == "Easy":
            color = "#00ff6a"
        elif diff == "Medium":
            color = "#faaf00"
        else:
            color = "#ff0000"

        diff_label.configure(text=diff, fg_color=color)

        #showing the acceptance rate
        acc_label.configure(text=f"Acceptance Rate: {q['acceptance_rate']}%")


        #clearing the discription and putting new discription
        desc_box.delete("1.0", "end")
        desc_box.insert("end", q["description"])

    #to go to the next question
    def next_question():
        nonlocal current_index
        if current_index < len(questions) - 1:
            current_index += 1
            show_question()

    #to go back to the previous question
    def prev_question():
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            show_question()


    #the buttons
    btn_frame = ctk.CTkFrame(main, fg_color="#000000")
    btn_frame.pack(pady=10)

    prev_btn = ctk.CTkButton(btn_frame, text=" Previous", width=140, command=prev_question,corner_radius=5)
    prev_btn.grid(row=0, column=0, padx=20)

    next_btn = ctk.CTkButton(btn_frame, text="Next ", width=140, command=next_question,corner_radius=5)
    next_btn.grid(row=0, column=1, padx=20)

    # Load first question
    show_question()

    q_window.mainloop()
