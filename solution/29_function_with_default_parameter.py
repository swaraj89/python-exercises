def greet(name="student"):
    print(f"Hello, {name.capitalize()}")

greet()

user_name = input("Enter your name : ")
greet(user_name)