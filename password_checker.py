import re
def check_password_strength(password):
    score = 0
    feedback = []
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12+ is better)")
    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$% etc.)")
    # Common pattern checks
    if re.search(r'(.)\1{2,}', password):  # 3+ repeated chars in a row
        score -= 1
        feedback.append("Avoid repeated characters (aaa, 111)")

    if password.lower() in ['password', '123456', 'qwerty', 'letmein', 'admin']:
        score = 0
        feedback.append("This is an extremely common password")
    # Rate the result
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, score, feedback
if __name__ == "__main__":
    pw = input("Enter a password to check: ")
    strength, score, feedback = check_password_strength(pw)
    print(f"\nStrength: {strength} (score: {score})")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")
