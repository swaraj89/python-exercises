# using maths
def reverse(num: int):
    rev = 0
    while num != 0:
        digit = num % 10
        rev = rev*10 + digit
        num //= 10
    
    return rev

# Run the app

N = int(input("Enter a number: "))
print(f"reverse of {N} is {reverse(N)}")
