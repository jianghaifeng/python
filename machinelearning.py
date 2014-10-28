#!/usr/bin/env python

'''data from archive.ics.uci.edu/ml'''

benignLst = []
malignantLst = []

benignNum = 0
malignantNum = 0

def initlists():
	for i in range(9):
		benignLst.append(0)
		malignantLst.append(0)

def newdata(datalist):
	global benignNum
	global malignantNum
	for i in range(9):
		if datalist[i].isdigit():
			if datalist[9] == '2':
				benignLst[i] = (benignLst[i]*benignNum + int(datalist[i])) / (benignNum + 1)
				benignNum += 1
			elif datalist[9] == '4':
				malignantLst[i] = (malignantLst[i]*malignantNum + int(datalist[i])) / (malignantNum + 1)
				malignantNum += 1

def traindata(filename):
	initlists()
	f = open(filename, 'r') #'breast-cancer-wisconsin-data.txt'
	for l in f:
		lineLst = l.strip().split(',')
		print('processing',lineLst.pop(0))
		newdata(lineLst)
	print('the benignLst')
	print(benignLst)
	print('the malignantLst')
	print(malignantLst)
	f.close()

def testdata(filename):
	midLst = []
	right = 0
	wrong = 0
	for i in range(9):
		midLst.append((benignLst[i] + malignantLst[i])/2)
	print('midLst',midLst)
		
	f = open(filename, 'r') #'breast-cancer-wisconsin-data.txt'
	for l in f:
		lineLst = l.strip().split(',')
		lineLst.pop(0)
		b = 0
		m = 0
		for i in range(9):
			if lineLst[i].isdigit():
				if (benignLst[i]-midLst[i])*(int(lineLst[i])-midLst[i]) > 0:
					b += 1
				else:
					m += 1
		if m >= b and lineLst[9] == '4':
			right += 1
		elif m <= b and lineLst[9] == '2':
			right += 1
		else:
			wrong += 1

	print('rate:', right/(right+wrong))
	f.close()

traindata('breast-cancer-wisconsin-data.txt')
testdata('breast-cancer-wisconsin-data.txt')


