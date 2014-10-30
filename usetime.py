#!/usr/bin/env python

''''an example of using time lib to get local time'''

import time

m = time.localtime()
print("Today's date is: %d-%d-%d" % (m.tm_year, m.tm_mon, m.tm_mday))
print("Now Time is: %d:%d:%d" % (m.tm_hour, m.tm_min, m.tm_sec))

