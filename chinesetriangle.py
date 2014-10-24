#!/usr/bin/env python

ct = [[1]]

def Generate(n):
	if n < 2:
		return
	for line in range(2,n+1):
		nlist = []
		for item in range(1, line+1):
			if item==1:
				nlist.append(ct[line-2][0])
			elif item==line:
				nlist.append(ct[line-2][line-2])
			else:
				nlist.append(ct[line-2][item-2]+ct[line-2][item-1])
		ct.append(nlist)

def ShowTriangle():
	layer = len(ct)
	for i in range(layer):
		print(' '*(layer-i), end = '')
		for eachnum in ct[i]:
			print(eachnum, end = ' ')
		print('')


if __name__ == '__main__':
	inp = input('Enter the layer: ')
	Generate(int(inp))
	ShowTriangle()
