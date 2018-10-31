# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/31 17:37'


# using a set and a generator if the values in the sequence are hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# [1, 5, 2, 9, 10]


# eliminate duplicates in a sequence of unhashable types(such as dicts)
# using a set and a generator if the values in the sequence are hashable
def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # converts sequence items into a hashable type
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_unhashable(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_unhashable(a, key=lambda d: d['x'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# make a set if only want to eliminate duplicates
# but this approach doesn't preserve any kind of ordering
c = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(c))
# {1, 2, 10, 5, 9}

# read a file, eliminate duplicate lines
with open(somefile, 'r') as f:
    for line in dedupe(f):
        ...











