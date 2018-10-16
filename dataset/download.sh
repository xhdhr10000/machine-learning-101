#!/bin/bash

echo "Downloading mnist dataset"
mkdir -p mnist && cd mnist
curl --remote-name-all -O http://yann.lecun.com/exdb/mnist/{train-images-idx3-ubyte.gz,train-labels-idx1-ubyte.gz,t10k-images-idx3-ubyte.gz,t10k-labels-idx1-ubyte.gz}
echo "Uncompressing mnist dataset"
gzip -d train-images-idx3-ubyte.gz train-labels-idx1-ubyte.gz t10k-images-idx3-ubyte.gz t10k-labels-idx1-ubyte.gz
cd ..

echo "Downloading iris dataset"
mkdir -p iris && cd iris
curl --remote-name-all -O https://archive.ics.uci.edu/ml/machine-learning-databases/iris/{bezdekIris.data,iris.data,iris.names}
cd ..
