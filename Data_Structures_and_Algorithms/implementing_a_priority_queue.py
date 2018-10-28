# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/28 15:58'

# implement a queue that sorts itmes by a given priority and always returns the item with the
# highest priority on each pop operation

# use the heapq module to implement a simple priority queue
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 1)
q.push(Item('spam'), 1)
q.push(Item('grok'), 1)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
# <__main__.PriorityQueue object at 0x0000023883698198>
# Item('foo')
# Item('bar')
# Item('spam')
# Item('grok')

# instances of Item can't be ordered
# a = Item('foo')
# b = Item('bar')
# print(a < b)
#   File "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Data_Structures_and_Algorithms/implementing_a_priority_queue.py", line 51, in <module>
#     print(a<b)
# TypeError: unorderable types: Item() < Item()

# (priority, item) tuples can be compared as long as the priorities are different
# But if two tuples with equal priorities are compared, the comparison fails as before
a = (1, Item('foo'))
b = (5, Item('bar'))
# print(a < b)
c = (1, Item('grok'))
# print(a < c)
# True
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Data_Structures_and_Algorithms/implementing_a_priority_queue.py", line 63, in <module>
#     print(a < c)
# TypeError: unorderable types: Item() < Item()

# introducing the extra index and making(priority, index, item) tuples
# no two tuples will ever have the same value for index
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
# True
print(a < c)
# True
# if use this queue for communication between threads,
# you will need to add appropriate locking and signaling
