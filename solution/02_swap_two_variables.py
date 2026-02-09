# XOR 
def swap_two_variables(number_one, number_two):
    number_one = number_one + number_two
    number_two = number_one - number_two
    number_one = number_one - number_two
    return (number_one, number_two)

def swap_two_variables_one_line(number_one, number_two):
    number_one, number_two = number_two, number_one
    return number_one, number_two 


test1 = swap_two_variables(10, 20)
test2 = swap_two_variables(-10, -20)
test3 = swap_two_variables(0, 0)
test4 = swap_two_variables(20, 10)

# test1 = swap_two_variables_one_line(10, 20)
# test2 = swap_two_variables_one_line(-10, -20)
# test3 = swap_two_variables_one_line(0, 0)
# test4 = swap_two_variables_one_line(20, 10)

print(f"{test1}")
print(test2)
print(test3)
print(test4)