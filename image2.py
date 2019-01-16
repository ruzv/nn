
class image:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def run(self):
        net = self.n.network([784, 20, 20, 10], self.n.sigmoid_f, self.n.quadratic_cost_f)

        #stgd(data, epochs, minbatch_size, eta, testing_data, evaluate=False)
        net.stgd(self.d.training_data, 20, 20, 3, self.d.testing_data, True, 1000)