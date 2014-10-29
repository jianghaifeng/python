#!/usr/bin/env python

import math

class Point(object):
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y
	def distance(self, p):
		xdiff = self.x - p.x
		ydiff = self.y - p.y
		return math.sqrt(xdiff**2 + ydiff**2)
	def sum(self, p):
		xnew = self.x + p.x
		ynew = self.y + p.y
		return Point(xnew, ynew)
	def __str__(self):
		return '(%.2f,%.2f)' % (self.x, self.y)

def test():
	pointa = Point(1,2)
	pointb = Point(3,4)
	print('point a:', pointa)
	print('point b:', pointb)
	print('distance of a and b:', pointa.distance(pointb))
	print('sum of a and b:', pointa.sum(pointb))

test()
