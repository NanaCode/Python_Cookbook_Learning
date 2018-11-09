# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/9 21:23'

# use basic string methods, such as str.find(), str.endswith(), str.startswith() if the text is simple literal
text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')
# False

# Match at start or end
print(text.startswith('yeah'))
# True

print(text.endswith('no'))
# False

print(text.find('no'))
# 10


# use regular expressions and the re module for more complicated matching
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
# yes
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# no

# precompile the regular expression pattern into a pattern object if performing a lot of matching using the same pattern
datapat= re.compile(r'\d+/\d+/\d+')
if datapat.match(text1):
    print('yes')
else:
    print('no')
# yes
if datapat.match(text2):
    print('yes')
else:
    print('no')
# no

# match() finds the match at the start of a string
# findall() method be used to search text of all occurrences of a pattern
text3 = 'Today is 11/27/2012. Pycon starts at 3/13/2013'
print(datapat.findall(text3))
# ['11/27/2012', '3/13/2013']

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
# <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>

# Exact the contents of each group
print(m.group(0))
# 11/27/2012
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group())
print(m.groups())
# 11
# 27
# 2012
# 11/27/2012
# ('11', '27', '2012')

month, day, year = m.groups()

# Find all matches(notice splitting into tuples)
print('*'*10)
print(text3)
print(datepat.findall(text3))
for month, day, year in datepat.findall(text3):
    print('{}-{}-{}'.format(year, month, day))
# Today is 11/27/2012. Pycon starts at 3/13/2013
# [('11', '27', '2012'), ('3', '13', '2013')]
# 2012-11-27
# 2013-3-13

# use the finditer() method to find matches iteratively
for m in datepat.finditer(text3):
    print(m.groups())
# ('11', '27', '2012')
# ('3', '13', '2013')