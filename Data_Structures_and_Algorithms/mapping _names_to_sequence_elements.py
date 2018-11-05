# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/4 8:06'

# collections.namedtuple()
from collections import namedtuple  # 注意是namedtuple不是nametuple

Student = namedtuple('Student', ['classes', 'grade'])  # 写class会报错呢
peter = Student('3', '2')  # 错误写法：peter = Student('Peter', ['3', '2'])
print(peter)
print(peter.classes)
print(peter.grade)
# Student(classes='3', grade='2')
# 3
# 2

# an instance of a namedtuple is interchangeable with a tuple and supports
# all of the usual tuple operations such as indexing and unpacking
print(len(peter))
classes, grade = peter
print(classes, grade)

# 2
# 3 2

# a major use case for named tuples is decoupling your code from the position of the elements it manipulates

# using ordinary tuples, a bit less expressive and more dependent on the structure of the records
# def compute_cost(records):
#     total = 0.0
#     for rec in records:
#         total += rec[1] * rec[2]
#     return total


from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# namedtuple is immutable
s = Stock('KFC', 100, 123.5)
print(s)
print(s.shares)
# s.shares = 75  # 报错：AttributeError: can't set attribute
# Stock(name='KFC', shares=100, price=123.5)
# 100
# Traceback (most recent call last):
# File
# "C:/Users/Administrator/Desktop/Python_Cookbook_Learning/Data_Structures_and_Algorithms/mapping _names_to_sequence_elements.py", line
# 52, in < module >
# s.shares = 75
# AttributeError: can't set attribute

# change of the attributes can be done by using the _replace() method of a namedtuple instance
# which makes an entirely new namedtuple with specified values
s = s._replace(shares=75)
print(s)
# Stock(name='KFC', shares=75, price=123.5)

print('-'*20)
# subtle use of the _replace() method: populate named tuples that have optional or missing fields
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'MC', 'shares': 99, 'price': 123.8}
print(dict_to_stock(a))
b = {'name': 'MC', 'shares': 99, 'price': 123.8, 'date': '12/17/2012'}
print(dict_to_stock(b))
# Stock(name='MC', shares=99, price=123.8, date=None, time=None)
# Stock(name='MC', shares=99, price=123.8, date='12/17/2012', time=None)

# if goal is to define an efficient data structure where you will be changing various instance
# attributes, consider defining a class using __slots__ instead of using namedtuple.