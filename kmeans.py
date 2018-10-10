import numpy as np
import math
import matplotlib.pyplot as plt
import random
from sys import maxsize

data = []
labels = []
group = []

def kmeans(center):
	change = 0
	for i in range(0, len(data)):
		d = data[i]
		mind = maxsize
		minp = -1
		for j in range(0, len(center)):
			c = center[j]
			s = 0
			for k in range(0, len(d)):
				s += (d[k]-c[k])*(d[k]-c[k])
			dist = math.sqrt(s)
			if dist < mind:
				mind = dist
				minp = j
		if minp != group[i]: change = 1
		group[i] = minp
	print(group)

	# recalculate center
	for i in range(0, len(center)):
		c = 0
		s = [0 for j in range(0, len(center[i]))]
		for j in range(0, len(data)):
			if group[j] != i: continue
			d = data[j]
			for k in range(0, len(d)):
				s[k] += d[k]
			c += 1
		for k in range(0, len(s)): s[k] /= c
		center[i] = s
	print(center)
	return change

with open("dataset/iris/iris.data") as ifile:
	for line in ifile:
		tokens = line.strip().split(',')
		data.append([float(tk) for tk in tokens[:-1]])
		group.append(-1)
		labels.append(tokens[-1])
print(data)
print(labels)

center = [];
for i in range(0, 3):
	index = random.randint(0, len(data)-1)
	while data[index] in center:
		index = random.randint(0, len(data)-1)
	center.append(data[index])
	group[index] = i
print(center)
change = 1
while change:
	change = kmeans(center)

print(labels)
