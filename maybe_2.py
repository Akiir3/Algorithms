import sys
import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

l=200
filename = sys.argv[1]


randomlySelectedNames=[]
newArr=[]
newArr2=[]

# get 50% random names from input file
with open(filename) as f:
	for line in f:
		newArr.append(line)

for i in newArr:
	i = i.split(" ",1)
	newArr2.append(i[0])

namesSize=len(newArr2)
halfSize=namesSize//2


for i in range(0,halfSize):
	index=random.choice(newArr2)
	randomlySelectedNames.append(index)
	newArr2.remove(index)

#print(randomlySelectedNames)

# fake the hash
hashFake=[]
for name in randomlySelectedNames:
	f=0
	for i in range(0,len(name)):
		f=f + (ord(name[i])-ord('A')+1)
		f=f%l;
	hashFake.append(f)

print(hashFake)

num_bins = 200
n, bins, patches = plt.hist(hashFake, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('hash location')
plt.ylabel('# of times hashed at this location')
plt.show()
