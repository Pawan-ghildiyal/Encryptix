import tkinter as tk
from tkinter import messagebox
import random
import string
import re

def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Weak Password", "Length should be at least 4.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)

def check_strength(pwd):
    strength = "Weak"
    color = "red"

    length = len(pwd)
    has_upper = re.search(r'[A-Z]', pwd)
    has_lower = re.search(r'[a-z]', pwd)
    has_digit = re.search(r'\d', pwd)
    has_symbol = re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd)

    score = sum([bool(has_upper), bool(has_lower), bool(has_digit), bool(has_symbol)])

    if length >= 12 and score >= 3:
        strength = "Strong"
        color = "green"
    elif length >= 8 and score >= 2:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    strength_label.config(text=f"Strength: {strength}", fg=color)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x350")
root.config(bg="#f0f4f7")

heading = tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#333")
heading.pack(pady=20)

length_frame = tk.Frame(root, bg="#f0f4f7")
length_frame.pack(pady=10)

tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#f0f4f7").grid(row=0, column=0, padx=5)
length_var = tk.IntVar(value=12)
length_entry = tk.Entry(length_frame, textvariable=length_var, font=("Arial", 12), width=5)
length_entry.grid(row=0, column=1)

gen_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4caf50", fg="white", font=("Arial", 12), width=20)
gen_btn.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 14), justify="center", bd=2, relief=tk.SUNKEN, width=30)
password_entry.pack(pady=10)

strength_label = tk.Label(root, text="Strength: N/A", font=("Arial", 12, "bold"), bg="#f0f4f7", fg="gray")
strength_label.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#2196f3", fg="white", font=("Arial", 12), width=20)
copy_btn.pack(pady=10)

root.mainloop()
