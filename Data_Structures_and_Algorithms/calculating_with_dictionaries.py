# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/29 13:39'

# perform various calculations on a dictionary of data
stock_prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.2,
    'FB': 10.75
}

# invert the keys and values of the dictionary using zip()
# to perform useful calculation on the dictionary contents
print(zip(stock_prices.values(), stock_prices.keys()))
# <zip object at 0x000001654FA9E088>
min_price = min(zip(stock_prices.values(), stock_prices.keys()))
max_price = max(zip(stock_prices.values(), stock_prices.keys()))
print(min_price)
print(max_price)
# (10.75, 'FB')
# (612.78, 'AAPL')

prices_sorted = sorted(zip(stock_prices.values(), stock_prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# zip() creates an iterator that can only be consumed once
prices_and_names = zip(stock_prices.values(), stock_prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names))
# Traceback (most recent call last):
# File
# "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Data_Structures_and_Algorithms/calculating_with_dictionaries.py", line
# 32, in < module >
#     print(max(prices_and_names))
# ValueError: max() arg is an empty sequence

# in calculations involving(value, key) pairs, the key will be used to determine the result in instances
# where multiple entried happen to have the same value
prices = {'AAA': 43.2, 'ZZZ': 43.2}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
# (43.2, 'AAA')
# (43.2, 'ZZZ')
prices = {'AAA': 43.2, 'zzz': 43.2}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
# (43.2, 'AAA')
# (43.2, 'zzz')
prices = {'AAA': 43.2, 'aaa': 43.2}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
# (43.2, 'AAA')
# (43.2, 'aaa')


