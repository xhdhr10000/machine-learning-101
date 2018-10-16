from struct import unpack
import numpy as np
from PIL import Image

def readDataset(filename):
	print("Reading %s" % filename)
	f = open(filename, "rb")
	magic, = unpack(">L", f.read(4))
	count, = unpack(">L", f.read(4))
	dtype = "images" if magic == 2051 else "labels"
	print("  Magic number: %d, %d %s!" % (magic, count, dtype))

	if dtype == "images":
		data = []
		width, = unpack(">L", f.read(4))
		height, = unpack(">L", f.read(4))
		print("  Image size: [%d, %d]" % (width, height))
		for i in range(0, count):
			print("  Reading image: %d / %d" % (i+1, count), end="\r")
			array = [unpack("B", f.read(1))[0] for j in range(0, width*height)]
			array = np.byte([array[j::28] for j in range(0, 28)])
			data.append(array)
		print("")
	elif dtype == "labels":
		data = [unpack("B", f.read(1))[0] for i in range(0, count)]
		#print("  The first 10 labels are:")
		#for i in range(0, 10): print("    %d" % data[i])

	f.close()
	print("")
	return (data, count)

def main():
	readDataset("dataset/mnist/train-images-idx3-ubyte")
	readDataset("dataset/mnist/train-labels-idx1-ubyte")
	readDataset("dataset/mnist/t10k-images-idx3-ubyte")
	readDataset("dataset/mnist/t10k-labels-idx1-ubyte")
	pass

if __name__ == "__main__":
	main()
