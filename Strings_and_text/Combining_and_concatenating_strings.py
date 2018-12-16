# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/17 23:24'

# use join() method to combine the strings in a sequence or iterable
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))
# Is Chicago Not Chicago?
# Is,Chicago,Not,Chicago?
# IsChicagoNotChicago?

# using + if only combining a few strings
a = 'Is Chicago'
b = 'Not Chicago'
print(a+' '+b)
# Is Chicago Not Chicago

# The + operator also works for more complicated string formatting operations
print('{} {}'.format(a, b))
print(a + ' ' + b)
# Is Chicago Not Chicago
# Is Chicago Not Chicago

# Place sring literals adjacent to each other to combine them together in source code
a = 'Hello' 'World'
print(a)
# HelloWorld

# Conversion of data to strings and concatenation at the same time using a generator expression
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
# ACME,50,91.1

# Be on the lookout for unnecessary string concatenations
c = 'Ha Ha'
print(a + ':' + b + ':' + c)
print(':'.join([a, b, c]))
print(a, b, c, sep=':')
# HelloWorld:Not Chicago:Ha Ha
# HelloWorld:Not Chicago:Ha Ha
# HelloWorld:Not Chicago:Ha Ha

# if you're writing code that is building output from lots of small strings, you might consider
# writing that cade as a generator function, using yield to emit fragments
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'
text = ''.join(sample())

# for part in sample():
#     f.write(part)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    f.write(part)
