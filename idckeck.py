#!/usr/bin/env python

import string

alphas = string.ascii_letters + '_'
nums   = string.digits

print('Welcome to the Identifier Check V1.0')
inp = input('Identifier to test:')

if len(inp) == 1:
    if inp[0] not in string.ascii_letters:
        print('Invalid (symbol must be alphabetic)')
    else:
        print('OK as an identifier')
elif (len(inp)) > 1:
    if (inp[0] not in alphas):
        print('Invalid (first symbol must be alphabetic)')
    else:
        for otherchar in inp[1:]:
            if otherchar not in alphas+nums:
                print('Invalid (symbols must be alphanumeric)')
                break
        else:
            print('OK as an identifier')
