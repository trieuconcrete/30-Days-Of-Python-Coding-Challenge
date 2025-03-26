# 30 Days Of Python Coding Challenge
###################################
# Day 6 - Tuples in Python
###################################
empty_tuple = ()
empty_tuple = tuple()
print('Empty tuple: ', empty_tuple)
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')
web_techs = ('HTML', 'CSS', 'JS', 'React', 'Vue', 'NodeJS', 'MongoDB', 'PHP', 'Python')
countries = ('VietNam', 'Japan', 'English', 'Sweden', 'United States')
print('Fruits: ', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', vegetables)
print('Number of vegetables: ', len(vegetables))
print('Animal products: ', animal_products)
print('Number of animal products: ', len(animal_products))
print('Web techs: ', web_techs)
print('Number of web techs: ', len(web_techs))
print('Countries: ', countries)
print('Number of countries: ', len(countries))

# Accessing tuple items
first_fruits = fruits[0]
print(first_fruits)
second_fruits = fruits[1]
print(second_fruits)
last_fruits = fruits[len(fruits) - 1]
print(last_fruits)
first_fruits = fruits[-4]
print(first_fruits)
second_fruits = fruits[-3]
print(second_fruits)
last_fruits = fruits[-1]
print(last_fruits)

# Slicing items
all_fruits = fruits[0:4]
print('All fruits: ', all_fruits)
print('All fruit: ', fruits[0:])
print('Orange and mango: ', fruits[1:3])
print('Orange mango lemon: ', fruits[1:])
print('All fruits: ', fruits[-4:])

# Checking items
does_exist = 'apple' in fruits
print('Does apple exist in fruits: ', does_exist)
does_exist = 'lemon' in fruits
print('Does lemon exist in fruits: ', does_exist)

# Change tuples to lists
fruits_list = list(fruits)
fruits_list[0] = 'avocado'
fruits_list[1] = 'apple'
fruits_list[len(fruits_list) - 1] = 'lime'
fruits = tuple(fruits_list)
print('Modified fruits: ', fruits)

# join
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5')
joined_items = tpl1 + tpl2
print('Joined fruits: ', joined_items)

# delete
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

tpl1 = ('item1', 'item2', 'item3')
del tpl1
