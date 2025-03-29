# 30 Days Of Python Coding Challenge
###################################
# Day 11 - Functions in Python
###################################
# Defining a function
def greet(name):
    print('Hello,', name)
# Calling a function
greet('Trieu Nguyen')

# Function without Parameters
def generate_full_name():
    first_name = 'Trieu'
    last_name = 'Nguyen'
    full_name = first_name + ' ' + last_name
    print('Full Name:', full_name)
generate_full_name()

def add_two_number():
    num1 = 5
    num2 = 7
    result = num1 + num2
    print('Result:', result)
add_two_number()

# Function returning a value - part1
def generate_full_name():
    first_name = 'Trieu'
    last_name = 'Nguyen'
    full_name = first_name + ' ' + last_name
    return full_name
print('Full name: ', generate_full_name())

def add_two_number():
    num1 = 2
    num2 = 3
    result = num1 + num2
    return result
print('Result: ', add_two_number())

# Function with parameters
def greeting(name):
    message = 'Hello ' + name + ', Welcome to Python for Everyone!'
    return message
print(greeting('Trieu Nguyen'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(5))

def square_number(x):
    return x * x
print(square_number(5))

def area_of_circle(r):
    PI = 3.14
    aea = PI * r ** 2
    return aea
print(area_of_circle(5))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name('Trieu', 'Nguyen'))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2025, 1990))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity)+ ' N'
    return weight
print('Weight of object: ', weight_of_object(75, 9.81))

# Function returning a value - part2
def print_name(name):
    return name
print('Name: ', print_name('Trieu Nguyen'))

def print_fullname(first, last):
    space = ' '
    full_name = first + space + last
    return full_name
print('Full name: ', print_fullname('Trieu', 'Nguyen'))

# Function with default parameters
def greet(name='World'):
    print('Hello,', name)
greet()
greet('Python for Everyone!')

def calculate_sum(num1=0, num2=0):
    return num1 + num2
print('Sum: ', calculate_sum(5, 7))

# Arbitrary number of arguments
def sum_all_num(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print('Sum: ', sum_all_num(5, 7, 2, 8, 1))

# Default and Arbitrary number of parameters in functions
def generate_grups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_grups('Team-1', 'ABC', 'Brook', 'David', 'Elon'))

# Function as a parameters of another function
def square_number(n):
    return n * n
def calculate_sum(func, x):
    return func(x)

print(calculate_sum(square_number, 3))



