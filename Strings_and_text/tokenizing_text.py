# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/24 6:50'

text = 'foo = 23+42 *10'

tokens = [('name', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# Defind all the possible tokens, including whitespace by regular expression pattens
# using named capture groups
import re

NAME = r'(?P<NAME>[a-zA-Z_}[a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\+)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# use the little-known scanner() method
scanner = master_pat.scanner('foo=42')
print(scanner.match())
# <_sre.SRE_Match object; span=(0, 3), match='foo'>
print(_.lastgroup, _.group())
# Traceback (most recent call last):
# <_sre.SRE_Match object; span=(0, 3), match='foo'>
#   File "C:/Users/Administrator/Desktop/Python cookbook学习/Python_Cookbook_Learning/Strings_and_text/tokenizing_text.py", line 27, in <module>
#     print(_.lastgroup, _.group())
# NameError: name '_' is not defined