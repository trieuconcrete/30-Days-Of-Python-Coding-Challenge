# 30 Days Of Python Coding Challenge
###################################
# Day 8 - Dictionaries
###################################
empty_dict = {}
person = {
    'first_name':'Trieu',
    'last_name':'Nguyen',
    'age':35,
    'country':'VietNam',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'PHP'],
    'address':{
        'street':'Space street',
        'zipcode':'550000'
    }
}
print('Person: ', person)

# Accessing dictionary items
first_name = person['first_name']
print('First name: ', first_name)
last_name = person['last_name']
print('Last name: ', last_name)
age = person['age']
print('Age: ', age)

print('first name: ', person.get('first_name'))
print('Last name: ', person.get('last_name', 'Unknown'))
print('Age: ', person.get('abc'))

# Adding items to a dictionary
person['job_title'] = 'Software Engineer'
print('Person after adding job_title: ', person)
person['skills'].append('HTML')
print('Person after adding skill: ', person)

# Modifying items to a dictionary
person['age'] = 30
print('Person after modifying age: ', person)

# Checking keys in a dictionary
print('Is first_name in person: ', 'first_name' in person)
print('Is job_title in person: ', 'job' in person)

# Removing items from a dictionary
person.pop('job_title')
person.popitem()
del person['is_marred']
print('Person after removing items: ', person)

# Changing dictionary to list of items
print(person.items())

# Clearing the dictionary
print(person.clear())

# Deleting a dictionary
dct = {'key1': 'value1', 'key2': 'value2'}
del dct

# Copy the dictionary
dct = {'key1': 'value1', 'key2': 'value2'}
dct_copy = dct.copy()
print('dct copy: ', dct_copy)

# Getting dictionary keys as a list
dct = {'key1': 'value1', 'key2': 'value2'}
keys = dct.keys()
print('keys: ', keys)

# Getting dictionary values as a list
values = dct.values()
print('values: ', values)