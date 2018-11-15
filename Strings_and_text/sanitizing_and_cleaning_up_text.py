# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/15 17:38'

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
print('*' * 10)
# pýtĥöñis	awesome
#
# **********

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)
print('*' * 10)
# pýtĥöñ is awesome
#
# **********

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print('*' * 10)
# pýtĥöñ is awesome
#
# **********
print(b.translate(cmb_chrs))
print('*' * 10)
# python is awesome
#
# **********

digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if
            unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# 550 ？？？

# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
# 123

print('*' * 10)
print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
print('*' * 10)


# pýtĥöñ is awesome
#
# python is awesome
#
# **********

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s
