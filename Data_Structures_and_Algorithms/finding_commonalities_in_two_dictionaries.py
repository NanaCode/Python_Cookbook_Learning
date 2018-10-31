# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/31 8:45'

# find out what two dictionaries might have in common(same values, same keys, etc)
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# perform common set operations using the keys() or items() methods
same_key = a.keys() & b.keys()
not_same_key = a.keys() - b.keys()
same_items = a.items() & b.items()
print(same_key)
print(not_same_key)
print(same_items)
# {'x', 'y'}
# {'z'} # attention!!!
# {('y', 2)}

# alter or filter dictionary contents
# make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
# {'x': 1, 'y': 2}

# The keys() method of a dictionary returns a keys_view object that exposes the keys.
# The keys views supports common set operations such as unions, intersections and differences.

# The items() method of a dictionary returns an items-view object consisting of (key, value) pairs.
# The items-view object supports similar set operations and can be used to perform operations.

# But the values() method of a dictionary does not support the set operations described in this recipe.
# Because unlike keys, the items contained in a values view aren't guaranteed to be unique.










