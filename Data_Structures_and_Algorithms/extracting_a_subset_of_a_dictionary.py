# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/3 16:26'

# dictionary comprehension
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.2,
    'FB': 10.75
}
# make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# {'IBM': 205.55, 'AAPL': 612.78}

# make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
# {'IBM': 205.55, 'AAPL': 612.78, 'HPQ': 37.2}

# creating a sequence of tuples and passing them to the dict() function
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)
# {'AAPL': 612.78, 'IBM': 205.55}

# rewritten: make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p2)
# {'HPQ': 37.2, 'IBM': 205.55, 'AAPL': 612.78}
