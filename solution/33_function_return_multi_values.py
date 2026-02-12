def calculate(num: int, num_one: int):
    return num + num_one, num * num_one

sum, product = calculate(5, 10)

print(f"Sum: {sum}, Product : {product}")