import numpy as np
import math
import operator
from sklearn import neighbors
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

def predict(k):
	ret = []
	for ent in x_test:
		mind = {}
		for i in range(0, len(x_train)):
			ref = x_train[i]
			dist = math.sqrt((ent[0]-ref[0])*(ent[0]-ref[0]) + (ent[1]-ref[1])*(ent[1]-ref[1]) + (ent[2]-ref[2])*(ent[2]-ref[2]) + (ent[3]-ref[3])*(ent[3]-ref[3]))
			mind[dist] = y_train[i]
		mind = sorted(mind.items(), key=operator.itemgetter(0))
		result = {}
		for i in range(0, k):
			if mind[0][1] in result:
				result[mind[0][1]] = result[mind[0][1]] + 1
			else:
				result[mind[0][1]] = 1
		result = sorted(result.items(), key=operator.itemgetter(1))
		ret.append(result[0][0])
	return ret

data = []
labels = []
with open("dataset/iris/iris.data") as ifile:
	for line in ifile:
		tokens = line.strip().split(',')
		data.append([float(tk) for tk in tokens[:-1]])
		labels.append(tokens[-1])
#print(data)
#print(labels)
x = np.array(data)
y = np.array(labels)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
print(x_train)
print(y_train)
print(x_test)
print(y_test)

ans = np.array(predict(10))
print(ans)
print(np.mean(ans == y_test))

'''
clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)

answer = clf.predict(x_test)
#print(x)
print(answer)
print(y_test)
print(np.mean(answer == y_test))
'''
