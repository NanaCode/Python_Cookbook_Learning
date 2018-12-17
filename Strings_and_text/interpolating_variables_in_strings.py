# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/17 22:04'

# Use the format() method of strings for simply substituting variable values in strings
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))
# Guido has 37 messages.

# Use the combination of format_map() and vars()
# if the values to be substituted are truly found in variables
name = 'Guido'
n = 37
print(s.format_map(vars()))


# Guido has 37 messages.

# One subtle feature of vars() is that it also works with instances.
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))


# Guido has 37 messages.

# One downside of format() and format_map() is that they do not deal gracefully
# with missing values
# print(s.format(name='Guido'))
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python cookbook学习/Python_Cookbook_Learning/Strings_and_text/interpolating_variables_in_strings.py", line 32, in <module>
#     print(s.format(name='Guido'))
# KeyError: 'n'

# Define a alternative dictionary class with a __missing__() method
class Safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


# Use class Safesub to wrap the inputs to format_map()
del n
print(s.format_map(Safesub(vars())))
# Guido has {n} messages.

# frame hack
import sys


def sub(text):
    return text.format_map(Safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
# Hello Guido
# You have 37 messages.
# Your favorite color is {color}

# name = 'Guido'
# n = 37
print('%(name) has %(n) messages.' % vars())
# Bug:ValueError: unsupported format character 'm' (0x6d) at index 17 ???

import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
# Guido has 37 messages.

