import tkinter as tk
from tkinter import messagebox, ttk
import re
import math

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password123"
}

SPECIAL_PATTERN = r'[!@#$%^&*(),.?":{}|<>]'

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if re.search(SPECIAL_PATTERN, password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)

def get_strength(password):
    score = 0

    if len(password) >= 8:
        score += 2
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if re.search(SPECIAL_PATTERN, password):
        score += 2
    if password.lower() not in COMMON_PASSWORDS:
        score += 2
    else:
        score -= 2

    if score <= 2:
        return "Weak"
    elif score <= 5:
        return "Medium"
    return "Strong"

def get_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase length")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add numbers")
    if not re.search(SPECIAL_PATTERN, password):
        suggestions.append("Add special characters")
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid common passwords")

    return suggestions

def analyze():
    password = entry.get()

    if not password:
        messagebox.showwarning("Error", "Password cannot be empty")
        return

    strength = get_strength(password)
    entropy = calculate_entropy(password)
    suggestions = get_suggestions(password)

    result_label.config(text=f"Strength: {strength}\nEntropy: {entropy}")

    if strength == "Weak":
        result_label.config(fg="red")
        progress['value'] = 30
    elif strength == "Medium":
        result_label.config(fg="orange")
        progress['value'] = 60
    else:
        result_label.config(fg="green")
        progress['value'] = 100

    if suggestions:
        suggestion_text = "Suggestions:\n" + "\n".join("- " + s for s in suggestions)
    else:
        suggestion_text = "Good password!"

    suggestion_label.config(text=suggestion_text)

def toggle_password():
    if show_password.get():
        entry.config(show="")
    else:
        entry.config(show="*")

# Window setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("420x350")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True)

tk.Label(frame, text="Password Strength Analyzer",
         font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

show_password = tk.BooleanVar()
tk.Checkbutton(frame, text="Show Password", variable=show_password,
               command=toggle_password, bg="#f0f0f0").pack()

tk.Button(frame, text="Analyze", command=analyze,
          font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=5)

progress = ttk.Progressbar(frame, length=250, mode='determinate')
progress.pack(pady=10)

suggestion_label = tk.Label(frame, text="", font=("Arial", 10),
                            bg="#f0f0f0", justify="left")
suggestion_label.pack(pady=5)

root.mainloop()