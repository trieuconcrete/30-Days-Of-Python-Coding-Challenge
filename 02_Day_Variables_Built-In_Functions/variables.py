# 30 Days Of Python Coding Challenge
###################################
# Day 2 - Variables in Python
###################################
first_name = 'Trieu'
last_name = 'Nguyen'
age = 35
country = 'VietName'
city = 'Da Nang'
is_married = True
skills = ['HTML', 'CSS', 'JS', 'PHP', 'Laravel', 'Python', 'Django', 'MYSQL', 'PostgreSQL', 'VPS', 'AWS']
person_info = {
    'first_name': 'Trieu',
    'last_name': 'Nguyen',
    'age': 35,
    'country': 'VietName',
    'city': 'Da Nang',
    'is_married': True,
}

# Printing the values stored in the variables
print('First name:', first_name)
print('Last name:', last_name)
print('Age:', age)
print('Country:', country)
print('City:', city)
print('Married:', is_married)
print('Skills:', skills)
print('Person info:', person_info)

# Declaring multiple variables in one line
first_name, last_name, age, country, city, is_married = 'Trieu', 'Nguyen', 35, 'VietName', 'Da Nang', True
print(first_name, last_name, age, country, city, is_married)