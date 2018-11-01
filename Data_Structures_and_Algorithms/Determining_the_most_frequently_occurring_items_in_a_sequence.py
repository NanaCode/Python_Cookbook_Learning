# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/1 15:37'

# The collections.Counter class
# most_common() method
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]
top_ten = word_counts.most_common(10)
print(top_ten)
# [('eyes', 8), ('the', 5), ('look', 4), ('my', 3), ('into', 3), ('around', 2),
# ('not', 1), ('under', 1), ("don't", 1), ("you're", 1)]

# a Counter object is a dictionary that maps the items to the number of occurrences
print(word_counts['not'])
print(word_counts['eyes'])
# 1
# 8

# use addition if you want to increment the count manually
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in more_words:
    word_counts[word] += 1
print(word_counts['eyes'])
# 9

# alternatively, you could use the update() method
word_counts.update(more_words)
print(word_counts['eyes'])
# 9

# Counter instances can be easily combined using various mathematical operations
a = Counter(words)
b = Counter(more_words)
print(a)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'my': 3, 'into': 3, 'around': 2, 'under': 1, "don't": 1, "you're": 1, 'not': 1})
print(b)
# Counter({'my': 1, 'are': 1, 'looking': 1, 'you': 1, 'why': 1, 'in': 1, 'not': 1, 'eyes': 1})
c = a + b
print(c)
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'around': 2, 'not': 2, 'you': 1, "you're": 1, 'are': 1, 'in': 1, 'under': 1, "don't": 1, 'looking': 1, 'why': 1})
d = a - b
print(d)
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, "don't": 1, 'under': 1, "you're": 1})

# Counter objects are a tremendously useful tool for almost any kind of problem where you need
# to tabulate and count data.
