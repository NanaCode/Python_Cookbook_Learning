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

# lack of discussion

