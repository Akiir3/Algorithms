import sys
import os
import math
	
#definition of the array, list  and l we are going to use 
theArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l = 200
fileInput = sys.argv[1]
theList = list()
if not os.path.isfile(fileInput):
	print("File path {} does not exist. Exiting...".format(fileInput))
	sys.exit()
	
with open(fileInput) as f:
	for line in f:
		for ch in line:
			i =0 
			if ch != theArray[i]:
				i = i+1
			elif ch== theArray[i]:
				theSum = 0
				theMod = 0
				theSum = theSum + (i+1)
				theMod = theMod % l
				theList.append(theMod)	
	print(theList)
