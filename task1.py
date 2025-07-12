import tkinter as tk
from tkinter import messagebox, font

tasks = []
completed_tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        # Remove from correct list
        if selected < len(tasks):
            tasks.pop(selected)
        else:
            completed_tasks.pop(selected - len(tasks))
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        if selected < len(tasks):
            completed_task = tasks.pop(selected)
            completed_tasks.append(completed_task)
            update_listbox()
        else:
            messagebox.showinfo("Info", "Task is already marked as completed.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark completed.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
    for task in completed_tasks:
        listbox.insert(tk.END, f"✅ {task}")

root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x550")
root.config(bg="#f0f4f7")

heading_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(size=10)

heading = tk.Label(root, text="My To-Do List", font=heading_font, bg="#f0f4f7", fg="#333")
heading.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(input_frame, text="Add Task", command=add_task, bg="#4caf50", fg="white", font=button_font)
add_btn.grid(row=0, column=1)

list_frame = tk.Frame(root, bg="#f0f4f7")
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=45, height=15, font=("Arial", 11), yscrollcommand=scrollbar.set, selectbackground="#d3d3d3")
listbox.pack()

scrollbar.config(command=listbox.yview)

btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

mark_btn = tk.Button(btn_frame, text="Mark as Completed", command=mark_completed, bg="#2196f3", fg="white", font=button_font, width=17)
mark_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=button_font, width=15)
del_btn.grid(row=0, column=1, padx=5)

root.mainloop()
