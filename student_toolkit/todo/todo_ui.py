import customtkinter as ctk
import tkinter as tk
from todo.file_ops import (save_task,clear_all_tasks,load_tasks_from_file,save_tasks_after_delete)

def open_todo_list(root):
    todo_window = ctk.CTkToplevel(root)
    todo_window.title("Your To-Do List")
    todo_window.geometry("500x400")
    todo_window.configure(fg_color="#111111")

    #add tasks
    def add_task():
        task = task_entry.get().strip()
        if task:
            task_listbox.insert(tk.END, task)
            save_task(task)
            task_entry.delete(0, tk.END)

    #delete all tasks
    def clear_tasks():
        task_listbox.delete(0, tk.END)
        clear_all_tasks()

    #check file if tasks exisst , if yes load said tasks
    def load_tasks():
        tasks = load_tasks_from_file()
        for t in tasks:
            task_listbox.insert(tk.END, t)

    # deleting tasks if selected (1 at a time)
    def delete_selected():
        selected = task_listbox.curselection()  # this selects the task clicked
        for index in reversed(selected):
            task_listbox.delete(index)
        save_tasks_after_delete(task_listbox)

    task_entry = ctk.CTkEntry(todo_window,font=("Segoe UI", 18),width=280,corner_radius=15,height=36)
    task_entry.pack(pady=10)

    ctk.CTkButton(todo_window,text="Add Task",command=add_task,text_color="white",corner_radius=5,height=36,width=130,hover_color= "#0E3C10",fg_color="#375638").pack(pady=5)

    task_listbox = tk.Listbox(todo_window,font=("Segoe UI", 15),width=40,height=12,selectbackground="#ffffff",selectforeground="Black")
    task_listbox.pack(pady=10)

    ctk.CTkButton(todo_window,text="Delete Selected",command=delete_selected,text_color="#ffffff",corner_radius=5,height=36,width=130,hover_color= "#0E3C10",fg_color="#375638").pack(pady=5)

    ctk.CTkButton(todo_window,text="Clear All",command=clear_tasks,text_color="#ffffff",corner_radius=5,height=36,width=130,hover_color= "#0E3C10",fg_color="#375638").pack(pady=5)

    load_tasks()
