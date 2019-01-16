import network as n
import mn_d as d

net = n.network([784, 10, 10], n.sigmoid_f, n.cross_entropy_f)

#stg(data, epochs, minbatch_size, eta, testing_data, evaluate=False)
net.stgd(d.training_data, 10, 10, 0.5, d.testing_data, True, 1000)