import numpy as np
import random


class network:

    def __init__(self, layers, af, cf):
        self.layers = layers
        # todo reduce
        self.activation_f = af[0]
        self.activation_f_d = af[1]
        self.cost_f = cf[0]
        self.cost_f_d = cf[1]

        self.weights = []
        self.biases = []
        for x, y in zip(layers[:len(layers)-1], layers[1:]):
            self.biases.append(np.random.randn(y, 1))
            self.weights.append(np.random.randn(y, x))

    def feedforward(self, a):
        for w, b in zip(self.weights, self.biases):
            a = self.activation_f(np.dot(w, a)+b)
        return a

    def forwardprop(self, a): # feedforward and return midle activationz and midle z
        activations = [a]
        z = []
        for w, b in zip(self.weights, self.biases):
            z.append(np.dot(w, activations[-1])+b)
            activations.append(self.activation_f(z[-1]))
        return activations, z

    def backprop(self, training_example):
        a, z = self.forwardprop(training_example[0])
        deltas = [0 for b in self.biases]
        # calc delta^L
        deltas[-1] = self.cost_f_d(a[-1], training_example[1])*self.activation_f_d(z[-1])
        # calc delta^l
        for i in range(len(deltas)-2, -1, -1):
            deltas[i] = np.dot(self.weights[i+1].transpose(), deltas[i+1])*self.activation_f_d(z[i])
        # if want efficient rm partial bs and ret deltas in its place
        partial_ws, partial_bs = [], []
        for i in range(len(deltas)):
            partial_bs.append(deltas[i])
            partial_ws.append(np.dot(deltas[i], a[i].transpose()))
        return partial_ws, partial_bs

    def update_minbatch(self, minbatch, eta):
        # get gradient
        gradient_w = [np.zeros(w.shape) for w in self.weights]
        gradient_b = [np.zeros(b.shape) for b in self.biases]
        for te in minbatch:
            pw, pb = self.backprop(te)
            for i in range(len(self.weights)):
                gradient_w[i] += pw[i]
                gradient_b[i] += pb[i]
        # apply gradient
        for i in range(len(self.biases)):
            self.weights[i] -= (eta/len(minbatch))*gradient_w[i]
            self.biases[i] -= (eta/len(minbatch))*gradient_b[i]

    def stgd(self, data, epochs, minbatch_size, eta, testing_data, evaluate=False, eval_size=0):
        print("training network {0} for {1} epochs".format(self.layers, epochs))
        for e in range(epochs):
            if evaluate == True:
                cost, corr = self.evaluate(testing_data[0:eval_size])
                print("epoch  {0}, avg cost  {1},  {2}/{3}".format(e, cost, corr, eval_size))
            else:
                print("epoch  {0}".format(e))
            random.shuffle(data)
            k = 0
            for mb in range(int(len(data)/minbatch_size)):
                minbatch = data[k:k+minbatch_size]
                k += minbatch_size
                self.update_minbatch(minbatch, eta)
        print("testing network ", self.layers)
        cost, corr = self.evaluate(testing_data)
        print("avg cost  {0},  {1}/{2}".format(cost, corr, len(testing_data)))


    def evaluate(self, data):
        correct = 0
        cost = 0
        for e in data:
            a = self.feedforward(e[0])
            cost += self.cost_f(a, e[1])
            if np.argmax(a) == np.argmax(e[1]):
                correct += 1
        return cost/len(data), correct

# cost functions
def quadratic_cost_derivetive(a, y):
    return a-y

def quadratic_cost(a, y):
    return np.sum((y-a)**2)/2*len(y)

def cross_entropy(activ, expec_output):
    sum = 0
    for a, y in zip(activ, expec_output):
        sum += (y*np.log(a)) + ((1-y)*np.log(1-a)) 
    return -sum/len(expec_output)

def cross_entropy_derivetive(activ, expec_output):
    output = np.zeros(np.shape(activ))
    for a, y, i in zip(activ, expec_output, range(len(activ))):
        output[i] = ((1-y)/(1-a))-(y/a)
    return output

quadratic_cost_f = [quadratic_cost, quadratic_cost_derivetive]
cross_entropy_f = [cross_entropy, cross_entropy_derivetive]

# activation functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivetive(z):
    return sigmoid(z)*(1-sigmoid(z))


sigmoid_f = [sigmoid, sigmoid_derivetive]
