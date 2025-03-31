# 30 Days Of Python Coding Challenge
###################################
# Day 11 - Modules in Python
###################################
def generate_full_name(first_name, last_name):
    sppace = ' '
    full_name = first_name + sppace + last_name
    return full_name

def sum_two_numbs(num1, num2):
    return num1 + num2

def calculate_age(current_year, birth_year):
    return current_year - birth_year

gravity = 9.81
person = {
    'first_name': 'Trieu',
    'last_name': 'Nguyen',
    'age': calculate_age(2025, 1990),
}