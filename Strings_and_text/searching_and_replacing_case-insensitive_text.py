# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/11 11:13'

import re

# use the remodule and supply the re.IGNORECASE flag to various operations to perform case-insensitive text operations
text1 = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text1, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']
print(re.sub('python', 'snake', text1, flags=re.IGNORECASE))


# UPPER snake, lower snake, Mixed snake

# use a support function to fix the limitation that replacing text won't match the case of the matched text
def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(re.sub('python', match_case('snake'), text1, flags=re.IGNORECASE))
# UPPER SNAKE, lower snake, Mixed Snake
