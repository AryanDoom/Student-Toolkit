import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TimetablePlanner(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Week Timetable Planner")
        self.geometry("800x600")
        self.day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Storage of activities: dict day->hour->string
        # Initialize empty dict for each day and hour 6am to 11pm
        self.schedule = {day: {h: "" for h in range(6, 24)} for day in self.day_names}
        
        # Create tab view for each day
        self.tabview = ctk.CTkTabview(self, width=780, height=520)
        self.tabview.pack(pady=20, padx=15, fill="both", expand=True)
        
        for day in self.day_names:
            self.tabview.add(day)
            self.create_day_tab(day)
        
        # Save & clear buttons below tabs
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=5)
        save_btn = ctk.CTkButton(btn_frame, text="Print Schedule to Console", command=self.print_schedule)
        save_btn.grid(row=0, column=0, padx=10)
        clear_btn = ctk.CTkButton(btn_frame, text="Clear Current Day", command=self.clear_current_day)
        clear_btn.grid(row=0, column=1, padx=10)
        




    def create_day_tab(self, day):
        frame = self.tabview.tab(day)
        
        # Scrollable frame to hold hourly schedule
        canvas = tk.Canvas(frame, bg="#222222", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # For each hour from 6 AM to 11 PM, create an entry and label
        for hour in range(6, 24):
            hour_12h = hour % 12 if hour % 12 != 0 else 12
            am_pm = "AM" if hour < 12 else "PM"
            time_label = ctk.CTkLabel(scrollable_frame, text=f"{hour_12h} {am_pm}", width=50, anchor="w",
                                      font=("Segoe UI", 14), text_color="#1e90ff")
            time_label.grid(row=hour-6, column=0, padx=10, pady=5, sticky="w")
            
            # Create entry widget for activity input
            entry = ctk.CTkEntry(scrollable_frame, width=600, font=("Segoe UI", 14), corner_radius=10)
            entry.grid(row=hour-6, column=1, padx=10, pady=5, sticky="ew")
            
            # Pre-fill from stored schedule if exists
            entry.insert(0, self.schedule[day][hour])
            
            # Save the entry widget reference to update storage on change
            def save_text(event, day=day, hour=hour, ent=entry):
                self.schedule[day][hour] = ent.get()
            
            entry.bind("<FocusOut>", save_text)
            
            # Allow expanding the entry when resizing window
            scrollable_frame.grid_columnconfigure(1, weight=1)
    
    def print_schedule(self):
        print("Weekly Schedule:")
        for day in self.day_names:
            print(f"\n{day}:")
            for hour in range(6, 24):
                activity = self.schedule[day][hour]
                if activity.strip():
                    hour_12h = hour % 12 if hour % 12 != 0 else 12
                    am_pm = "AM" if hour < 12 else "PM"
                    print(f"  {hour_12h} {am_pm}: {activity.strip()}")
    
    def clear_current_day(self):
        current_day = self.tabview.get()
        for hour in range(6, 24):
            self.schedule[current_day][hour] = ""
        
        tab_frame = self.tabview.tab(current_day)
        # Clear all entries in current tab
        for widget in tab_frame.winfo_children():
            if isinstance(widget, tk.Canvas):
                for inner in widget.winfo_children():
                    if isinstance(inner, ctk.CTkFrame):
                        for entry in inner.winfo_children():
                            if isinstance(entry, ctk.CTkEntry):
                                entry.delete(0, tk.END)

if __name__ == "__main__":
    app = TimetablePlanner()
    app.mainloop()
""