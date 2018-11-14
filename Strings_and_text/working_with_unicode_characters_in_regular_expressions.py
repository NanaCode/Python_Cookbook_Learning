# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/14 21:24'

# \d matches any unicode digit character
import re
num = re.compile('\d+')
# ASCII digits
print(num.match('123'))
# <_sre.SRE_Match object; span=(0, 3), match='123'>

# Arabic digits
print(num.match('\u0661\u0662\u0663'))
# <_sre.SRE_Match object; span=(0, 3), match='١٢٣'>

arabic = re.compile('[\0600-\u06ff\u0750-\u077f\u08a0-\u08ff]')
print(arabic)
# re.compile('[00-ۿݐ-ݿࢠ-ࣿ]')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
print(pat)
s = 'straße'
print(pat.match(s))
# <_sre.SRE_Match object; span=(0, 6), match='straße'>
print(pat.match(s.upper()))
# None
print(s.upper())
# STRASSE
