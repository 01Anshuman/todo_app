import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(False, False)

# List to store tasks
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to delete")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def clear_tasks():
    global tasks
    tasks = []
    update_listbox()

# Widgets
entry = tk.Entry(root, font=('Arial', 16), width=24)
entry.pack(pady=20)

add_btn = tk.Button(root, text="Add Task", font=('Arial', 14), command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", font=('Arial', 14), command=delete_task)
delete_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All Tasks", font=('Arial', 14), command=clear_tasks)
clear_btn.pack(pady=5)

listbox = tk.Listbox(root, font=('Arial', 14), width=30, height=10)
listbox.pack(pady=20)

# Run the GUI loop
root.mainloop()
