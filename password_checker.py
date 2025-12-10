import re

def check_password_strength(password):
    score = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add at least one number.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character.")

    # Strength result
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return strength[score], remarks


def main():
    print("Password Strength Checker ")
    password = input("Enter your password: ")

    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print(f" - {s}")
    else:
        print("Your password is perfect!")


if __name__ == "__main__":
    main()

