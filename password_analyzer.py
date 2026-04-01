import re
import math

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password123"
}

SPECIAL_CHAR_PATTERN = r'[!@#$%^&*(),.?":{}|<>]'


def has_upper(password):
    return any(c.isupper() for c in password)


def has_lower(password):
    return any(c.islower() for c in password)


def has_digit(password):
    return any(c.isdigit() for c in password)


def has_special(password):
    return bool(re.search(SPECIAL_CHAR_PATTERN, password))


def is_common(password):
    return password.lower() in COMMON_PASSWORDS


def calculate_entropy(password):
    charset = 0

    if has_lower(password):
        charset += 26
    if has_upper(password):
        charset += 26
    if has_digit(password):
        charset += 10
    if has_special(password):
        charset += 32

    if charset == 0:
        return 0.0

    return round(len(password) * math.log2(charset), 2)


def calculate_score(password):
    score = 0

    if len(password) >= 8:
        score += 2
    if has_upper(password):
        score += 1
    if has_lower(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special(password):
        score += 2

    if is_common(password):
        score -= 2
    else:
        score += 2

    return score


def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 5:
        return "Medium"
    return "Strong"


def generate_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase length to at least 8 characters")
    if not has_upper(password):
        suggestions.append("Add uppercase letters")
    if not has_lower(password):
        suggestions.append("Add lowercase letters")
    if not has_digit(password):
        suggestions.append("Include numbers")
    if not has_special(password):
        suggestions.append("Include special characters")
    if is_common(password):
        suggestions.append("Avoid common passwords")

    return suggestions


def analyze_password(password):
    if not password:
        return {"error": "Password cannot be empty"}

    score = calculate_score(password)
    entropy = calculate_entropy(password)
    strength = get_strength(score)
    suggestions = generate_suggestions(password)

    return {
        "length_valid": len(password) >= 8,
        "has_upper": has_upper(password),
        "has_lower": has_lower(password),
        "has_digit": has_digit(password),
        "has_special": has_special(password),
        "is_common": is_common(password),
        "score": score,
        "strength": strength,
        "entropy": entropy,
        "suggestions": suggestions
    }


def display_result(result):
    if "error" in result:
        print(result["error"])
        return

    print("\nPassword Analysis")
    print("----------------------")

    print("Length OK:", result["length_valid"])
    print("Has Uppercase:", result["has_upper"])
    print("Has Lowercase:", result["has_lower"])
    print("Has Digits:", result["has_digit"])
    print("Has Special Characters:", result["has_special"])
    print("Is Common Password:", result["is_common"])

    print("\nScore:", result["score"])
    print("Strength:", result["strength"])
    print("Entropy:", result["entropy"])

    if result["suggestions"]:
        print("\nSuggestions:")
        for s in result["suggestions"]:
            print("-", s)


if __name__ == "__main__":
    password = input("Enter a password to analyze: ").strip()
    result = analyze_password(password)
    display_result(result)