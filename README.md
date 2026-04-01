Password Strength Analyzer

Overview

This project is a Python-based password strength analyzer that evaluates the security of a password using rule-based checks and entropy calculation.

Features

- Validates password length
- Detects uppercase and lowercase characters
- Identifies digits and special characters
- Checks against common weak passwords
- Calculates password strength (Weak, Medium, Strong)
- Computes entropy for security estimation
- Provides suggestions to improve weak passwords

How It Works

The program analyzes a password based on multiple criteria such as length, character diversity, and common patterns. It assigns a score, calculates entropy, and determines the overall strength.

Usage

Run the program using:

python password_checker.py

Enter a password when prompted to see the analysis.

Example

Input:
Hello123

Output:
Strength: Medium
Entropy: (value shown)
Suggestions:

- Add special characters

Technologies Used

- Python

Project Structure

password-strength-analyzer/
│
├── password_checker.py
└── README.md

Future Improvements

- Add graphical user interface (GUI)
- Integrate password breach detection
- Improve scoring algorithm using advanced techniques

Author

ShriNandhan