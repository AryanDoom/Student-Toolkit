#add tasks
def save_task(task):
    with open("Todolist.txt", "a") as file:
        file.write(task + "\n")

#delete all tasks
def clear_all_tasks():
    open("Todolist.txt", "w").close()

#check file if tasks exisst , if yes load said tasks
def load_tasks_from_file():
    tasks = []
    try:
        with open("Todolist.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass    # will just create a file when writing or adding a task so just pass the error raised
    return tasks

# deleting tasks if selected (1 at a time)
def save_tasks_after_delete(task_listbox):
    with open("Todolist.txt", "w") as file:
        for i in range(task_listbox.size()):
            file.write(task_listbox.get(i) + "\n")
