# 30 Days Of Python Coding Challenge
###################################
# Day 18 - Regular Expressions in Python
###################################
# Match
import re
txt = 'I love to teach python and javascript'
# if returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)
# we can get the starting and ending position of the match as tuple using span
span =  match.span()
print(span)
# Let's find the start and stop position from the span
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

match2 = re.match('I like to teach', txt, re.I)
print(match2)

# Search
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

# Searching for all Matches sing findall
matchs = re.findall('language', txt, re.I)
print(matchs)
matchs2 = re.findall('python', txt, re.I)
print(matchs2)
matchs3 = re.findall('Python|python', txt, re.I)
print(matchs3)
matchs4 = re.findall('[Pp]ython', txt, re.I)
print(matchs4)

# Replacing a Substring
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)
# Or
match_replaced2 = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced2)

# Splitting Text Using RegEx Split
txt = '''I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teraching more interesting than any other jobs.
Does this motivate you to be ateacher?'''
print(re.split('\n', txt))

# Writing RegEx Patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far away.'
match = re.findall(regex_pattern, txt)
print(match)
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'
matchs = re.findall(regex_pattern, txt)
print(matchs)

# Square Bracket
regex_pattern = r'[Aa]pple|[Bb]anana'
matchs = re.findall(regex_pattern, txt)
print(matchs)

# Escape character(\) in RegEx
regex_pattern = r'\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matchs = re.findall(regex_pattern, txt)
print('Escape character in RegEx: ', matchs)

# One or more times(+)
regex_pattern = r'\d+'
matchs = re.findall(regex_pattern, txt)
print('One or more times(+): ', matchs)

# Period(.)
regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matchs = re.findall(regex_pattern, txt)
print('Period(.): ', matchs)
regex_pattern = r'[a].+'
matchs = re.findall(regex_pattern, txt)
print('Period(.)+: ', matchs)

# Zero or one time(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'
matchs = re.findall(regex_pattern, txt)
print('Zero or one time(?) in RegEx: ', matchs)

# Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matchs = re.findall(regex_pattern, txt)
print('Quantifier in RegEx: ', matchs)

regex_pattern = r'\d{1,4}'
matchs = re.findall(regex_pattern, txt)
print('Quantifier in RegEx: ', matchs)

# Cart ^
regex_pattern = r'^This'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matchs = re.findall(regex_pattern, txt)
print('Cart ^ in RegEx: ', matchs)

regex_pattern = r'[^A-Za-z ]+'
matchs = re.findall(regex_pattern, txt)
print('Cart ^ in RegEx: ', matchs)

# Dollar($)
regex_pattern = r'2019$'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matchs = re.findall(regex_pattern, txt)
print('Dollar($) in RegEx: ', matchs)

regex_pattern = r'202[0-1]$'
matchs = re.findall(regex_pattern, txt)
print('Dollar($) in RegEx: ', matchs)
