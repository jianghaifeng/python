#!/usr/bin/env python

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
			sum_vc = 0
			sum_v = 0
			for eachDay in dayLst:
				sum_vc += eachDay[1]*eachDay[2]
				sum_v += eachDay[2]
			if sum_v != 0:
				aveprice = sum_vc/sum_v
				monLst.append((his_mon_str, aveprice))
			his_mon_str = cur_mon_str
			dayLst.clear()
			dayLst.append((cur_mon_str,closeprice,volumn))
		else:
			dayLst.append((cur_mon_str,closeprice,volumn))
	else:
		sum_vc = 0
		sum_v = 0
		for eachDay in dayLst:
			sum_vc += eachDay[1]*eachDay[2]
			sum_v += eachDay[2]
		if sum_v != 0:
			aveprice = sum_vc/sum_v
			monLst.append((his_mon_str, aveprice))

	return monLst


def printinfo(MonthlyaveLst):
	MonthlyaveLst.sort(key=lambda x:x[1])
	for eachitem in MonthlyaveLst:
		print(eachitem,end='\n')

if __name__ == '__main__':
	MonLst = getMonthlyave('example.csv')
	printinfo(MonLst)

