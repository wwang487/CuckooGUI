from Cuckoo import *
from CuckooEgg import *
import random
import math
from ReedsBirdPair import *
from ReedsBirdGroup import *
from ParasiteRand import *

class CuckooGroup:
    Female_Cuckoo = []
    Male_Cuckoo = []
    mating_coef = 0.95
    def __init__(self, Female_Cuckoo, Male_Cuckoo):
        self.Female_Cuckoo = Female_Cuckoo
        self.Male_Cuckoo = Male_Cuckoo
    
    def getFemaleCuckooNum(self):
        if not self.Female_Cuckoo:
            return 0
        return len(self.Female_Cuckoo)
    
    def getMaleCuckooNum(self):
        if not self.Male_Cuckoo:
            return 0
        return len(self.Male_Cuckoo)
    
    def getTotalCuckooNum(self):
        return self.getFemaleCuckooNum() +self.getMaleCuckooNum()
    
    def setCuckooGroupMatingRate(self, P):
        self.mating_coef = P
        
    def getCuckooGroupMatingRate(self):
        return self.mating_coef
    
    def addFemaleCuckoo(self, female_cuckoo):
        self.Female_Cuckoo.append(female_cuckoo)
    
    def addMaleCuckoo(self, male_cuckoo):
        self.Male_Cuckoo.append(male_cuckoo)
        
    def getPregFemaleCuckooNum(self):
        return math.floor(self.getFemaleCuckooNum() * self.mating_coef)
    
    def getFemaleCuckoo(self):
        return self.Female_Cuckoo
    
    def getMaleCuckoo(self):
        return self.Male_Cuckoo
    
    def markPregFemaleCuckoo(self):
        Preg_Num = self.getPregFemaleCuckooNum()
        random.shuffle(self.Female_Cuckoo)
        for i in range(Preg_Num):
            self.Female_Cuckoo[i].setPregCond(True)
                    
    def resetPregFemaleCuckoo(self):
        Female_Num = self.getFemaleCuckooNum()
        for i in range(Female_Num):
            self.Female_Cuckoo[i].setPregCond(False)
    
    def addOneAge2Cuckoo(self):
        Female_Num = self.getFemaleCuckooNum()
        Male_Num = self.getMaleCuckooNum()
        for i in range(Female_Num):
            self.Female_Cuckoo[i].growCuckoo()
        for i in range(Male_Num):
            self.Male_Cuckoo[i].growCuckoo()
    
    def RemoveDeadCuckoo(self):
        Female_Num = self.getFemaleCuckooNum()
        Male_Num = self.getMaleCuckooNum()
        f0 = Female_Num - 1
        m0 = Male_Num - 1
        while f0 >= 0:
            if self.Female_Cuckoo[f0].isCuckooDead():
                self.Female_Cuckoo.pop(f0)
            f0 = f0 - 1        
        while m0 >= 0:
            if self.Male_Cuckoo[m0].isCuckooDead():
                self.Male_Cuckoo.pop(m0)
            m0 = m0 - 1
            
    def getBabyMaleCuckooPopulation(self):
        count = 0
        Male_Num = self.getMaleCuckooNum()
        for i in range(Male_Num):
            if self.Male_Cuckoo[i].getCuckcooAge() == 0:
                count = count + 1
        return count
    
    def getBabyFemaleCuckooPopulation(self):
        count = 0
        Female_Num = self.getFemaleCuckooNum()
        for i in range(Female_Num):
            if self.Female_Cuckoo[i].getCuckcooAge() == 0:
                count = count + 1
        return count
    
    def CuckooFirstGaming(self):
        self.markPregFemaleCuckoo()
        Female_Num = self.getFemaleCuckooNum()
        Male_Num = self.getMaleCuckooNum()
        if Male_Num == 0:
            self.addOneAge2Cuckoo()
            return
        for i in range(Female_Num):
            if self.Female_Cuckoo[i].getPregCond():
                male_ind = random.randint(0, Male_Num - 1)
                self.Female_Cuckoo[i].apprendOneEgg(CuckooEgg(self.Female_Cuckoo[i],self.Male_Cuckoo[male_ind]))
        self.addOneAge2Cuckoo()
    
    def CuckooSecondGaming(self, reedsbirds):
        Female_Num = self.getFemaleCuckooNum()
        for i in range(Female_Num):
            temp_cuckoo = self.Female_Cuckoo[i]
            if temp_cuckoo.getPregCond():
                Laid_atleast_One = False
                Remain_Nest_Num = reedsbirds.getNonOccupiedReedsBirdPairNum()
                Cuckoo_Eggs = temp_cuckoo.getFemaleCuckooEggs()
                for j in Cuckoo_Eggs:
                    if Remain_Nest_Num == 0:
                        break
                    LaidProb = temp_cuckoo.getCuckooActLaidProb()
                    if IsReallyLaid(LaidProb):
                        Laid_atleast_One = True
                        ind = random.randrange(Remain_Nest_Num)
                        reedsbirds.updateNonOccupiedReedsBirdPairs(ind, j)
                        Remain_Nest_Num = Remain_Nest_Num - 1
                if Laid_atleast_One:
                    self.Female_Cuckoo[i].UpdateFemaleCuckooLaid()
        return reedsbirds
    
    def CuckooFinalGaming(self, baby_male, baby_female):
        Baby_Male_Num = 0 if not baby_male else len(baby_male)
        Baby_Female_Num = 0 if not baby_female else len(baby_female)
        for i in range(Baby_Male_Num):
            self.Male_Cuckoo.append(baby_male[i])
        for i in range(Baby_Female_Num):
            self.Female_Cuckoo.append(baby_female[i])
        self.RemoveDeadCuckoo()
        self.resetPregFemaleCuckoo()
    
    def countCuckooProp(self):
        Female_Num = self.getFemaleCuckooNum()
        Male_Num = self.getMaleCuckooNum()
        Total_Num = self.getTotalCuckooNum()
        New_Female_Num = self.getBabyFemaleCuckooPopulation()
        New_Male_Num = self.getBabyMaleCuckooPopulation()
        res = [Female_Num, Male_Num, Total_Num, New_Female_Num, New_Male_Num]
        return res