#!/usr/bin/env python

seta = {'a','b','c','d'}
setb = {'c','d','e','f'}

set_intersection = seta.intersection(setb)
set_union = seta.union(setb)
set_difference = seta.difference(setb)
set_symmetric_difference = seta.symmetric_difference(setb)

setsmall = {'a','b'}
setlarge = {'a','b','c','d'}
bool_a = setsmall.issubset(setlarge)
bool_b = setsmall.issuperset(setlarge)
bool_c = setlarge.issubset(setsmall)
bool_d = setlarge.issuperset(setsmall)


print('seta:', seta)
print('setb:', setb)
print('intersection:', set_intersection)
print('union:', set_union)
print('difference:', set_difference)
print('symmetric_difference:', set_symmetric_difference)

print('setlarge:', setlarge)
print('setsmall:', setsmall)
print('small is subset of large:', bool_a)
print('small is superset of lareg:', bool_b)
print('large is subset of small:', bool_c)
print('large is superset of small:', bool_d)
