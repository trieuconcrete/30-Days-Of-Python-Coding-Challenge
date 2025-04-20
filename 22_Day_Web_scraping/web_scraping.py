# 30 Days Of Python Coding Challenge
###################################
# Day 22 - Web scraping
###################################
# Install packages
## pip install requests
## pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/dataset/19/car+evaluation'
# Lets use the request get method to fetch the data from url
response = requests.get(url)
# lets check the status
status = response.status_code
print(status)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
# print(soup.body)
tables = soup.find_all('table')
print(tables)
table = tables[0]
print(table)
print(table.find('tr'))
for th in table.find('tr').find_all('th'):
    print('table tr th: ', th.text)