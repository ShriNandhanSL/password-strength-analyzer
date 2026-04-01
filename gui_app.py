import tkinter as tk
from tkinter import messagebox
import re
import math

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "password123"
]

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
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
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    if password.lower() not in COMMON_PASSWORDS:
        score += 2
    else:
        score -= 2

    if score <= 2:
        return "Weak"
    elif score <= 5:
        return "Medium"
    else:
        return "Strong"

def analyze():
    password = entry.get()

    if not password:
        messagebox.showwarning("Error", "Password cannot be empty")
        return

    strength = get_strength(password)
    entropy = calculate_entropy(password)

    result.set(f"Strength: {strength}\nEntropy: {entropy}")

# GUI window
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("350x200")

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Analyze", command=analyze).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12)).pack(pady=10)

root.mainloop()