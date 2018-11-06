# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/6 11:23'

# logically combine multiple dictionaries or mappings into a single mapping
# to perform certain operations, such as looking up values or checking for the existence of keys
dict_one = {'x': 1, 'z': 4}
dict_two = {'y': 2, 'z': 5}

from collections import ChainMap
c = ChainMap(dict_one, dict_two)
print(c['x'])
print(c['y'])
print(c['z'])
# 1
# 2
# 4  # if there are duplicate keys, the values from the first mapping get used

# a ChainMap simply keeps a list of the underlying mappings
# and redefines common dictionary operations to scan the list
print(len(c))
print(c.keys)
print(list(c.keys()))
print(c.values())
print(list(c.values()))
# 3
# <bound method Mapping.keys of ChainMap({'x': 1, 'z': 4}, {'z': 5, 'y': 2})>
# ['x', 'z', 'y']
# ValuesView(ChainMap({'x': 1, 'z': 4}, {'z': 5, 'y': 2}))
# [1, 4, 2]

# operations that mutate the mapping always affect the first mapping listed
c['z'] = 88
c['w'] = 99
del c['x']
print(dict_one)
# {'w': 99, 'z': 88}

# del c['y']
# Traceback (most recent call last):
# File
# "C:\Users\Administrator\AppData\Local\Programs\Python\Python35\lib\collections\__init__.py", line
# 932, in __delitem__
#     del self.maps[0][key]
# KeyError: 'y'
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Data_Structures_and_Algorithms/combining_multiple_mappings_into_single_mapping.py", line 39, in <module>
#     del c['y']
#   File "C:\Users\Administrator\AppData\Local\Programs\Python\Python35\lib\collections\__init__.py", line 934, in __delitem__
#     raise KeyError('Key not found in the first mapping: {!r}'.format(key))
# KeyError: "Key not found in the first mapping: 'y'"

# a ChainMap is particularly useful when working with scoped values such as variables
# in a programming language(glocals, locals and etc)
values = ChainMap()
values['x'] = 1
# add a new mapping
values = values.new_child()
values['x'] = 2
# add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
# 3

# discard last mapping
values = values.parents
print(values)
print(values['x'])
# ChainMap({'x': 2}, {'x': 1})
# 2

# discard last mapping
values = values.parents
print(values)
print(values['x'])
# ChainMap({'x': 1})
# 1
# discard last mapping
values = values.parents
print(values)
# ChainMap({})
# print(values['x'])  # 报错：KeyError: 'x'

# merging dictionaries together using the update() method as an alternative to ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
print(merged)
# {'z': 4, 'y': 2}
merged.update(a)
print(merged)
print(merged['x'])
print(merged['y'])
print(merged['z'])
# {'y': 2, 'x': 1, 'z': 3}
# 1
# 2
# 3


c = {'x': 3, 'z': 5}
d = {'y': 4, 'z': 6}
d.update(c)
print(d)
print(d['x'])
print(d['y'])
print(d['z'])
# {'y': 4, 'z': 5, 'x': 3}
# 3
# 4
# 5

# but this requires to make a completely separate dictionary object
# if any of the original dictionaries mutate, the changes don't get reflected in the merged dictionary
a['x'] = 13
print(merged['x'])
# 1

# a ChainMap uses the original dictionaries
e = {'x': 5, 'z': 7}
f = {'y': 6, 'z': 8}
merged = ChainMap(e, f)
print(merged['x'])
e['x'] = 66
print(merged)
print(merged['x'])
# 5
# ChainMap({'z': 7, 'x': 66}, {'z': 8, 'y': 6})
# 66
