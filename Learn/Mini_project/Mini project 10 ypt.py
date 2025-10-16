
import customtkinter as ctk
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class StudyTimerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Study Timer")
        self.geometry("400x300")

        # Subject handling
        self.subjects = []
        self.current_subject = ctk.StringVar(value="Select Subject")

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter Subject")
        self.entry.pack(pady=10)

        self.add_btn = ctk.CTkButton(self, text="Add Subject", command=self.add_subject)
        self.add_btn.pack(pady=5)

        self.dropdown = ctk.CTkOptionMenu(self, values=["No subjects yet"], variable=self.current_subject)
        self.dropdown.pack(pady=10)

        # Timer
        self.time_label = ctk.CTkLabel(self, text="00:00:00", font=("Arial", 24))
        self.time_label.pack(pady=20)

        self.start_btn = ctk.CTkButton(self, text="Start", command=self.start_timer)
        self.start_btn.pack(side="left", padx=20, pady=20)

        self.stop_btn = ctk.CTkButton(self, text="Stop", command=self.stop_timer)
        self.stop_btn.pack(side="left", padx=20)

        self.reset_btn = ctk.CTkButton(self, text="Reset", command=self.reset_timer)
        self.reset_btn.pack(side="left", padx=20)

        # Stopwatch vars
        self.running = False
        self.start_time = 0
        self.elapsed = 0

    def add_subject(self):
        subject = self.entry.get().strip()
        if subject and subject not in self.subjects:
            self.subjects.append(subject)
            self.dropdown.configure(values=self.subjects)
            self.entry.delete(0, "end")

    def update_timer(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            formatted = time.strftime("%H:%M:%S", time.gmtime(self.elapsed))
            self.time_label.configure(text=formatted)
            self.after(500, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.elapsed = 0
        self.time_label.configure(text="00:00:00")

if __name__ == "__main__":
    app = StudyTimerApp()
    app.mainloop()









def open_ypt():  # Function to open the "Study Timer" window
    ypt_window = ctk.CTkToplevel(root)  # Create a new top-level window inside the main root window
    ypt_window.title("Study Timer")  # Set the window title
    ypt_window.geometry("650x520")  # Set the window size (width x height)

    # Heading label at the top of the window
    ctk.CTkLabel(
        ypt_window, 
        text="Study Timer", 
        font=("Segoe UI", 24, "bold"), 
        text_color="#1e90ff"
    ).pack(pady=20)  # Add the label to the window with vertical padding

    subjects = {}  # Dictionary to store subjects and their total study times (in seconds)
    current_subject = tk.StringVar(value="Select Subject")  # Holds the currently selected subject

    # Entry box to type new subject names
    subject_entry = ctk.CTkEntry(
        ypt_window, 
        placeholder_text="Enter Subject", 
        corner_radius=15, 
        height=40, 
        width=240, 
        font=("Segoe UI", 16)
    )
    subject_entry.pack(pady=10)  # Place the entry box with some spacing

    def add_subject():  # Function to add a new subject
        subject = subject_entry.get().strip()  # Get text from entry box and remove spaces
        if subject=="" and subject not in subjects:  # Check if it's a valid and new subject
            subjects[subject] = 0  # Add to dictionary with 0 seconds
            subject_menu.configure(values=list(subjects.keys()))  # Update dropdown with new subject
            current_subject.set(subject)  # Select the new subject automatically
        subject_entry.delete(0, "end")  # Clear the entry box

    # Button to add subject when clicked
    ctk.CTkButton(
        ypt_window, 
        text="Add Subject", 
        command=add_subject,  # Runs add_subject() on click
        text_color="#1e90ff", 
        corner_radius=20, 
        height=40, 
        width=140
    ).pack(pady=5)  # Add button to the window with small padding

    # Dropdown menu to select current subject
    subject_menu = ctk.CTkOptionMenu(
        ypt_window, 
        values=["No subjects yet"],  # Initial state before subjects are added
        variable=current_subject  # Tied to current_subject variable
    )
    subject_menu.pack(pady=10)  # Add dropdown to window

    # Label to display the timer
    time_label = ctk.CTkLabel(
        ypt_window, 
        text="00:00:00", 
        font=("Segoe UI", 28, "bold"), 
        text_color="white"
    )
    time_label.pack(pady=15)  # Add timer label with spacing

    running = False  # Flag to check if timer is running
    start_time = 0  # Stores the timestamp when timer starts
    elapsed = 0  # Total elapsed time for current subject

    def update_timer():  # Updates timer display continuously
        nonlocal elapsed  # Allows access to outer 'elapsed' variable
        if running:  # Only run if timer is active
            elapsed = time.time() - start_time  # Calculate elapsed seconds
            formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed))  # Convert seconds to HH:MM:SS
            time_label.configure(text=formatted)  # Update the timer label
            ypt_window.after(500, update_timer)  # Call again every 0.5 seconds

    def start_timer():  # Function to start timer
        nonlocal running, start_time  # Access and modify outer variables
        current = current_subject.get()  # Get selected subject
        if not running and current != "Select Subject" and current in subjects:  # Ensure valid subject
            running = True  # Set timer as active
            start_time = time.time() - subjects[current]  # Resume from last saved time if any
            update_timer()  # Start updating the timer display

    def stop_timer():  # Function to stop the timer
        nonlocal running
        current = current_subject.get()
        if running and current in subjects:  # Stop only if running
            running = False  # Stop the timer
            subjects[current] = elapsed  # Save elapsed time for that subject

    def reset_timer():  # Function to reset timer to 00:00:00
        nonlocal running, elapsed
        running = False  # Stop the timer
        elapsed = 0  # Reset elapsed time
        current = current_subject.get()
        if current in subjects:
            subjects[current] = 0  # Reset saved time for that subject
            time_label.configure(text="00:00:00")  # Reset label display

    # Frame to hold Start, Stop, and Reset buttons
    btn_frame = ctk.CTkFrame(ypt_window)
    btn_frame.pack(pady=10)  # Add frame to window

    # Start button
    ctk.CTkButton(
        btn_frame, text="Start", command=start_timer,
        text_color="#1e90ff", corner_radius=20, width=90
    ).pack(side="left", padx=10)

    # Stop button
    ctk.CTkButton(
        btn_frame, text="Stop", command=stop_timer,
        text_color="#1e90ff", corner_radius=20, width=90
    ).pack(side="left", padx=10)

    # Reset button
    ctk.CTkButton(
        btn_frame, text="Reset", command=reset_timer,
        text_color="#1e90ff", corner_radius=20, width=90
    ).pack(side="left", padx=10)

    # Label above the stats box
    ctk.CTkLabel(
        ypt_window, 
        text="Study Time per Subject", 
        font=("Segoe UI", 16), 
        text_color="#1e90ff"
    ).pack(pady=10)

    # Text box to display time stats for each subject
    stats_box = tk.Text(
        ypt_window, height=8, width=40, 
        font=("Consolas", 13), 
        bg="#1e1e1e", fg="white"
    )
    stats_box.pack(pady=5)

    def update_stats():  # Function to refresh subject stats every second
        stats_box.delete("1.0", tk.END)  # Clear text box
        for subj, secs in subjects.items():  # Loop through all subjects
            formatted = time.strftime("%H:%M:%S", time.gmtime(secs))  # Format their times
            stats_box.insert(tk.END, f"{subj}: {formatted}\n")  # Display subject and time
        ypt_window.after(1000, update_stats)  # Update every 1 second

    update_stats()  # Start auto-updating the stats box
