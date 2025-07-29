import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Main window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f7f7f7")

# Title
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"), bg="#f7f7f7", fg="#333")
title_label.pack(pady=10)

# Entry field
task_entry = tk.Entry(root, font=("Helvetica", 14), width=30, bd=2)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f7f7f7")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

# Listbox with scrollbar
frame = tk.Frame(root, bg="#f7f7f7")
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox = tk.Listbox(frame, width=40, height=10, font=("Helvetica", 12), yscrollcommand=scrollbar.set, selectbackground="#d3d3d3")
tasks_listbox.pack()

scrollbar.config(command=tasks_listbox.yview)

# Run the app
root.mainloop()
