# 30 Days Of Python Coding Challenge
###################################
# Day 19 - File Handling in Python
###################################
# Opening Files for Reading
f = open('./reading_file_example.txt')
print(f)
txt = f.read()
print(type(txt))
print(txt)
f.close()

f = open('./reading_file_example.txt')
txt10 = f.read(10)
print(type(txt10))
print(txt10)
f.close()

f = open('./reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

f = open('./reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

f = open('./reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

with open('./reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# Opening Files for Writing and Updating
with open('./reading_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end')

with open('./reading_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')

# Deleting Files
import os
if os.path.exists('./example.txt'):
    os.remove('./example.txt')
else:
    print('The file does not exist')

# File Types
## Changing JSON to Dictionary
import json
## JSON
person_json = '''{
    "name": "Trieu",
    "country": "VietNam",
    "city": "DaNang",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

## Changing Dictionary to JSON
# python dictionary
person = {
    "name": "Trieu",
    "country": "VietNam",
    "city": "DaNang",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# Saving as JSON File
import json
# python dictionary
person = {
    "name": "Trieu",
    "country": "VietNam",
    "city": "DaNang",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./person_json.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# File with csv Extension
import csv
with open('./person.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a Web Developer. He lives in {row[1]}, {row[2]}'
            )
            line_count += 1
    print(f'Number of lines: {line_count}')

# File with xlsx Extension
import xlrd
excel_person = xlrd.open_workbook('./person.xls')
print(excel_person.nsheets)
print(excel_person.sheet_names)

# File with xml Extension
import xml.etree.ElementTree as ET
tree = ET.parse('./person.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)