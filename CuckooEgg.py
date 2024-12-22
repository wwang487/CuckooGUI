from ParasiteRand import *
from Cuckoo import *
class CuckooEgg:
    def __init__(self, female_cuckoo, male_cuckoo):
        self.female_cuckoo = female_cuckoo
        self.male_cuckoo = male_cuckoo
        self.cheatingReinFac = female_cuckoo.getCuckooCheatReinFac()
        self.hatching = (female_cuckoo.getCuckooHatchProb() + male_cuckoo.getCuckooHatchProb()) / 2
        self.laying = female_cuckoo.getCuckooBaseLaidProb()
        self.life = (female_cuckoo.getCuckooLife() + male_cuckoo.getCuckooLife()) / 2
        self.dp1 = female_cuckoo.getCuckooLaidReinFac()
        self.dp0 = female_cuckoo.getCuckooCheatReinFac()
        self.N = female_cuckoo.getCuckooEggNum()
        
    def HatchFemaleEgg(self):
        prob = self.hatching
        life = self.life
        age = 0
        prob_1 = self.laying
        dp1 =self.dp1
        dp0 = self.dp0
        N = self.N
        is_Preg = False
        DP0 = self.dp0 + self.cheatingReinFac
        return prob, life, age, prob_1, dp1, dp0, N, is_Preg, DP0
    
    def HatchMaleEgg(self):
        prob = self.hatching
        life = self.life
        age = 0
        return prob, life, age
    
    def getCuckooEggHatchingProb(self):
        return self.hatching
    
    def getCuckooEggCheatingReinFac(self):
        return self.cheatingReinFac
    
    