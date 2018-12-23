# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/19 22:17'

# Use the html.escape() to replace special characters such as < or >
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
# Elements are written as "<tag>text</tag>".
print(html.escape(s))
# Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.
print(html.escape(s, quote=False))
# Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

# Use the errors = 'xmlcharrefreplace' argument to various I/O-related functions
# to emit text as ASCII and embed character code entities
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
# b'Spicy Jalape&#241;o'

# Replace manually if receiving bare text with some entities
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))
# Spicy "Jalapeño".

t = 'The promt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
# The promt is >>>

