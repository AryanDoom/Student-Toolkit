import customtkinter as ctk
from llm.doom_engine import ask_llm

def open_llm(root):
    llm_window = ctk.CTkToplevel(root)
    llm_window.title("Any Doubts you might have gets solved")
    llm_window.geometry("1000x1000")

    def label(text):
        ctk.CTkLabel(llm_window, text=text, font=("Segoe UI", 15), text_color="#006d12").pack(pady=(15, 5))

    label("Enter your doubt (Please enter exit if conversation is completed).")

    # UI for the response box and the doubt text box
    llm_entry = ctk.CTkEntry(llm_window, font=("Segoe UI", 15), corner_radius=12, height=33, width=500)
    llm_entry.pack(pady=(12, 6))

    response_box = ctk.CTkTextbox(llm_window, width=850, height=400, wrap="word", font=("Segoe UI", 15))
    response_box.pack(pady=15)

    def get_answer():
        user_doubt = llm_entry.get().strip()

        if user_doubt.lower() == "exit":
            llm_window.destroy()
            return

        if user_doubt == "":
            response_box.insert("end", " Please enter a question.\n\n")
            return

        try:
            reply = ask_llm(user_doubt)

            response_box.insert(
                "end",
                f" You: {user_doubt}\n\n=> Response: {reply}\n\n"
            )
            response_box.see("end")
            llm_entry.delete(0, "end")  # clears the text (doubt ) box

        except Exception as e:
            response_box.insert("end", f" Error: {e}\n\n")

    ctk.CTkButton(
        llm_window,
        text="Calculate Response",
        command=get_answer,
        text_color="#000000",
        corner_radius=15,
        height=40,
        width=160
    ).pack(pady=10)
