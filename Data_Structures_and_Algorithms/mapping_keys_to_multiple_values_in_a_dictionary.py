# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/29 13:05'

# make a dictionary that maps keys to more than one value(a so-called multidict)
# store the multiple values in another container such as a list or set
# use a list to preserve the insertion order of the items
# use a set to eliminate duplicates
a = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# feature of defaultdict is that it automatically initializes the first value so you can simply
# focus on adding items
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(6)
d['b'].append(8)
print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4, 6, 8]})

f = defaultdict(set)
f['a'].add(1)
f['a'].add(2)
f['a'].add(3)
f['b'].add(4)
f['b'].add(6)
print(f)
# defaultdict(<class 'set'>, {'a': {1, 2, 3}, 'b': {4, 6}})

# defaultdict will automatically create dictionary entries for keys accessed later on
# use setdefault() on an ordinary dictionary instead
g = {}
g.setdefault('a', []).append(1)
g.setdefault('a', []).append(2)
g.setdefault('b', []).append(4)
print(g)
# {'a': [1, 2], 'b': [4]}

# initialization of the first value by yourself
# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

# using a defaultdict simply leads to much cleaner code
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)

