# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/3 15:51'

# extract values or reduce the sequence using some criteria

# the easiest way to filter sequence data is to use a list comprehension
my_list = [1, 4, -5, 10, -7, 2, 3, -1]
a = [n for n in my_list if n > 0]
print(a)
# [1, 4, 10, 2, 3]
b = [n for n in my_list if n < 0]
print(b)
# [-5, -7, -1]

# generator expressions to product the filtered values iteratively
pos = (n for n in my_list if n > 0)
print(pos)
for x in pos:
    print(x)
# <generator object <genexpr> at 0x000001C2D5BC1AF0>
# 1
# 4
# 10
# 2
# 3

# put the filtering code into its own function and use the built-in filter() function
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# ['1', '2', '-3', '4', '5']

# list comprehensions and generator expressions have the added power to transform the data
# at the same time
my_list = [1, 4, -5, 10, -7, 2, 3, -1]
import math

a = [math.sqrt(n) for n in my_list if n > 0]
print(a)
# [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

# one variation on filtering involves replacing the values that don't meet the criteria
# with a new value instead of discarding them
clip_neg = [n if n > 0 else 0 for n in my_list]
print(clip_neg)
# [1, 4, 0, 10, 0, 2, 3, 0]
clip_pos = [n if n < 0 else 0 for n in my_list]
print(clip_pos)
# [0, 0, -5, 0, -7, 0, 0, -1]

# itertools.compress() takes an iterable and an accompanying Boolean selector sequence as input
# As output, it gives you all of the items in the iterable where the corresponding element in the selector is Tre
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))
# [False, False, True, False, False, True, True, False]
# ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
