
class image:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def run(self):
        net = self.n.network([784, 10, 10], self.n.sigmoid_f, self.n.cross_entropy_f)

        #stgd(data, epochs, minbatch_size, eta, testing_data, evaluate=False)
        net.stgd(self.d.training_data, 20, 20, 0.05, self.d.testing_data, True, 1000)