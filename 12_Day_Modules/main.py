from module import generate_full_name, sum_two_numbs, calculate_age, person

print(generate_full_name('Trieu', 'Nguyen'))
print(sum_two_numbs(5, 7))
print(calculate_age(2025, 1990))
print('Person info:', person)

# OS Module
import os
print('OS:', os.name)
# Creating a directory
os.mkdir('dictionary_name')
# Changing the current directory
os.chdir('dictionary_name')
# Getting current working directory
print(os.getcwd())
# Removing a directory
os.rmdir(os.getcwd())

# Sys Module
import sys
print('Python version:', sys.version)
print('Python executable:', sys.executable)
print('Python path:', sys.path)
print('Maxsize: ', sys.maxsize)
# sys.exit()

# Statistics Module
from statistics import *
ages = [20, 30, 40, 50]
print('Mean:', mean(ages))
print('Median:', median(ages))
print('Mode:', mode(ages))
print('Standard Deviation:', stdev(ages))

# Math Module
import math
print('Square root of 25:', math.sqrt(25))
print('Exponential of 2:', math.exp(2))
print('Logarithm of 100:', math.log(100))
print('Factorial of 5:', math.factorial(5))
print('PI: ', math.pi)
print('Pow: ', math.pow(2, 3))
print('Floor: ', math.floor(9.81))
print('Ceil: ', math.ceil(9.81))
print('Log10: ', math.log10(100))

# String Module
import string
print('Uppercase alphabet:', string.ascii_uppercase)
print('Lowercase alphabet:', string.ascii_lowercase)
print('Digits:', string.digits)
print('Punctuation:', string.punctuation)
print('Whitespace:', string.whitespace)

# Random Module
import random
print('Random integer between 1 and 10:', random.randint(1, 10))
print('Random float between 0 and 1:', random.random())
print('Random choice from a list:', random.choice([1, 2, 3, 4, 5]))
print('Random sample from a list:', random.sample([1, 2, 3, 4, 5], 2))
print('Random choice from a list:', random.choice(['PHP', 'Python', 'Java', 'Jquery', 'HTML']))


