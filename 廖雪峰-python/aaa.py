# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import time

print(datetime.now())
print(datetime(2018, 1, 10, 11, 31, 20))
a = datetime.now()
b = a.timetuple()
print(time.mktime(b))

c = time.mktime(datetime.now().timetuple())
time1 = datetime.fromtimestamp(c).strftime('%Y-%m-%d %H:%M:%S')
time2 = datetime.utcfromtimestamp(c).strftime('%Y-%m-%d %H:%M:%S')
time3 = datetime.utcfromtimestamp(c)
print(isinstance(time3, datetime))
d = datetime(2019, 1, 10, 11, 53, 30)
print(d.strftime('%a %b %d %X'))
ab = '2019-1-20 09:20:24'
print(datetime.strptime(ab, '%Y-%m-%d %H:%M:%S'))

dd = datetime.now()
print(dd + timedelta(hours=1))
print(dd - timedelta(days=10, minutes=45))
print(dd + timedelta(minutes=200))