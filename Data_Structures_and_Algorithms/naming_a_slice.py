# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/1 8:10'

# clean the unreadable mess of hardcoded slice indices up

# the built-in slice() creates a slice object that can be used anywhere a slice is allowed
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2: 4])
print(items[a])
# [2, 3]
# [2, 3]
items[a] = [10, 11]
print(items)
# [0, 1, 10, 11, 4, 5, 6]
del items[a]
print(items)
# [0, 1, 4, 5, 6]

# you can get more information about a slice instances by looking at its s.start, s.stop, s.step
a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
# 10
# 50
# 2

# map a slice onto a sequence of a specific size by using its indices(size) method
s = 'HelloWorld'
print(a.indices(len(s)))
# (10, 10, 2)  ???
print('-'*10)
for i in range(*a.indices(len(s))):
    print(s[i])
# no result???
