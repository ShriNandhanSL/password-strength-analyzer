import re

# List of common weak passwords (can be expanded)
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123", "password123"
]

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digits(password):
    return any(char.isdigit() for char in password)

def check_special_chars(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def check_common(password):
    return password.lower() in COMMON_PASSWORDS

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

def get_strength(score):
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 5:
        return "Medium"
    else:
        return "Strong"

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

    print("\nScore:", score)
    print("Strength:", strength)


# Main Program
if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    
    if not password:
        print("Password cannot be empty!")
    else:
        analyze_password(password)