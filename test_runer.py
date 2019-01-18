import network as n
import mn_loader as mnl
import formulas as f


d = mnl.data()

def get_data(prams):
    if(prams[0] == 'f'):
        return []
    else(prams[0] == 'd'):
        return 

def get_cost_f(prams):
    if prams[6] == 'entropy':
        return f.cross_entropy_f
    else:
        return f.quadratic_cost_f

def get_layers(prams):
    l = [784]
    if prams[1] != '-':
        l.append(int(prams[0]))
    if prams[2] != '-':
        l.append(int(prams[1]))
    l.append(10)
    return l

def get_actfs(prams):
    actfs = []
    if prams[3] != '-':
        if prams[2] == "some actf":
            pass
        else:
            actfs.append(f.sigmoid_f)
    if prams[3] != '-':
        if prams[3] == "some actf":
            pass
        else:
            actfs.append(f.sigmoid_f)
    if prams[4] != '-':
        if prams[4] == "some actf":
            pass
        else:
            actfs.append(f.sigmoid_f)
    return actfs

test_nets = open("test_net_discrip.txt", 'r')

cost = None
layers = None
actfs = None

for net_discrip in test_nets:
    prams = net_discrip.split(';')

    layers = get_layers(prams)
    actfs = get_actfs(prams)

    print(layers, actfs)




# open file
# read line in witch a net is described
# get net discrip
# run net
# get rezults
# out rezults to a file