#!/usr/bin/env python

'this is the document string'

import math

globalX = 27
globalLst = []
def myFunc(param1=123,param2='hi'):
	localX = 32
	globalX = 28
	print('\n===local namespace===')
	for key,val in locals().items():
		print('key: %s object: %s' % (key, str(val)))
	print('localX:', localX)
	localX = globalX + 1
	print('globalX:', globalX)
	globalLst.append(3)

myFunc()

print('\n===global namespace===')
#for key,val in globals().items():
#	print(key,val)
for key,val in globals().copy().items():
	print('key: %-15s object: %s' % (key, val))

