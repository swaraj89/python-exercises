N = int(input("Enter a number: "))

def multiplication_table(num):
    for i in range(1, 11, 1):
        print(f"{num} * {i} = {num*i}")


multiplication_table(N)