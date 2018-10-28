# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/28 13:06'

# keeping a limited history is a perfect use for a collections.deque
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# Ilovepython
# --------------------
# Ilovepython
# python
# --------------------
# Ilovepython
# python
# yesyesyes
# lovepython
# --------------------
# Ilovepython
# python
# yesyesyes
# lovepython
# oppspython
# --------------------
# python
# yesyesyes
# lovepython
# oppspython
# nonono
# pythonpython--------------------   ???

# using deque creates a fixed-size queue.
# When new itmes are added and the queue is full,the oldest item is automatically removed.
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
# deque([1, 2, 3], maxlen=3)
# deque([2, 3, 4], maxlen=3)
# deque([3, 4, 5], maxlen=3)

# get an unbounded queue that lets you append and pop items on either end
# if you don't give it a maximum size
q =deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
# deque([1, 2, 3])
# deque([4, 1, 2, 3])
# deque([4, 1, 2])
# deque([1, 2])
# adding or popping items from either end of a queue has O(1) complexity
# inserting or removing items from the front of the list is O(N)


