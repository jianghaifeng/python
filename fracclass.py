#!/usr/bin/env python

class Rational(object):
	'''this is a rational number'''
	def __init__(self, a, b=1):
		self.a = a
		self.b = b

	def gcd(self,a,b):
		if not a>b:
			a,b = b,a
		while b!=0:
			reminder = a%b
			a,b = b,reminder
		return a

	def lcm(self,a,b):
		return (a*b)/self.gcd(a,b)

	def __str__(self):
		return str(self.a) + '/' + str(self.b)

	def __add__(self, r):
		if type(r) == int:
			r = Rational(r)
		thelcm = self.lcm(self.b, r.b)
		newa = self.a*thelcm/self.b+r.a*thelcm/r.b
		return Rational(int(newa), int(thelcm))

	def __radd__(self, r):
		return self.__add__(r)

	def __sub__(self, r):
		thelcm = self.lcm(self.b, r.b)
		newa = self.a*thelcm/self.b-r.a*thelcm/r.b
		return Rational(int(newa), int(thelcm))

	def __mul__(self, r):
		return Rational(self.a*r.a, self.b*r.b)

	def __truediv__(self, r):
		return Rational(self.a*r.b, self.b*r.a)

	def __eq__(self, r):
		if __sub__(self, r) == 0:
			return True
		else:
			return False

def test():
	a = Rational(1,2)
	b = Rational(3,2)
	print('a=',a)
	print('b=',b)
	print('a+b=',a+b)
	print('a-b=',a-b)
	print('a*b=',a*b)
	print('a/b=',a/b)

	print('a+1=',a + 1)
	print('1+a=',1 + a)

test()
