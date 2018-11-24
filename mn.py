import numpy as np
from mnist import MNIST

mndata = MNIST("data")

def int_to_nparray(n):
    v = np.zeros((10, 1))
    v[n] = 1
    return v

def prep_data(images, labels):
    data = []
    for i, l in zip(images, labels):
        norm_i = []
        for p in i:
            norm_i.append(p/255)
        norm_i = np.array(norm_i).reshape((784, 1))
        data.append([norm_i, int_to_nparray(l)])
    return data


images, labels = mndata.load_testing()
testing_data = prep_data(images, labels)

images, labels = mndata.load_training()
training_data = prep_data(images, labels)
