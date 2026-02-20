"""
Exercise 54: Validate a Password Strength
"""
import re

def main():
    """Main function for exercise 54."""
    password = input("Enter a password to validate: ")
    
    if validate_password(password):
        print("Password is strong.")
    else:
        print("Password is weak.")

def validate_password(password):
    """Validate the strength of a password."""
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))


if __name__ == "__main__":
    main()
