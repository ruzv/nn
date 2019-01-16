import numpy as np
from mnist import MNIST


def prep_data(images, labels):
    data = []
    for i, l in zip(images, labels):
        norm_i = []
        for p in i:
            norm_i.append(p/255)
        norm_i = np.array(norm_i).reshape((784, 1))
        data.append([norm_i, int_to_nparray(l)])
    return data

def int_to_nparray(n):
    v = np.zeros((10, 1))
    v[n] = 1
    return v


class data:

    def __init__(self):
        self.f_mn_data = MNIST('data/mn_f')
        self.d_mn_data = MNIST('data/mn_d')

    def load_f_training(self):
        images, labels = self.f_mn_data.load_training()
        self.f_training_data = prep_data(images, labels)

    def load_f_testing(self):
        images, labels = self.f_mn_data.load_testing()
        self.f_testing_data = prep_data(images, labels)

    def load_d_training(self):
        images, labels = self.d_mn_data.load_training()
        self.d_training_data = prep_data(images, labels)

    def load_d_testing(self):
        images, labels = self.d_mn_data.load_testing()
        self.d_testing_data = prep_data(images, labels)
