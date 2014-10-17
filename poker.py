#!/usr/bin/env python

import random

Card = '23456789XJQKA' 	#13 card
Rank = 'RBFG' 		#Red, Black, Flower, Grid
Royal = 'pP'		#poker and POKER

CardList = []
CardCnt  = 54

def initCardList():
	for c in Card:
		for r in Rank:
			CardList.append(c+r)
	for c in Royal:
		CardList.append(c)

def test_initCardList():
	initCardList()
	printCard()

def printCard():
	total = len(CardList)
	print('there is %d cards, they are:' % len(CardList))
	for index in range(CardCnt):
		if index % 4 == 0:
			print()
		print(CardList[index], end = ' ')
	print()
	
def washCard():
	CardHeap = []
	for i in range(CardCnt):
		n = random.randint(0, CardCnt - i - 1)
		global CardList
		CardHeap.append(CardList.pop(n))
	CardList = CardHeap

def handCard(n):
	ave = CardCnt // n
	for i in range(n):
		print('Hand[%d]:' % (i+1))
		print(sorted(CardList[i*ave:ave*(i+1)]), end = ' ')
		print()
	if CardCnt % n != 0:
		print('there are %d cards left, they are' % (CardCnt % n))
		print(CardList[ave*n:])

if __name__ == '__main__':
	test_initCardList()
	washCard()
	printCard()
	handCard(4)
