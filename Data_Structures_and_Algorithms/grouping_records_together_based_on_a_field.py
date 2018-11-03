# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/11/3 15:34'

# iterate over the data in a sequence of dictionaries or instances based on the value of a particular field

# itertools.groupby() function
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# sort by the desired field first
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)


# 07/01/2012
#      {'date': '07/01/2012', 'address': '5412 N CLARK'}
#      {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
# 07/02/2012
#      {'date': '07/02/2012', 'address': '5800 E 58TH'}
#      {'date': '07/02/2012', 'address': '5645 N RAVENWOOD'}
#      {'date': '07/02/2012', 'address': '1060 W ADDISON'}
# 07/03/2012
#      {'date': '07/03/2012', 'address': '2122 N CLARK'}
# 07/04/2012
#      {'date': '07/04/2012', 'address': '5148 N CLARK'}
#      {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
for r in rows_by_date['07/01/2012']:
    print(r)
# {'address': '5412 N CLARK', 'date': '07/01/2012'}
# {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
