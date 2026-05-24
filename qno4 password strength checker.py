# Password Strength Checker
passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_chars = "!@#$%^&*"

for password in passwords:

    print("\nChecking password:", password)

    missing = []
 # Check length
    if len(password) < 8:
        missing.append("At least 8 characters")

    # Check uppercase
    if not any(char.isupper() for char in password):
        missing.append("One uppercase letter")
