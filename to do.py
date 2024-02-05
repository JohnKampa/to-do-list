import tkinter as tk
from tkinter import ttk

def add_task():
    task = entry_task.get()
    if task and task.lower() not in task_list:
        task_list.append(task.lower())
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)  # Clear the entry after adding a task
    elif task.lower() in task_list:
        label_status.config(text="Task already in the list.")

def show_tasks():
    label_status.config(text="List of tasks: " + ', '.join(task_list))

# Create the main window
window = tk.Tk()
window.title("TO DO List")

# Configure style for a more modern look
style = ttk.Style()
style.theme_use("clam")  # Choose the theme (aqua, clam, alt, default, etc.)

# Task input entry
label_task = ttk.Label(window, text="Was musst du noch alles machen?")
label_task.pack(pady=10)

entry_task = ttk.Entry(window, font=("Arial", 12))
entry_task.pack(pady=10)

# Yes/No input entry
label_yes_no = ttk.Label(window, text="TO DO:", font=("Arial", 12, "bold"))
label_yes_no.pack(pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(window, font=("Arial", 12), selectbackground="#a6a6a6", selectforeground="white")
listbox_tasks.pack(pady=10)

# Add and Show buttons
button_add = ttk.Button(window, text="Hinzufügen", command=add_task)
button_add.pack(pady=5)

button_show = ttk.Button(window, text="Anzeigen", command=show_tasks)
button_show.pack(pady=5)

# Status label
label_status = ttk.Label(window, text="", font=("Arial", 12))
label_status.pack(pady=10)

# Task list
task_list = []

# Start the main loop
window.mainloop()
