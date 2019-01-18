import numpy as np



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
