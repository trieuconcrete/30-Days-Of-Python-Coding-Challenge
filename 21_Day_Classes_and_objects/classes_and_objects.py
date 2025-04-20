# 30 Days Of Python Coding Challenge
###################################
# Day 21 - Classes and objects
###################################
# Creating a Class
from tkinter.font import names


class Person:
    pass
print(Person)

# Creating an object
p = Person()
print(p)

## Class Constructor
class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name
p = Person('Trieu')
print(p.name)
print(p)

class Person:
    def __init__(self, first_name, last_name, age, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Trieu', 'Nguyen', 25, 'VietNam', 'DaNang')
print(p.first_name)
print(p.last_name)
print(p.age)
print(p.country)
print(p.city)
print(p.person_info())

## Object default methods
class Person:
    def __init__(self, first_name = 'Trieu', last_name = 'Nguyen', age = 35, country = 'VietNam', city = 'DaNang'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)

p = Person()
p.add_skill('HTML')
p.add_skill('CSS')
p.add_skill('Javascript')
print(p.person_info())
print(p.skills)

class Student(Person):
    pass

s1 = Student('Trieu', 'Nguyen', 20, 'VietNam', 'DaNang')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.person_info())
print(s1.skills)

# Overriding parent method
class Student(Person):
    def __init__(self, first_name = 'Trieu', last_name = 'Nguyen', age = 30, country = 'VietNam', city = 'DaNang', gender = 'male'):
        self.gender = gender
        super().__init__(first_name, last_name, age, country, city)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.first_name} {self.last_name} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s2 = Student('TrieuNguyen', 'Ba', 32, 'VietName', 'DaNang')
print(s2.person_info())
s2.add_skill('Java')
print(s2.skills)