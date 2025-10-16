import tkinter as tk

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        with open("todolist.txt", "a") as file:
            file.write(task + "\n")
        task_entry.delete(0, tk.END)

def clear_tasks():
    task_listbox.delete(0, tk.END)
    open("todolist.txt", "w").close()  # clears file

def load_tasks():
    try:
        with open("todolist.txt", "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

def delete_selected():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
        with open("todolist.txt", "w") as file:
            for i in range(task_listbox.size()):
                file.write(task_listbox.get(i) + "\n")

# GUI setup
window = tk.Tk()
window.title("Aryan's To-Do List")
window.geometry("400x400")
window.config(bg="#1e1e1e")

task_entry = tk.Entry(window, font=("Segoe UI", 12), width=25)
task_entry.pack(pady=10)

tk.Button(window, text="Add Task", command=add_task, font=("Segoe UI", 12),
          bg="#1e90ff", fg="white").pack(pady=5)

task_listbox = tk.Listbox(window, font=("Segoe UI", 12), width=35, height=10)
task_listbox.pack(pady=10)

tk.Button(window, text="Delete Selected", command=delete_selected, font=("Segoe UI", 12),
          bg="#ff6347", fg="white").pack(pady=5)

tk.Button(window, text="Clear All", command=clear_tasks, font=("Segoe UI", 12),
          bg="#ff4500", fg="white").pack(pady=5)

load_tasks()
window.mainloop()

