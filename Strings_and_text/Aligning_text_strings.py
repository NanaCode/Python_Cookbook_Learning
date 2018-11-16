# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/16 11:45'

# the ljust(), rjust(), and center() methods of strings can be used for basic alignment of strings
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
# Hello World
#          Hello World
#     Hello World

print(text.rjust(20, '='))
print(text.center(20, '*'))
# =========Hello World
# ****Hello World***** ???为什么是9

# the format() function can be used to easily align things using the <, >, or ^ characters
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
#          Hello World
# Hello World
#     Hello World

# include a fill character other than a space, specify it before the alignment character
print(format(text, '=>20s'))
print(format(text, '*^20s'))
# =========Hello World
# ****Hello World*****

# these format codes can be used in the format() method when formatting multiple values
print('{:>10s} {:>10s}'.format('Hello', 'World'))
# Hello      World

# format() is not specific to strings
x = 1.234
print(format(x, '>10'))
print(format(x, '^10.2f'))
#   1.234
# 1.23

print('%-20s' % text)
print('%20s' % text)
# Hello World
#          Hello World
