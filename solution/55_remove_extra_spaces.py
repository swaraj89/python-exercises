"""
Exercise 55: Remove Extra Spaces
"""


import re


def main():
    """Main function for exercise 55."""
    input_string = input("Enter a string : ")
    # Remove extra spaces
    clean_text = re.sub(r'\s+', ' ', input_string).strip()
    
    if not clean_text:
        print("Error: Input contains only spaces!")
    else:
        print(f"Cleaned string: {clean_text}")


if __name__ == "__main__":
    main()
