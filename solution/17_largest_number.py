user_input = input("Enter three numbers seprated by space : ")
user_input_list = user_input.split(" ")

numbers = list(map(int, user_input_list))

# greatest = 0

# for number in numbers:
#     if number > greatest:
#         greatest = number
    

# print(f"among {numbers}, {greatest} is greatest")
print(f"among {numbers}, {sorted(numbers, reverse=True)[0]} is greatest")