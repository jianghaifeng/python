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

def makeUnique_useset(speech):
	wordSet = set(speech)
	return wordSet

def makewordDict(speech):
	wordDict = {}
	for word in speech:
		if word in wordDict:
			wordDict[word] += 1
		else:
			wordDict[word] = 1
	return wordDict

def prettyprint(wordDict):
	wordLst = []
	for eachkey in wordDict:
		wordLst.append((wordDict[eachkey], eachkey))
	wordLst.sort(reverse = True)
	print('%-10s%-10s'%('word','count'))
	print('_'*10)
	for eachitem in wordLst:
		print('%-12s%-3d'%(eachitem[1],eachitem[0]))

f = open('Gettysburg.txt', 'rU')
speech = makeWordList(f)
unique = makeUnique_useset(speech)
wordDict = makewordDict(speech)

print('the lecture has %d words' % len(speech))
#print(sorted(unique))
print('unique length is', len(unique))
#print('wordDict is', wordDict)
prettyprint(wordDict)
