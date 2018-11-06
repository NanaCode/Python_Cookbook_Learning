# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/5 17:34'

# combine a data reductin and a transformation using a generator-expression argument
# Examples as follow:

# calculate the sum of the squares
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)
# 55

# Determine if any .py files exist in a directory
import os

files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python file!')
else:
    print('Sorry, no python!')

# Output a tuple as CSV
s = ('ACME', 50, 123.5)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [{'name': 'ABC', 'shares': 50},
             {'name': 'BCD', 'shares': 75},
             {'name': 'CDE', 'shares': 20},
             {'name': 'DEF', 'shares': 65}, ]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# 20

test_nums = [1, 2, 3, 4, 5]
e = sum((x * x for x in nums))
f = sum(x * x for x in nums)
g = sum([x * x for x in nums])
print(e)
print(f)
print(g)
# 55
# 55
# 55

# reduction functions such as min() and max() accept a key argument that might be useful in situations
# where you might be inclined to use a generator.
# Original
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# 20

# Alternative： Returns
min_shares = min(portfolio, key = lambda s: s['shares'])
print(min_shares)
# {'shares': 20, 'name': 'CDE'}