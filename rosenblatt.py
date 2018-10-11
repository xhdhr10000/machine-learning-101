import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

datasize = 1000
datamax = 10000
manual = False
speed = 0.1

def main():
	# Env setup
	matplotlib.interactive(True)

	# Generate data
	data = np.random.randint(-datamax, datamax, size=(datasize, 2))

	# Plot
	plt.plot(data[:,0], data[:,1], "r.")

	# Generate divider
	y = np.array([np.random.randn() * datamax for i in range(3)])
	print("%.2f x0 + %.2f x1 + %.2f = 0" % (y[0], y[1], y[2]))

	# Plot
	(x0, y0, x1, y1) = lineToPoints(y)
	print(x0, y0, x1, y1)
	plt.plot((x0, x1), (y0, y1), "g")

	# Divide points
	positive = np.array([d for d in data if d[0]*y[0]+d[1]*y[1]+y[2]>0])
	plt.plot(positive[:,0], positive[:,1], "b.")

	w = np.array([0.0, 0.0, 0.0])
	step = 0
	line = [None, None]
	while True:
		print("Step: %d, %.2f x0 + %.2f x1 + %.2f = 0" % (step, w[0], w[1], w[2]))
		(x0, y0, x1, y1) = lineToPoints(w)
		if line[1]: line[1].remove()
		if line[0]: line[0].set_alpha(0.5)
		line[1] = line[0]
		[line[0]] = plt.plot((x0, x1), (y0, y1), "c")

		if manual: input()
		else: plt.pause(0.00000000001)
		train(data, w, step, y)
		step += 1

def lineToPoints(w):
	# w[0]*x[0] + w[1]*x[1] + w[2] = 0
	if w[0] == 0 or w[1] == 0: return (0, 0, 0, 0)
	x = (datamax * w[0] - w[2]) / w[1]
	if abs(x) < datamax:
		(x0, y0) = (-datamax, x)
	else:
		(x0, y0) = ((datamax*w[1] - w[2]) / w[0], -datamax)
	x = (-datamax * w[0] - w[2]) / w[1]
	if abs(x) < datamax:
		(x1, y1) = (datamax, x)
	else:
		(x1, y1) = ((-datamax*w[1] - w[2]) / w[0], datamax)
	return (x0, y0, x1, y1)

def inArray(x, positive):
	for p in positive:
		if np.array_equal(x, p): return True
	return False

def train(data, w, step, label):
	index = np.random.randint(len(data))
	x = data[index]
	isPositive = x[0]*label[0] + x[1]*label[1] + label[2] > 0
	plt.plot(x[0], x[1], "k*")
	if w[0]*x[0]+w[1]*x[1]+w[2] <= 0 and isPositive:
		print("Using data [%.2f, %.2f] %s" % (x[0], x[1], "positive" if isPositive else "negetive"))
		w[0] += speed * x[0]
		w[1] += speed * x[1]
		w[2] += speed
	elif w[0]*x[0]+w[1]*x[1]+w[2] > 0 and not isPositive:
		print("Using data [%.2f, %.2f] %s" % (x[0], x[1], "positive" if isPositive else "negetive"))
		w[0] -= speed * x[0]
		w[1] -= speed * x[1]
		w[2] -= speed

if __name__ == "__main__":
	main()