#!/usr/bin/env python

def makeWordList(f):
	speech = []
	for eachline in f:
		linelist = eachline.split()
		#speech.extend(linelist)
		for eachword in linelist:
			eachword = eachword.lower()
			eachword = eachword.strip('.,')
			if eachword != '--':
				speech.append(eachword)
	return speech

def makeUnique(speech):
	unique = []
	for eachword in speech:
		if eachword not in unique:
			unique.append(eachword)
	return unique

f = open('Gettysburg.txt', 'rU')
speech = makeWordList(f)
unique = makeUnique(speech)

print('the lecture has %d words' % len(speech))
#print(sorted(unique))
print('unique length is', len(unique))
