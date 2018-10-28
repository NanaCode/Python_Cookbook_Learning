# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/28 12:01'


# solve "too many values to unpack" exception
# star expressions
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)
# Dave
# dave@example.com
# ['773-555-1212', '847-555-1212']   # list regardless of how many phone numbers are unpacked(including none)

# The starred variable can also be the first one in the list
# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)
# return avg_comparision(trailing_avg, current_qtr)
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)
# [10, 8, 7, 1, 9, 5, 10]
# 3

# the star syntax can be especially useful when iterating over a sequence of tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
# foo 1 2
# bar hello
# foo 3 4

# combined with certain kinds of string processing operations, such as splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
# nobody
# /var/empty
# /usr/bin/false

# a star syntax with a common throwaway variable name, such as _ or ign(ignored)
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record  # ???
print(name)
print(year)
# ACME
# 2012

# split into head and tail components
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


# 1
# [10, 7, 4, 5, 9]

# clever recursive algorithm
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head  # ???
items_sum = sum(items)
print(items_sum)
# 36
# noticing: recursion isn't a strong Python feature due to the inherent recursion limit
# this example might be nothing more than an academic curiosity in practice  # ???



