# 30 Days Of Python Coding Challenge
###################################
# Day 14 - Higher order functions in Python
###################################
# Higher Order Functions
## Function as a Parameter
def sum_number(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

result = higher_order_function(sum_number, [1, 2, 3])
print(result)

## Function as a Return Value
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    else:
        return None

result = higher_order_function('square')
print(result(5))

result = higher_order_function('cube')
print(result(3))

result = higher_order_function('absolute')
print(result(-5))

# Python Closures
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

# Python Decorators
## Creating Decorators
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())

## Let us implement the example above with a decorator
'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())

# Applying Multiple Decorators to a Single Function
'''These decorator functions are higher order functions
that take functions as parameters'''
## First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
## Second Decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())

# Accepting Parameters in Decorator Functions
def decorator_with_parameter(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameter
def greeting(name, age, country):
    print("Hello, {}! You are {} years old.".format(name, age))

greeting('Trieu', 35, 'VietName')

# Built-in Higher Order Functions
## Python - Map Function
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
### Lets apply it with a lambda function
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

skills = ['PHP', 'JavaScript', 'Java', 'Jquery', 'Python']
def change_to_upper(name):
    return name.upper()
name_upper = map(change_to_upper, skills)
print(list(name_upper))

names_upper_cased = map(lambda name: name.upper(), skills)
print(list(names_upper_cased))

# Python - Filter Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

skills = ['PHP', 'JavaScript', 'Java', 'Jquery', 'Python']
def is_name_long(skill):
    return len(skill) > 5
python_skills = filter(is_name_long, skills)
print(list(python_skills))

# Python - Reduce Function
from functools import reduce  # Import hàm reduce từ module functools
numbers_str = ['1', '2', '3', '4', '5', '6']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)