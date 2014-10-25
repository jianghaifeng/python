#!/usr/bin/env python

def calcAverage(dayLst):
	sum_vc = 0
	sum_v = 0
	for item in dayLst:
		sum_vc += item[1]*item[2]
		sum_v += item[2]
	if sum_v != 0:
		return sum_vc/sum_v
	else:
		return 0

def getMonthlyave(filename):
	fileobj = open(filename, 'r')
	dayLst = []
	monLst = []
	his_mon_str = ''
	for eachline in fileobj:
		Lst = eachline.strip().split(',')
		datestr = Lst[0].strip('"')
		cur_mon_str = datestr[:7]
		closeprice = float(Lst[1].strip('"'))
		volumn = float(Lst[2].strip('"'))
		if cur_mon_str != his_mon_str:
			aveprice = calcAverage(dayLst)
			monLst.append((his_mon_str, aveprice))
			his_mon_str = cur_mon_str
			dayLst.clear()
			dayLst.append((cur_mon_str,closeprice,volumn))
		else:
			dayLst.append((cur_mon_str,closeprice,volumn))
	else:
		aveprice = calcAverage(dayLst)
		monLst.append((his_mon_str, aveprice))
	return monLst


def printinfo(MonthlyaveLst):
	MonthlyaveLst.sort(key=lambda x:x[1])
	for eachitem in MonthlyaveLst:
		print(eachitem,end='\n')

if __name__ == '__main__':
	MonLst = getMonthlyave('example.csv')
	printinfo(MonLst)

