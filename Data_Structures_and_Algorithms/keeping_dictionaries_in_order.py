# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/10/29 13:27'

# create a dictionary and control the order of items when iterating or serializing
# OrderedDict from the collections module exactly preserves the original insertion order of data when iterating
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d)
# OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])
for key in d:
    print(key, d[key])
# foo 1
# bar 2
# spam 3
# grok 4

# OrderedDict can be particularly useful when building a mapping to later serialize or encode into a different format
# precisely control the order of fields appearing in a JSON encoding
import json
f = json.dumps(d)
print(f)
# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}
