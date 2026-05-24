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
 # Check lowercase
    if not any(char.islower() for char in password):
        missing.append("One lowercase letter")

    # Check digit
    if not any(char.isdigit() for char in password):
        missing.append("One digit")
 # Check special character
    if not any(char in special_chars for char in password):
        missing.append("One special character")

    if len(missing) == 0:
        print("Strong password")
