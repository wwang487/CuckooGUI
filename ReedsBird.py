class ReedsBird:
    # is_single: if the ReedsBird is single or not
    # prob    prob of hatching
    # prob_h: prob of successfully breeding.
    # prob_1: prob of detecting cheating
    # prob_0: prob of detecting that can be inherited.
    # dp1: reinforcement from last-year cheating
    # dp2: reinforcement from mom's wisdom
    # dph: Increase of breeding capacity due to previous experience
    def __init__(self, prob, prob_b, prob_1, prob_0, life, age, dp1, dp2, dpb):
        self.prob = prob
        self.prob_b = prob_b
        self.prob_1 = prob_1
        self.prob_0 = prob_0
        self.life = life
        self.age = age
        self.dp1 = dp1
        self.dp2 = dp2
        self.dpb = dpb
        self.total_prob_b = prob_b
    
    def setReedsBirdBreedProb(self, p1):
        self.prob_b = p1
    
    def setReedsBirdBreedReinFac(self, dp):
        self.dpb = dp
    
    def setReedsBirdDectProb(self, p1):
        self.prob_1 = p1
    
    def setReedsBirdAge(self, n):
        self.age = n
        
    def setReedsBirdLife(self, m):
        self.life = m
    
    def setReedsBirdHatchProb(self, p1):
        self.prob = p1
        
    def setReedsBirdBaseDectProb(self, P):
        self.prob_0 = P
    
    def getReedsBirdBreedReinFac(self):
        return self.dpb
    
    def getReedsBirdBreedProb(self):
        return self.prob_b
    
    def getReedsBirdBaseDectProb(self):
        return self.prob_0
    
    def getReedsBirdDectProb(self):
        return self.prob_1
    def getReedsBirdTrainReinFac(self):
        return self.dp1
    
    def getReedsBirdMomReinFac(self):
        return self.dp2
    
    def getReedsBirdAge(self):
        return self.age
    
    def getReedsBirdLife(self):
        return self.life
    
    def getReedsBirdRemYrs(self):
        return self.life - self.age
    
    def getReedsBirdHatchProb(self):
        return self.prob
    
    def getTotalBreedingCap(self):
        return self.total_prob_b
    
    def updateTotalBreedingCap(self):
        self.total_prob_b = self.total_prob_b + self.dpb
    
    def isReedsBirdDead(self):
        if self.getReedsBirdRemYrs() > 0:
            return False
        else:
            return True
    
    def growReedsBird(self):
        self.age = self.age + 1
    
    def UpdateMomReedsBirdDectProb(self):
        self.prob_1 = min(self.prob_1 + self.dp2, 1)
        self.prob_0 = min(self.prob_0 + self.dp2, 1)
    
    def UpdateSecReedsBirdDectProb(self):
        self.prob_1 = min(self.prob_1 + self.dp1, 1)    
   
    def printReedsBird(self):
        print('==============================   It is a male reedsbird   =====================================\n')
        print('Age of this cuckoo is: %d, Lifetime of this cuckoo is: %d.\n'%(self.age,self.life))
        print('Current probability to detect cheating is %f. \n'%self.prob_1)

class FemaleReedsBird(ReedsBird):
    # N: number of eggs
    def __init__(self, prob, prob_h, prob_1, prob_0, life, age, dp1, dp2, dph, N):
        super(FemaleReedsBird,self).__init__(prob, prob_h, prob_1, prob_0, life, age, dp1, dp2, dph)       
        self.N = N
    
    def getReedsBirdEggNum(self):
        return self.N
    
    def setReedsBirdEggNum(self, N0):
        self.N = N0
    
    def printReedsBird(self):
        print('==============================   It is a female reedsbird   =====================================\n')
        print('Age of this cuckoo is: %d, Lifetime of this cuckoo is: %d.\n'%(self.age,self.life))
        print('Current probability to detect cheating is %f. Number of eggs laid is %d. \n'%(self.prob_1,self.N))
   
class MaleReedsBird(ReedsBird):
    pass