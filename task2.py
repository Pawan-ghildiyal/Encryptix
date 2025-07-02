import tkinter as tk

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.configure(bg="#f0f4f7")

entry = tk.Entry(root, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout with '.' added
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), relief=tk.RAISED, bd=2)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        if btn_text == "C":
            btn.config(bg="#f44336", fg="white", command=clear)
        elif btn_text == "=":
            btn.config(bg="#4caf50", fg="white", command=evaluate)
        else:
            btn.bind("<Button-1>", click)

root.mainloop()
