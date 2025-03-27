# 30 Days Of Python Coding Challenge
###################################
# Day 9 - Conditional in Python
###################################
# If conditional
a = 3
if a > 0:
    print('a is positive')

# If Else
a = -3
if a < 0:
    print('a is negative')
else:
    print('a is positive')

# If elif Else
a = 0
if a > 0:
    print('a is positive')
elif a < 0:
    print('a is negative')
else:
    print('a is zero')

# Short hand
a = 3
print('a is positive') if a > 0 else print('a is negative')

# Nested conditional
a = 0
if a > 0:
    if a % 2 == 0:
        print('a is positive and even')
    else:
        print('a is positive and odd')
elif a == 0:
    print('a is zero')
else:
    print('a is negative')

# If condition and logical operators
a = 3
if a > 0 and a % 2 == 0:
    print('a is positive and even')
elif a == 0:
    print('a is zero')
else:
    print('a is negative or odd')

# If and or logical operators
user = 'Trieu'
access_level = 3
if user == 'Admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')