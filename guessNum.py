#!/usr/bin/env python

'a number guessing game'

import random

'generate a random number'
num = random.randint(0,100)

print('Guess number game:')

timesInt = 0
while True:
    numStr = input('>')
    if not (numStr.isdigit()):
        print('You should enter a number')
        continue
    numInt = int(numStr)
    timesInt += 1
    if numInt < num:
        print('Higher')
    elif numInt > num:
        print('Lower')
    else:
        print('You got it, spent %d times' % timesInt)
        break

