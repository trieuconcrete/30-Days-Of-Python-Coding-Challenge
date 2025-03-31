# 30 Days Of Python Coding Challenge
###################################
# Day 11 - List Comprehension in Python
###################################
# One way
language = 'python'
lst = list(language)
print(type(lst))
print(lst)

# Second way: List Comprehension in Python
lst = [i for i in lst]
print(type(lst))
print(lst)

# Generating numbers
numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

# Lambda Function
def add_two_nums(a, b):
    return a + b
print('Without Lambda', add_two_nums(2, 3))

add_two_nums_lambda = lambda a, b: a + b
print('With Lambda', add_two_nums_lambda(2, 3))

# Lambda Function Inside Another Function
def power(x):
    return lambda n: x ** n
cube = power(2)(3)
print('Cube of 2: ', cube)
two_power_of_five = power(2)(5)
print('2 to the power of 5: ', two_power_of_five)