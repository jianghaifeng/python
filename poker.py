#!/usr/bin/env python

import random
#class Cards
#method Cards.Deck()
#method Deck.shuffle()
#method Deck.get_suite()
#method Deck.get_rank()
#method Deck.get_value()
#method Deck.deal()
#method Deck.empty()

CardCommon = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
CardJokers = ['o','O']
CardTypes = ['spade','heart','club','diamond']
CardList = []
CardCnt  = 54

def initCardRank():
	pass

def initCardList():
	global CardList
	for a in CardCommon:
		for b in CardTypes:
			CardList.append((a,b))
	for c in CardJokers:
		CardList.append((c,))

def test_initCardList():
	initCardList()
	printCard()

def printCard():
	total = len(CardList)
	print('there are %d cards, they are:' % len(CardList))
	for index in range(CardCnt):
		print(CardList[index], end = ' ')
		if (index+1) % 4 == 0:
			print()
	print()
	
def washCard():
	global CardList
	CardHeap = []
	for i in range(CardCnt):
		n = random.randint(0, CardCnt - i - 1)
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

