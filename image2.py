
class image:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def run(self):
        net = self.n.network([784, 10, 10], self.n.sigmoid_f, self.n.quadratic_cost_f)

        #stgd(data, epochs, minbatch_size, eta, testing_data, evaluate=False)
        net.stgd(self.d.d_training_data, 5, 20, 100, self.d.d_testing_data, True, 100)