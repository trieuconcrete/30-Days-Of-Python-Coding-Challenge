# 30 Days Of Python Coding Challenge
###################################
# Day 5 - Lists in Python
###################################
empty_list = list()
print(empty_list)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Vue', 'NodeJS', 'MongoDB', 'PHP', 'Python']
countries = ['VietNam', 'Japan', 'English', 'Sweden', 'United States']

print('fruits: ', fruits)
print('number of fruits: ', len(fruits))
print('vegetables: ', vegetables)
print('number of vegetables: ', len(vegetables))
print('animal products: ', animal_products)
print('number of animal products: ', len(animal_products))
print('web techs: ', web_techs)
print('number of web techs: ', len(web_techs))
print('countries: ', countries)
print('number of countries: ', len(countries))

# Modifying list
first_fruits = fruits[0]
print(first_fruits)
second_fruits = fruits[1]
print(second_fruits)
last_fruits = fruits[len(fruits) - 1]
print(last_fruits)

# Slicing items
all_fruits = fruits[0:4]
print('All fruits: ', all_fruits)
print('All fruit: ', fruits[0:])
print('Orange and mango: ', fruits[1:3])
print('Orange mango lemon: ', fruits[1:])
print('All fruits: ', fruits[-4:])
print('Orange and mango: ', fruits[-3:-1])
print('Orange mango lemo: ', fruits[-3:])

fruits[0]  = 'avocado'
fruits[1] = 'apple'
fruits[len(fruits) - 1] = 'lime'
print('Modified fruits: ', fruits)

# Checking items
does_exist = 'apple' in fruits
print('Does apple exist in fruits: ', does_exist)
does_exist = 'lemon' in fruits
print('Does lemon exist in fruits: ', does_exist)

# Append
fruits.append('grape')
print('Fruits after append: ', fruits)
fruits.append('lemon')
print('Fruits after append: ', fruits)

# Insert
fruits.insert(2, 'banana')
print('Fruits after insert: ', fruits)
fruits.insert(3, 'orange')
print('Fruits after insert: ', fruits)

# Remove
fruits.remove('lemon')
print('Fruits after remove: ', fruits)
fruits.remove('banana')
print('Fruits after remove: ', fruits)

# Pop
fruits.pop()
print('Fruits after pop: ', fruits)
fruits.pop(0)
print('Fruits after pop: ', fruits)

# del
del fruits[1]
print('Fruits after del: ', fruits)

# clear
fruits.clear()
print('Fruits after clear: ', fruits)

# copying a lists
fruits = ['banana', 'orange', 'mango', 'lemon']
copied_fruits = fruits.copy()
print('Copied fruits: ', copied_fruits)

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-1, -2, -3, -4, -5]
integers = negative_numbers + zero + positive_numbers
print('Integers: ', integers)
fruits_and_vegetables = fruits + vegetables
print('Fruits and vegetables: ', fruits_and_vegetables)

# join with extend
num1 = [0, 1, 2, 3, 4]
num2 = [5, 6, 7, 8, 9]
num1.extend(num2)
print('Extended num1: ', num1)
fruits.extend(vegetables)
print('Extended fruits: ', fruits)

# count
print('Number of orange: ', fruits.count('orange'))
ages = [22, 29, 23, 24, 25, 24, 25, 26]
print('Number of 25s: ', ages.count(25))

# index
print('Index of orange: ', fruits.index('orange'))
print('Index of 25: ', ages.index(25))

# reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print('Reversed fruits: ', fruits)
ages.reverse()
print('Reversed ages: ', ages)

# sort
fruits.sort()
print('Sorted fruits: ', fruits)
fruits.sort(reverse=True)
print('Sorted fruits in descending order: ', fruits)
ages.sort()
print('Sorted ages: ', ages)
ages.sort(reverse=True)
print('Sorted ages in descending order: ', ages)
