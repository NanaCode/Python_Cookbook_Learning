# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/7 9:42'

# check the start of end of a string for specific text patterns, such as filename extensions, URL schemas, etc

# str.starts() or str.endswith()
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.endswith('txt'))
# True
# True
print(filename.startswith('file:'))
# False
url = 'http://www.python.org'
print(url.startswith('http:'))
# True

# provide a tuple of possibilities to startswith() or endswith() if need to check against multiple choices
import os

filenames = os.listdir('.')
print(filenames)
# ['matching_text_at_the_start_or_end_of_a_string.py', 'splitting_strings_on_any_of_multiple_delimiters.py', '__init__.py']
print([name for name in filenames if name.endswith(('.c', '.h'))])
# []
print(any(name.endswith('.py') for name in filenames))
# True

from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# a tuple is required as input
# if the choices specified in a list or set, make sure you convert them using tuple() first
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices))
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Strings_and_text/matching_text_at_the_start_or_end_of_a_string.py", line 42, in <module>
#     print(url.startswith(choices))
# TypeError: startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))
# True

# startswith() and endswith() methods can perform basic prefix and suffix checking
# slices can perform basic prefix and suffix checking too, but are far less elegant
filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')
# True

# use regular expressions as an alternative
import re

url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
# <_sre.SRE_Match object; span=(0, 5), match='http:'>

# checks a directory for the presence of certain kinds of files
dirname = 'xxx'
if any(name.endswith(('.c', '.h')) for name in os.listdir(dirname)):
    pass