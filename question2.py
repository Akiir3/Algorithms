# Using census data of last names produce a histogram of hashed values?
#!/usr/bin/env python
import sys
import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def randomizing(thefile):
	with open(thefile) as file:
		theNames = [line.strip() for line in file]
		file.close()
	random.shuffle(theNames)
	theFifty = len(theNames)/2
	return theNames[:theFifty]

# fake the hash
def fakingtheHash(lastNames, l, numberCollisions):
	modulars =[]
	collisions = []
	theArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for line in lastNames:
		theSum = 0
		theMod = 0
		for char in line:
			for i in range(len(theArray)):
				if (char == theArray[i]):
					theSum = theSum + (i+1)
					break
		theMod = theSum%l
		modulars.append(theMod)
		numberCollisions[theMod] = numberCollisions[theMod] +1
	print (numberCollisions)
	return modulars

useFile = randomizing(sys.argv[1])
names =[]
theHistogram = []
for i in range(0, 200):
	theHistogram.append(0)

answers = fakingtheHash(names, 200, theHistogram)


num_bins = 200
n, bins, patches = plt.hist(fakingtheHash, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('hash location')
plt.ylabel('# of times hashed at this location')
plt.show()
