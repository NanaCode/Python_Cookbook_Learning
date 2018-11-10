# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/10 20:43'

# use str.replace() method for simple literal patterns
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
# yep, but no, but yep, but no, but yep

# use the sub() functions/methods in the re module for more complicated patterns
text = 'Today is 11/27/2012. Pycon starts at 3/13/2013'
import re

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# Today is 2012-11-27. Pycon starts at 2013-3-13

# compiling it first for better performance to perform repeated substitutions
import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
# Today is 2012-11-27. Pycon starts at 2013-3-13

# specify a substitution callback function for more complicated substitutions
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))
# Today is 27 Nov 2012. Pycon starts at 13 Mar 2013

# use re.subn() to know how many subsitutions were made in addition to getting the replacement rext
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
# Today is 2012-11-27. Pycon starts at 2013-3-13
# 2









