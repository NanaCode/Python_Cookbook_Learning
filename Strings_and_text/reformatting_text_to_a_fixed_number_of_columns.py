# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/12/18 23:11'

# Use the textwrap module to reformat text for output
s = "Look into my eyes, look into my eyes, the eyes, the eyes, " \
    "the eyes, not aroung the eyes, do't look around the eyes," \
    "look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))
# Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
# not aroung the eyes, do't look around the eyes,look into my eyes,
# you're under.

print(textwrap.fill(s, 40))
# Look into my eyes, look into my eyes,
# the eyes, the eyes, the eyes, not aroung
# the eyes, do't look around the eyes,look
# into my eyes, you're under.

print(textwrap.fill(s, 40, initial_indent='     '))
#      Look into my eyes, look into my
# eyes, the eyes, the eyes, the eyes, not
# aroung the eyes, do't look around the
# eyes,look into my eyes, you're under

print(textwrap.fill(s, 40, subsequent_indent='     '))
# Look into my eyes, look into my eyes,
#      the eyes, the eyes, the eyes, not
#      aroung the eyes, do't look around
#      the eyes,look into my eyes, you're
#      under.

# On the subject of the terminal size, you can obtain it using os.get_terminal_size()
import os
print(os.get_terminal_size().columns)
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python cookbook学习/Python_Cookbook_Learning/Strings_and_text/reformatting_text_to_a_fixed_number_of_columns.py", line 37, in <module>
#     print(os.get_terminal_size().columns)
# OSError: [WinError 6] 句柄无效。