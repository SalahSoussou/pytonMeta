import sys

pathes = sys.path

#for i in pathes:
#   print(i)

import calendar

leap = calendar.leapdays(2000,2020)
print(leap)
print('text from pathes')