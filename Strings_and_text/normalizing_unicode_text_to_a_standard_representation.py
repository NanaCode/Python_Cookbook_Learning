# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/13 15:40'

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
# Spicy Jalapeño
# Spicy Jalapeño  ???
print(s1 == s2)
print(len(s1))
print(len(s2))
# False
# 14
# 15

# normalize the text into a standard representation using the unicodedata module
import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
# True
print(ascii(t1))
# 'Spicy Jalape\xf1o'
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
# True
print(ascii(t3))
# 'Spicy Jalapen\u0303o'

# normalization forms NFKC and NFKD to add extra compatibility features for dealing with
# certain kinds of character
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
# ﬁ
# ﬁ

# notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))
# fi
# fi

t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
# Spicy Jalapeno
