from Cuckoo import *
from CuckooGroup import *
from ReedsBird import *
from ReedsBirdPair import *
from ReedsBirdGroup import *
import numpy
import random

# Initial Number
N_c = 100
N_r = 2000

# Number of eggs
n_c = 15
n_r = 4

# Lifetime
life_c = 6
life_r = 2

# Simulation period
Y = 30

# Cuckoo alive eggs
prob_c1 = 0.9
# Cuckoo lay the eggs
prob_c2 = 0.6
# Reedsbird alive eggs
prob_r1 = 0.9
# Reedsbird detect the cheating
prob_r2 = 0.5
# Reedsbird breed prob
prob_r3 = 0.43

# lay rein
dp_c1 = 0.01
# cheating rein
dp_c2 = 0.01
# anti-cheating rein from training
dp_r1 = 0.1
# anti-cheating rein from mom
dp_r2 = 0.02
# learning rate for breeding
dp_r3 = 0.02

def CreateInitialCuckoos():
    cuckoogroup = CuckooGroup([],[])
    for i in range(N_c):
        rand_num = numpy.random.uniform(0,1)
        if rand_num < 0.5:
            cuckoogroup.Female_Cuckoo.append(FemaleCuckoo(prob_c1, life_c, 0, prob_c2, dp_c1, dp_c2, n_c, False))
        else:
            cuckoogroup.Male_Cuckoo.append(MaleCuckoo(prob_c1, life_c, 0))
    return cuckoogroup

def CreateInitialReedsBirds():
    reedsbirdgroup = ReedsBirdGroup([], [])
    for i in range(N_r):
        rand_num = numpy.random.uniform(0,1)
        if rand_num < 0.5:
            reedsbirdgroup.Sig_Female_ReedsBird.append(FemaleReedsBird(prob_r1, prob_r3, prob_r2, prob_r2, life_r, 0, dp_r1, dp_r2, dp_r3, n_r))
        else:
            reedsbirdgroup.Sig_Male_ReedsBird.append(MaleReedsBird(prob_r1, prob_r3, prob_r2, prob_r2, life_r, 0, dp_r1, dp_r2, dp_r3))
    reedsbirdgroup.BuildNewReedsBirdPair()
    return reedsbirdgroup

def YearlyGaming(cuckoos, reedsbirds):
    cuckoos.CuckooFirstGaming()
    reedsbirds.ReedsBirdFirstGaming()
    reedsbirds = cuckoos.CuckooSecondGaming(reedsbirds)
    reedsbirds.ReedsBirdSecondGaming()
    babymalecuckoo, babyfemalecuckoo = reedsbirds.getBabyCuckooHatchedbyReedsBird()
    cuckoos.CuckooFinalGaming(babymalecuckoo, babyfemalecuckoo)
    reedsbirds.ReedsBirdFinalGaming()
    return cuckoos, reedsbirds
    
cuckoogroup = CreateInitialCuckoos()
reedsbirdgroup = CreateInitialReedsBirds()
for i in range(Y):
    cuckoogroup, reedsbirdgroup = YearlyGaming(cuckoogroup, reedsbirdgroup)
    print(cuckoogroup.countCuckooProp())
    print(reedsbirdgroup.countReedsBirdProp())

