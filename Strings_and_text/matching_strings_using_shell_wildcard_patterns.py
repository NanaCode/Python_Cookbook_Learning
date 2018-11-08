# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/8 10:22'

# two functions of the fnmatch module - fnmatch() and fnmatchcase()
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
# True
# True
# True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# ['Dat1.csv', 'Dat2.csv']

print(fnmatch('foo.txt', '*.TXT'))
# True
# On OS X(Mac) system, the result is False

# fnmatchcase() matches exactly based on the lower- and uppercase conventions
print(fnmatchcase('foo.txt', '*.TXT'))
# False

# data processing of nonfilename strings
addresses = [
    '5412 N CLARK ST',
    '5060 W ADDISON ST',
    '1039 W GRANVILLE ACE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

# list comprehensions
from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
# ['5412 N CLARK ST', '5060 W ADDISON ST', '2122 N CLARK ST']
# ['5412 N CLARK ST']
