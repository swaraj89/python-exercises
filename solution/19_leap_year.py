user_input = int(input("Enter year to check if it's leap year : "))

if user_input % 4 == 0:
    if user_input % 100 == 0:
        if user_input % 400 == 0:
            print(f"{user_input} is a leap year")
    else:
        print(f"{user_input} is a leap year")
else:
    print(f"{user_input} is not a leap year")

        