# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/28 14:25'

# the heapq module has two functions--nlargest() and nsmallest()

import heapq

nums = [1, 8, 2, 34, 6, 8, -4, 2, 56, 10, 78]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
# [78, 56, 34]
# [-4, 1, 2]

# both functions accept a key parameter that allows them to be used with more complicated data structures
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

small_shares = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
large_shares = heapq.nlargest(3, portfolio, key=lambda s: s['shares'])

print(cheap)
print(expensive)
print(small_shares)
print(large_shares)
# [{'price': 16.35, 'shares': 45, 'name': 'YHOO'}, {'price': 21.09, 'shares': 200, 'name': 'FB'}, {'price': 31.75, 'shares': 35, 'name': 'HPQ'}]
# [{'price': 543.22, 'shares': 50, 'name': 'AAPL'}, {'price': 115.65, 'shares': 75, 'name': 'ACME'}, {'price': 91.1, 'shares': 100, 'name': 'IBM'}]
# [{'price': 31.75, 'shares': 35, 'name': 'HPQ'}, {'price': 16.35, 'shares': 45, 'name': 'YHOO'}, {'price': 543.22, 'shares': 50, 'name': 'AAPL'}]
# [{'price': 21.09, 'shares': 200, 'name': 'FB'}, {'price': 91.1, 'shares': 100, 'name': 'IBM'}, {'price': 115.65, 'shares': 75, 'name': 'ACME'}]


# work by first comverting the data into a list where itmes are ordered as a heap
nums = [1, 8, 2, 23, 7, -4, 18, 23, 43, 37, 2]
import heapq

heap = list(nums)  # ???
print(heap)
heapq.heapify(heap)
print(heap)
# [1, 8, 2, 23, 7, -4, 18, 23, 43, 37, 2]
# [-4, 2, 1, 23, 7, 2, 18, 23, 43, 37, 8]

# the most important feature of a heap is that heap[0] is always the smallest item
# heapq.heappop() method pops off the first item and replaces it with the next smallest item(OlogN))
# heapq.heappop(heap)
# print(heap)
# heapq.heappop(heap)
# print(heap)
# heapq.heappop(heap)
# print(heap)
# [1, 2, 2, 23, 7, 8, 18, 23, 43, 37]
# [2, 2, 8, 23, 7, 37, 18, 23, 43]
# [2, 7, 8, 23, 43, 37, 18, 23]
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
# -4
# 1
# 2

# find a relatively small number of items:  nlargest() and nsmallest()
# fimd the single smallest or largest itme(N=1):  min() and max()
# N is about the same size as the collection ifself:
# sort it first and take a slice use sorted(items)[:N] or sorted(items)[-N:])F