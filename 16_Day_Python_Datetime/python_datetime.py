# 30 Days Of Python Coding Challenge
###################################
# Day 16 - Python Datetime
###################################
import datetime
print(dir(datetime))

# Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)
print('Day: ', now.day)
print('Month: ', now.month)
print('Year: ', now.year)
print('Hour:', now.hour)
print('Minute: ', now.minute)
print('Second: ', now.second)
print('Timestamp: ', now.timestamp())
print('{}/{}/{}'.format(now.day, now.month, now.year))

# Formatting Date Output Using strftime
new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute, second)
print('{}/{}/{}'.format(day, month, year))

t = now.strftime("%H:%M:%S")
print("time: ", t)
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
print('Time one:', time_one)
time_two = now.strftime("%m/%d/%Y, %H:%M:%S")
print('Time one:', time_two)

# String to time using strptime
from datetime import datetime
date_String = "5 December, 2019"
print("Date string = ", date_String)
date_object = datetime.strptime(date_String, "%d %B, %Y")
print('Date object = ', date_object)

# Using date from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date: ', d.today())
# date object of today's day
today = date.today()
print('Current year: ', today.year)
print('Current month: ', today.month)
print('Current day: ', today.day)

# Time Object to represent time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print('a = ', a)
b = time(10, 30, 50)
print('b = ', b)
d = time(10, 30, 50, 20000)
print('d = ', d)

# Difference between two points in time using
today = date(year=2020, month=12, day=5)
new_year = date(year=2021, month=1, day=1)
time_left_for_newyear = new_year-today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(2020, 12, 5, 0, 59, 0)
t2 = datetime(2021, 1, 1, 0, 0, 0)
diff = t2-t1
print('Time left for new year: ', diff)

# Difference between two points in time using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(weeks=7, days=7, hours=3, seconds=30)
t3 = t1-t2
print('t3 = ', t3)









