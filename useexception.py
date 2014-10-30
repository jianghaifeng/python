#!/usr/bin/env python

def processfile(f):
	if not f.name.endswith('.py'):
		return ''
	while True:
		linestr = f.readline().strip()
		print(linestr)
		if linestr.startswith('#'):
			continue
		elif len(linestr) == 0:
			continue
		elif linestr.startswith("'''") and linestr.endswith("'''"):
			return linestr.strip("'''")
		else:
			return ''


def openfile():
	while True:
		filename = input('Enter file name:')
		try:
			f = open(filename,'r')
		except IOError:
			print('Bad filename, try again')
		else:
			des = processfile(f)
			if len(des) > 0:
				print('the doc desc: ' + des)
			else:
				print('no dese')
		finally:
			try:
				f.close()
			except NameError:
				pass

openfile()	

