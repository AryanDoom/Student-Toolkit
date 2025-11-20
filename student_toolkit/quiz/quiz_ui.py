import customtkinter as ctk
import json
import ollama


def open_quiz(root):
    quiz_window = ctk.CTkToplevel(root)
    quiz_window.title("Quiz Centre")
    quiz_window.geometry("600x650")
    quiz_window.configure(fg_color="#000000")

    # ---------- TOP FRAME ----------
    top_frame = ctk.CTkFrame(quiz_window, fg_color="#000000", corner_radius=0, height=200)
    top_frame.pack(fill="x")

    ctk.CTkLabel(top_frame, text="Subject Name", font=("Agency FB", 20, "bold")).pack(pady=10)
    subject_entry_user = ctk.CTkEntry(top_frame, font=("Agency FB", 18), corner_radius=5, height=40, width=300)
    subject_entry_user.pack()

    ctk.CTkLabel(top_frame, text="Topic / Niche", font=("Agency FB", 20, "bold")).pack(pady=10)
    topic_entry_user = ctk.CTkEntry(top_frame, font=("Agency FB", 18), corner_radius=5, height=40, width=300)
    topic_entry_user.pack()

    # ---------- RESULT FRAME ----------
    result_frame = ctk.CTkFrame(quiz_window, fg_color="#000000")
    result_frame.pack(fill="both", expand=True, pady=10)

    question_label = ctk.CTkLabel(result_frame, text="", font=("Agency FB", 20, "bold"), wraplength=500)
    question_label.pack(pady=20)

    option_buttons = []  # will store the 4 option buttons

    # ---------- MCQ GENERATION LOGIC ----------
    def generate_mcq():
        # get input from entries
        subject = subject_entry_user.get()
        topic = topic_entry_user.get()

        if subject == "" or topic == "":
            question_label.configure(text=" Please enter BOTH subject and topic!")
            return

        # ---- prompt for the LLM ----
        user_input = f"""
                    Create ONE multiple choice question on subject '{subject}', topic '{topic}'.
                    Return ONLY this JSON (no explanation, no formatting outside JSON):
{{
  "question": "text",
  "options": ["A", "B", "C", "D"],
  "answer": "correct option text"
}}
"""

        try:

            response = ollama.chat(
                model="DOOM_BOT_ASSITANT",
                messages=[{"role": "user", "content": user_input}]
            )

            reply = response["message"]["content"]

            data = json.loads(reply)

            question_text = data["question"]
            options = data["options"]
            correct_answer = data["answer"]

            # ---- DISPLAY QUESTION ----
            question_label.configure(text=question_text)

            # delete old buttons if they exist
            for btn in option_buttons:
                btn.destroy()
            option_buttons.clear()

            # ---- BUTTON LOGIC ----
            def check_answer(index):
                if options[index] == correct_answer:
                    question_label.configure(text=f" Correct!\n\n{question_text}")
                else:
                    question_label.configure(text=f" Wrong!\nCorrect answer: {correct_answer}")

            # create 4 option buttons
            for i in range(4):
                btn = ctk.CTkButton(result_frame,text=options[i],font=("Agency FB", 18),width=400,height=50,corner_radius=5,command=lambda x=i: check_answer(x))
                btn.pack(pady=8)
                option_buttons.append(btn)

        except Exception as e:
            question_label.configure(text=f"Error: {e}")

    ctk.CTkButton(top_frame,text="Generate MCQ",font=("Agency FB", 20, "bold"),height=50,width=200,fg_color="#3d6335",hover_color="#094022",command=generate_mcq).pack(pady=15)











