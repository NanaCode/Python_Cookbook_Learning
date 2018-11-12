# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/12 11:27'

import re

# match C-style comments
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
              multiline comment */'''
print(comment.findall(text1))
# [' this is a comment ']
print(comment.findall(text2))
# []

# add support for newlines
# (?:.|\n) specifies a noncapture group
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text1))
# [' this is a comment ']
print(comment.findall(text2))
# [' this is a \n              multiline comment ']

# the re.compile() function accepts a flag, re.DOTALL which makes the . in a regular expression
# match all characters, including newlines.
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
# [' this is a \n              multiline comment ']
