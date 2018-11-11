# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/11 11:24'
import re

# match text enclosed inside a pair of starting and ending delimiters
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
# ['no.']
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']

# solve the greedy regular expression problem, make the matching non-greedy
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# ['no.', 'yes.']