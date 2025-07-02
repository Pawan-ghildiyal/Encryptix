import tkinter as tk
import random

# Choices with emojis
choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Scores and history
user_score = 0
computer_score = 0
rounds_history = []

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(list(choices.keys()))

    result = ""
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Scissors" and comp_choice == "Paper") or
        (user_choice == "Paper" and comp_choice == "Rock")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update result display
    result_label.config(text=f"Your Choice: {user_choice} {choices[user_choice]}\n"
                             f"Computer's Choice: {comp_choice} {choices[comp_choice]}\n\n{result}")
    
    # Update score
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

    # Update history
    rounds_history.append(f"You: {choices[user_choice]} | Comp: {choices[comp_choice]} → {result}")
    history_listbox.delete(0, tk.END)
    for item in rounds_history[-10:]:  # Show last 10 rounds
        history_listbox.insert(tk.END, item)

def reset_game():
    global user_score, computer_score, rounds_history
    user_score = 0
    computer_score = 0
    rounds_history = []
    score_label.config(text="Score → You: 0 | Computer: 0")
    result_label.config(text="Make your move!")
    history_listbox.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x600")
root.config(bg="#f0f4f7")

# Heading
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333").pack(pady=20)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

for item in choices:
    btn = tk.Button(btn_frame, text=f"{item} {choices[item]}", font=("Arial", 14), width=12, command=lambda c=item: play(c))
    btn.pack(side="left", padx=10)

# Result display
result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), bg="#f0f4f7", fg="#555", justify="center")
result_label.pack(pady=30)

# Score display
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#f0f4f7", fg="#222")
score_label.pack(pady=10)

# Rounds History Label
tk.Label(root, text="Rounds History (Last 10):", font=("Arial", 12, "bold"), bg="#f0f4f7", fg="#555").pack(pady=5)

# History Listbox
history_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 11))
history_listbox.pack(pady=10)

# Control buttons
control_frame = tk.Frame(root, bg="#f0f4f7")
control_frame.pack(pady=15)

reset_btn = tk.Button(control_frame, text="Reset Game", font=("Arial", 12), bg="#ffa726", fg="white", command=reset_game)
reset_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(control_frame, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", command=root.quit)
exit_btn.grid(row=0, column=1, padx=10)

# Run the GUI
root.mainloop()
