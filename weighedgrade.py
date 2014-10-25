#!/usr/bin/env python

def weightedGrade(gradeLst, weights=(0.3,0.3,0.4)):
	'''Expects 3 elements in gradeLst, Multiples each grade by its weight, returns the sum'''
	result = \
		(gradeLst[0] * weights[0]) + \
		(gradeLst[1] * weights[1]) + \
		(gradeLst[2] * weights[2])
	return result

def grade(fileLine):
	'''Expects a line of form last, first, exam1, exam2, exam3, returns first+last and a final grade'''
	fieldLst = fileLine.split(',')
	name = fieldLst[1]+' '+fieldLst[0]
	grade = []
	for elements in fieldLst[2:]:
		grade.append(int(elements))
	theGrade = weightedGrade(grade)
	return name, theGrade

if __name__ == '__main__':
	filename = 'grades.txt'
	fileobj = open(filename, 'r')
	print('%-15s %-15s' % ('name', 'grade'))
	print('-' * 30)
	for line in fileobj:
		line = line.strip()
		print('%-15s %7.2f' % grade(line))
