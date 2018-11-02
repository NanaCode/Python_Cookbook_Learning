# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/2 20:04'

from operator import attrgetter


# sort objects of the same class which don't natively support comparison operations

# The built-in sorted() functioin takes a key argument that can be passed a callable
# that will return some value in the object that sorted will use to compare the objects
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))
# [User(23), User(3), User(99)]
# [User(3), User(23), User(99)]

# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
# User(3)
# User(99)
