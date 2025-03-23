# 30 Days Of Python Coding Challenge
###################################
# Day 4 - Strings in Python
###################################
# Single line comment
letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello World'
print(greeting)
print(len(greeting))
sentence = 'I hope you are enjoying 30 days of python coding challenge'
print(sentence, ', len: ', len(sentence))

# Multiline string
multiline_string = '''I am a teacher and enjoy teaching
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of Python.
'''
print(multiline_string)
# Another way of doing the sam thing
another_multiline_string = """I am a teacher and enjoy teaching
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of Python.
"""
print(another_multiline_string)

# String concatenation
first_name = 'Trieu'
last_name = 'Nguyen'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Unpacking characters
language = 'Python'
a,b,c,d,e,f = language
print(a, b, c, d, e, f)

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end we can use negative indexing. -1 is the laster index
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

# Slicing
language = 'Python'
first_three = language[0:3]
last_three = language[3:6]
print(last_three)
last_three = language[3:]
print(last_three)

# Skipping character while splitting Python strings
language = 'Python'
split_string = language[0:6:2]
print(split_string)

# Escape sequences
print('I hope every one enjoying the python challenge.\nDo you?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash symbol(\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String methods
# capitalize(): Converts the first character the string to Capital Letter
challenge = 'thirty days of python'
print(challenge.capitalize())

# count(): Return occurrences of substring in string, count(substring, start=.., end=..)
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

#find(): Returns the index of first occurrence of substring in string
print(challenge.find('th'))
print(challenge.find('th', 7, 14))
print(challenge.find('o'))

# expandtabs(): Replaces tab characters with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tday\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# format(): formats string into nicer output
first_name = 'Trieu'
last_name = 'Nguyen'
job = 'Software Engineer'
country = 'VietNam'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name,job,country)
print(sentence)

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}.'.format(str(radius), str(area))
print(result)

# index(): Returns the index of substring
challenge = 'thirty days of python challenge'
print(challenge.index('th'))
print(challenge.index('o'))

# isalnum(): Check alphanumeric characters
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'thirty days of python challenge'
print(challenge.isalnum())

# isalpha(): Check if all characters are alphabets
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
challenge = '30DaysPython3'
print(challenge.isalpha())
challenge = '30'
print(challenge.isalpha())

# isdigit(): Check digit characters
challenge = '30DaysPython'
print(challenge.isdigit())
challenge = 'ThirtyDaysPython'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())

# isdecimal(): check decimal characters
challenge = '10'
print(challenge.isdecimal())
challenge = '30.5'
print(challenge.isdecimal())

# isidentifier(): Check if string is valid identifier
challenge = '30thirtyDaysPython'
print(challenge.isidentifier())
challenge = 'Days_Python'
print(challenge.isidentifier())

# islower(): Check if all alphabets in a string are lowercase
challenge = 'thirty days python'
print(challenge.islower())
challenge = 'ThirtyDaysPython'
print(challenge.islower())

# isupper(): check if all alphabets in a string are upper
challenge = 'THIRTY DAYS PYTHON'
print(challenge.isupper())
challenge = 'ThirtyDaysPython'
print(challenge.isupper())

# isnumeric(): Check if string is valid numeric
challenge = '30'
print(challenge.isnumeric())
challenge = '30.5'
print(challenge.isnumeric())
challenge = 'ThirtyDaysPython'
print(challenge.isnumeric())

# isspace(): Check if string is a space
challenge = 'Thirty Days Python'
print(challenge.isspace())
challenge =' '
print(challenge.isspace())

# join(): Joins all items in an iterable into a string, separated by specified separator
challenge = ['thirty', 'days', 'of', 'python']
separator ='#'
result = separator.join(challenge)
print(result)

# ljust(): Returns a string left-justified in a field of specified width
challenge = 'Thirty Days Python'
width = 20
result = challenge.ljust(width)
print(result)

# strip(): Returns a string left-justified in a field of specified width
challenge = ' thirty Days Python'
presult = challenge.strip('y')
print(presult)

# replace(): Returns a string left-justified in a field of specified width
challenge = 'Thirty Days Python'
replace_with = 'Three'
result = challenge.replace('Thirty', replace_with)
print(result)

# title(): Returns a string left-justified in a field of specified width
challenge = 'thirty days python'
result = challenge.title()
print(result)

# swapcase(): Returns a string left-justified in a field of specified width
challenge = 'Thirty Days Python'
result = challenge.swapcase()
print(result)

# startswith(): Checks if string starts with the specified string
challenge = 'Thirty Days Python'
print(challenge.startswith('Thirty'))
print(challenge.startswith('three'))