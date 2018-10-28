# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/28 12:00'

# Any sequence(or iterable) can be unpacked into variables using simple assignment operation.
# The only requirement is that the number of varialbles and structures match the sequence.
p = (4, 5)
x, y = p
print(x)
print(y)
# 4
# 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)
# ACME
# (2012, 12, 21)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)
# ACME
# 2012
# 12
# 21

p = (4, 5)
x, y, z = p
print(x)
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Data_Structures_and_Algorithms/unpacking_a_sequence_into_separate_variables.py", line 30, in <module>
#     x, y, z = p
# ValueError: not enough values to unpack (expected 3, got 2)


# Work With:
# any object that happens to be iterable, including strings, files, iterators, and generators
s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(c, d, e)
# H
# e
# l l o

# discard certain values by picking a throwaway variable name
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
# 50
# 91.1


