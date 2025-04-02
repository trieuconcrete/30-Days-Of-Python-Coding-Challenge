# 30 Days Of Python Coding Challenge
###################################
# Day 15 - Python Type Errors
###################################
# SyntaxError
# print "Error" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("hello world")

# NameError
# print(age) # NameError: name 'age' is not defined
age = 35
print(age)

# IndexError
numbers = [1, 2, 3, 4, 5]
# numbers[6] # IndexError: list index out of range
numbers[3]

# ModuleNotFoundError
# import maths # ModuleNotFoundError: No module named 'maths'

# AttributeError
import math
# math.PI # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# KeyError
users = {'name': 'John', 'age': 35}
# users['skills'] # KeyError: 'skills'

# TypeError
# 4 + '3' #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ImportError
# from math import power # ImportError: cannot import name 'power' from 'math' (/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload/math.cpython-312-darwin.so)

# ValueError
# int('12a') # ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError
# 1/0 # ZeroDivisionError: division by zero






