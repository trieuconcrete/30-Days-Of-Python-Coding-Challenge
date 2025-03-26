# 30 Days Of Python Coding Challenge
###################################
# Day 7 - Sets in Python
###################################
st = set() # Empty set
st = {'item1', 'item2', 'item3', 'item4', 'item5'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Number of ST: ', len(st))
print('Number of Fruits: ', len(fruits))

# Checking items in a set
print('Does set st contain item6: ', 'item6' in st)
print('Does set fruits contain banana: ', 'banana' in fruits)

# Adding items to a set
st = {'item1', 'item2', 'item3', 'item4', 'item5'}
st.add('item6')
print('ST after adding item6: ', st)
st.update(['item7', 'item8', 'item9'])
print('ST after updating: ', st)

# Removing items from a set
st.remove('item2')
print('ST after removing item2: ', st)
fruits.pop()
print('ST after popping: ', fruits)

# Clearing items in a set
st.clear()
print('ST after clearing: ', st)
fruits.clear()
print('Fruits after clearing: ', fruits)

# Delete a set
st = {'item1': 'item2', 'item3': 'item4'}
del st

# Convert list to set
lst = ['item1', 'item2', 'item3', 'item4']
st = set(lst)
print('Set from list: ', st)

# Join sets
st1 = {'item1', 'item2'}
st2 = {'item3', 'item4'}
st3 = st1.union(st2)
print('Union of st1 and st2: ', st3)

# Finding intersection items
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print('Intersection of python and dragon: ', python.intersection(dragon))

# Checking subset and super set
st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}
print('Is st1 a subset of st2: ', st1.issubset(st2))
print('Is st1 a superset of st2: ', st1.issuperset(st2))

# Checking the difference between the two sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2', 'item4'}
print('Difference between st1 and st2: ', st1.difference(st2))
print('Difference between st2 and st1: ', st2.difference(st1))

# Checking symmetric difference
st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2', 'item4'}
print('Symmetric difference between st1 and st2: ', st1.symmetric_difference(st2))
print('Symmetric difference between st2 and st1: ', st2.symmetric_difference(st1))

# Joining sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2', 'item4'}
print('Joining sets: ', st1.isdisjoint(st2))
