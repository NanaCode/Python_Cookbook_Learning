# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/6 20:16'

# re.split() method allow for multiple delimiters or account
# for possible whitespace around the delimiters
line = 'asdf fjdk; afed, fjek,asdf,    foo'
import re

print(re.split(r'[;,\s*]', line))
# ['asdf', 'fjdk', '', 'afed', '', 'fjek', 'asdf', '', '', '', '', 'foo']
print(re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# if capture groups are used, then the matched text is also included in the result
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

# getting the split characters to reform an output string
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
# [' ', ';', ',', ',', ',', '']

# reform the line using the same delimiters
print(''.join(v + d for v, d in zip(values, delimiters)))
# asdf fjdk;afed,fjek,asdf,foo

# use a noncapture group specified as (?:...) to use parentheses to group parts of the regular expression pattern
print(re.split(r'(?:,|;|\s)\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
