# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/14 21:34'

# strip unwanted characters

# whitespace stripping
s = '   hello world  \n'
print(s.strip())
print(s.lstrip()) # notice
print('-'*10)
print(s.rstrip())
print('-'*10)
# hello world
# hello world
#
# ----------
#    hello world
# ----------

# character stripping
print('*'*10)
t = '-----hello====='
print(t.lstrip('-'))
print('*'*5)
print(t.lstrip('-='))
print('*'*6)
print(t.rstrip('='))
print('*'*7)
print(t.rstrip('-='))
print('*'*8)
print(t.strip('-='))
# **********
# hello=====
# *****
# hello=====
# ******
# -----hello
# *******
# -----hello
# ********
# hello
