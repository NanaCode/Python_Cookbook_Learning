# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/2 8:09'

# operator module's itemgetter function
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# output these rows ordered by any of the fields common to all of the dictionaries
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
# [{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'}, {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'}, {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'}, {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'}]
# [{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'}, {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'}, {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'}, {'fname': 'Big', 'uid': 1004, 'lname': 'Jones'}]

# the itemgetter() function alse accept multiple keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
# [{'lname': 'Beazley', 'fname': 'David', 'uid': 1002}, {'lname': 'Cleese', 'fname': 'John', 'uid': 1001}, {'lname': 'Jones', 'fname': 'Big', 'uid': 1004}, {'lname': 'Jones', 'fname': 'Brian', 'uid': 1003}]
# 最后两个有疑义？？？

# the functionality of itemgetter() is sometimes replaced by lambda expressions
# however, the solution involving itemgetter() typically runs a bit faster
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_fname)
print(rows_by_lfname)
# [{'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}, {'lname': 'Jones', 'uid': 1003, 'fname': 'Brian'}, {'lname': 'Beazley', 'uid': 1002, 'fname': 'David'}, {'lname': 'Cleese', 'uid': 1001, 'fname': 'John'}]
# [{'lname': 'Beazley', 'uid': 1002, 'fname': 'David'}, {'lname': 'Cleese', 'uid': 1001, 'fname': 'John'}, {'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}, {'lname': 'Jones', 'uid': 1003, 'fname': 'Brian'}]

# the technique shown in this recipe can be applied to functions such as min() and max()
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}





