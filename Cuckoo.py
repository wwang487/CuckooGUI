from ParasiteRand import *
from CuckooEgg import *
class Cuckoo:
    # prob: probability ~ alive egg
    # life: lifetime
    # age: age
    def __init__(self, prob, life, age):
        self.prob = prob
        self.life = life
        self.age = age
    
    def setCuckooAge(self, n):
        self.age = n
        
    def setCuckooLife(self, m):
        self.life = m
    
    def setCuckooHatchProb(self, p1):
        self.prob = p1
    
    def getCuckcooAge(self):
        return self.age
    
    def getCuckooLife(self):
        return self.life
    
    def getCuckooRemYrs(self):
        return self.life - self.age
    
    def getCuckooHatchProb(self):
        return self.prob
    
    def isCuckooDead(self):
        if self.getCuckooRemYrs() > 0:
            return False
        else:
            return True
    
    def growCuckoo(self):
        self.age = self.age + 1
        
    def printCuckoo(self):
        print('==============================   It is a male cuckoo   =====================================\n')
        print('Age of this cuckoo is: %d, Lifetime of this cuckoo is: %d.\n'%(self.age,self.life))

class FemaleCuckoo(Cuckoo):
    # prob_1 : prob of successfully laying eggs
    # dp1: reinforcement factor for laying
    # N: number of eggs
    # is_Preg: if it is Preg
    # dp0: rein factor for cheating ReedsBird
    DP0 = 0
    Egg_list = []
    
    def __init__(self, prob, life, age, prob_1, dp1, dp0, N, is_Preg):
        super(FemaleCuckoo,self).__init__(prob, life, age)
        self.prob_1 = prob_1
        self.PROB_1 = prob_1
        self.dp0 = dp0
        self.dp1 = dp1
        self.N = N
        self.is_Preg = is_Preg
    
    def getCuckooEggNum(self):
        return self.N
    
    def setCuckooEggNum(self, N0):
        self.N = N0
        
    def getCuckooBaseLaidProb(self):
        return self.prob_1
    
    def setCuckooBaseLaidProb(self, p1):
        self.prob_1 = p1
        
    def getCuckooActLaidProb(self):
        return self.PROB_1
    
    def setCuckooActLaidProb(self, p1):
        self.PROB_1 = p1
    
    def getCuckooCheatReinFac(self):
        return self.dp0
    
    def getCuckooLaidReinFac(self):
        return self.dp1
    
    def setCuckooLaidReinFac(self, dp):
        self.dp1 = dp
    
    def setCuckooCheatReinFac(self, dp):
        self.dp0 = dp
    
    def getPregCond(self):
        return self.is_Preg
    
    def setPregCond(self, Preg_Cond):
        self.is_Preg = Preg_Cond
    
    def getTotalCuckooReinFac(self):
        return self.DP0
    
    def setTotalCuckooReinFac(self, P):
        self.DP0 = P
        
    def getFemaleCuckooEggs(self):
        return self.Egg_list
    
    def setFemaleCuckooEggs(self, eggs):
        self.Egg_list = eggs
    
    def apprendOneEgg(self, egg):
        self.Egg_list.append(egg)
        
    def UpdateTotalCuckooReinFac(self):
        self.DP0 = min(self.DP0 + self.dp0, 1)
        
    def UpdateFemaleCuckooLaid(self):
        self.PROB_1 = min(self.PROB_1 + self.dp1, 1)
        
    def printCuckoo(self):
        print('=============================   It is a female cuckoo   ====================================\n')
        print('Age of this cuckoo is: %d, Lifetime of this cuckoo is: %d. \n'%(self.age,self.life))
        print('The maximum number of laying eggs is: %f, current probability for cheating is: %f.\n'%(self.N,self.prob_1))
        if self.getPregCond():
            print('In this turn, it is Pregnant!\n')
        else:
            print('In this turn, it is Not Pregnant!\n')
    
class MaleCuckoo(Cuckoo):
    pass

