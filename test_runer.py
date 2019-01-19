import network as n
import mn_loader as mnl
import formulas as f


class net_pram_seter:

    def __init__(self):
        self.costf = None
        self.actfs = []
        self.layers = []
        self.reg = None

        self.data = []
        self.eta = None
        self.prev_discrip = [None for i in range(8)]

    def get_net_setup_prams(self, discrip):
        discrip = discrip.split(";")

        self.get_layers(discrip)
        self.get_actfs(discrip)
        self.get_costf(discrip)
        self.get_reg(discrip)

        self.prev_discrip = discrip
        return self.layers, self.actfs, self.costf, self.reg

    def get_net_training_prams(self, discrip):

        return self.data, self. eta

    def get_layers(self, discrip):
        if self.prev_discrip[0] != discrip[0] or self.prev_discrip[1] != discrip[1]:
            self.layers = [784]
            self.layers.append(int(discrip[0]))
            if discrip[1] != '-':
                self.layers.append(int(discrip[1]))
            self.layers.append(10)

    def get_actfs(self, discrip):
        if self.prev_discrip[2] != discrip[2] or self.prev_discrip[3] != discrip[3] or self.prev_discrip[4] != discrip[4]:
            self.actfs = []
            if discrip[2] != '-':
                if discrip[2] == "soft":
                    pass
                    # self.actfs.append(f.softmax) # or something like that
                else:
                    self.actfs.append(f.sigmoid_f)
            if discrip[3] != '-': # can do without the first != 
                if discrip[3] == "soft":
                    pass
                    # self.actfs.append(f.softmax) # or something like that
                else:
                    self.actfs.append(f.sigmoid_f)
            if discrip[4] != '-':
                if discrip[4] == "soft":
                    pass
                    # self.actfs.append(f.softmax) # or something like that
                else:
                    self.actfs.append(f.sigmoid_f)

    def get_costf(self, discrip):
        if self.prev_discrip[5] != discrip[5]:
            if discrip[5] == "entropy":
                self.costf = f.cross_entropy_f
            else:
                self.costf = f.quadratic_cost_f

    def get_reg(self, discrip):
        if self.prev_discrip[6] != discrip[6]:
            if discrip[6] == "L2":
                pass # dont have it yet
            elif discrip[6] == "L1":
                pass # dnt have it yet ether
            elif discrip[6] == "DO": # dropout
                pass # nop


nps = net_pram_seter()

test_nets = open("test_net_discrip.txt", 'r')

# net setup
cost = None
layers = None
actfs = None
reg = None

# training setup
data = None
eta = None 

for net_discrip in test_nets:
    
    layers, actfs, costf, reg = nps.get_net_setup_prams(net_discrip)
    data, eta = nps.get_net_training_prams(net_discrip)

    print()
    print(layers)
    print(actfs)
    print(costf)
    print(reg)
    print(data)
    print(eta)
