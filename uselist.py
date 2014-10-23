#!/usr/bin/env python

astr = 'iceman'
bstr = 'cinema'

alist = sorted(astr)
blist = sorted(bstr)

if (alist == blist):
	print("%s and %s contains the same charactors" % (astr, bstr))
else:
	print("%s and %s are consists of different charactors" % (astr, bstr))
	
print('sorted string of %s is %s' % (astr, ''.join(alist)))
print('%s joined by %s is %s' % (astr, ',', ','.join(astr)))
