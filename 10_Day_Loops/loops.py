# 30 Days Of Python Coding Challenge
###################################
# Day 10 - Loops in Python
###################################
# While Loop
count = 0
while count < 5:
    print('Count: ', count)
    count += 1

count = 0
while count < 5:
    print('Count: ', count)
    count += 1
else:
    print('Loop completed')

# Break and Continue - part1
count = 0
while count < 5:
    print('Count: ', count)
    count += 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print('Count: ', count)
    count += 1

# For loop
list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for item in list:
    print('Item: ', item)

language = 'Python'
for letter in language:
    print('Letter: ', letter)

for i in range(len(language)):
    print('Index: ', i, 'Character: ', language[i])

# Dictionary
person = {
    'name':'John Doe',
    'age':35,
    'country':'USA'
}
for key in person:
    print('Key: ', key, 'Value: ', person[key])

for key, value in person.items():
    print('Key: ', key, 'Value: ', value)

# Set
st = {'Facebook', 'Twitter', 'Microsoft', 'Apple', 'IBM', 'Google', 'Amazon'}
for company in st:
    print('Company: ', company)

# Break and Continue - Part2
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
for num in numbers:
    print('Number: ', num)
    if num == 3:
        break

for num in numbers:
    print('Number: ', num)
    if num == 3:
        continue
    print('Next number should be ', num + 1) if num != 5 else print("Loop's end")

# The range function
for number in range(10):
    print('Number: ', number)

# Nested for loop
person = {
    'first_name': 'Trieu',
    'last_name': 'Nguyen',
    'age': 35,
    'country': 'VietNam',
    'city': 'Da Nang',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'PHP'],
    'address': {
       'street': 'Space street',
        'zipcode': '550000'
    }
}
for key, value in person.items():
    if key == 'skills':
        for skill in value:
            print('Skill: ', skill)

# For else
for number in range(10):
    print('Number: ', number)
else:
    print('Loop completed')

# Pass
for number in range(10):
    pass

# Exception Handlingr

