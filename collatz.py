#!/usr/bin/env python

'考拉兹猜想-冰雹序列'

numStr = input('Enter a positive integer: ')
numInt = int(numStr)

count = 0

print('Starting with number:', numInt)
print('Sequence is:')

while numInt > 1:
    if numInt % 2:
        numInt = numInt * 3 + 1
    else:
        numInt = numInt // 2
    print(numInt, end = ' ')
    count += 1
else:
    print()
    print('Sequence is %d number long' % count)
