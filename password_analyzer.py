import re
import math

# Common weak passwords list for basic validation
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "password123"
]

# Check if password length is at least 8 characters
def check_length(password):
    return len(password) >= 8

# Check for uppercase letters
def check_uppercase(password):
    return any(char.isupper() for char in password)

# Check for lowercase letters
def check_lowercase(password):
    return any(char.islower() for char in password)

# Check for numeric digits
def check_digits(password):
    return any(char.isdigit() for char in password)

# Check for special characters using regex
def check_special_chars(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

# Check if password is commonly used
def check_common(password):
    return password.lower() in COMMON_PASSWORDS

# Calculate entropy based on character set size and length
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

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

# Generate suggestions to improve weak passwords
def give_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters")
    if not any(char.isupper() for char in password):
        suggestions.append("Add uppercase letters")
    if not any(char.islower() for char in password):
        suggestions.append("Add lowercase letters")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include numbers")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include special characters")

    return suggestions

# Assign score based on password properties
def calculate_score(password):
    score = 0

    if check_length(password):
        score += 2
    if check_uppercase(password):
        score += 1
    if check_lowercase(password):
        score += 1
    if check_digits(password):
        score += 1
    if check_special_chars(password):
        score += 2
    if not check_common(password):
        score += 2
    else:
        score -= 2

    return score

# Convert score into strength category
def get_strength(score):
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 5:
        return "Medium"
    else:
        return "Strong"

# Main analysis function
def analyze_password(password):
    print("\nPassword Analysis:")
    print("----------------------")

    print("Length OK:", check_length(password))
    print("Has Uppercase:", check_uppercase(password))
    print("Has Lowercase:", check_lowercase(password))
    print("Has Digits:", check_digits(password))
    print("Has Special Characters:", check_special_chars(password))
    print("Is Common Password:", check_common(password))

    score = calculate_score(password)
    strength = get_strength(score)
    entropy = calculate_entropy(password)
    suggestions = give_suggestions(password)

    print("\nScore:", score)
    print("Strength:", strength)
    print("Entropy:", entropy)

    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print("-", s)

# Entry point of the program
if __name__ == "__main__":
    password = input("Enter a password to analyze: ")

    if not password:
        print("Password cannot be empty!")
    else:
        analyze_password(password)