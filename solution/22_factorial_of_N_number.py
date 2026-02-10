# Factorial of a number
def factorial(N: int):
    fact = 1
    while N != 0:
        fact = fact * N
        N = N-1
    
    return fact


N = int(input("Enter a number: "))

print(f"Factorial of {N} is {factorial(N)}")