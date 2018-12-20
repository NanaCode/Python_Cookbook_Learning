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

