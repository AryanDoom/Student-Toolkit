import customtkinter as ctk
import tkinter as tk
from llm.doom_engine_genai import what_would_doom_do

#Main window 
def open_llm(root):
    llm_window = ctk.CTkToplevel(root)
    llm_window.title("DOOM Bot - Doubt Solver")
    llm_window.geometry("900x700")
    llm_window.configure(fg_color="#000000")   

    # ----- HEADER -----
    header = ctk.CTkLabel(llm_window,text=" DOOM Bot - Ask Your Doubts",font=("Segoe UI", 28, "bold"),text_color="#ffffff")
    header.pack(pady=20)

    # ----- Chat frame -----------
    chat_frame = ctk.CTkFrame(llm_window, fg_color="#1e1e1e", corner_radius=15)
    chat_frame.pack(pady=10, padx=20, fill="both", expand=True)

    response_box = ctk.CTkTextbox(chat_frame,width=820,height=450,wrap="word",font=("Segoe UI", 15),fg_color="#000000",corner_radius=8,text_color="White")
    response_box.pack(padx=10, pady=10, fill="both", expand=True)

    # ----- INPUT AREA -----
    input_frame = ctk.CTkFrame(llm_window, fg_color="#121212")
    input_frame.pack(fill="x", pady=10, padx=20)

    llm_entry = ctk.CTkEntry(input_frame,font=("Segoe UI", 15),corner_radius=12,height=40)
    llm_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

    ask_btn = ctk.CTkButton(input_frame,text="Ask",command=lambda: get_answer(),hover_color= "#0E3C10",fg_color="#375638",text_color="White",corner_radius=10,width=120,height=40)
    ask_btn.pack(side="right")

    # -----  -----
    def get_answer():
        user_doubt = llm_entry.get().strip()

        if not user_doubt:
            response_box.insert("end", "Please enter a question.\n\n")
            return

        if user_doubt.lower() == "exit":
            llm_window.destroy()
            return

        try:
            reply = what_would_doom_do(user_doubt)

            import datetime
            time_now = datetime.datetime.now().strftime("[%H:%M]")

            response_box.insert("end", f"{time_now} You: {user_doubt}\n")
            response_box.insert("end", f"{time_now} DOOM Bot: {reply}\n\n")
            response_box.see("end")
            llm_entry.delete(0, "end")  # clears the text (doubt ) box

        except Exception as e:
            response_box.insert("end", f"Error: {e}\n\n")

        llm_entry.delete(0, "end")
