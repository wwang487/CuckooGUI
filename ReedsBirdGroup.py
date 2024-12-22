from ReedsBird import *
from ReedsBirdPair import *
from Cuckoo import *
from CuckooEgg import *
import random
import numpy
from ParasiteRand import *

class ReedsBirdGroup:
    Non_occupied_pairs = []
    Occupied_pairs = []
    Sig_Male_ReedsBird = []
    Sig_Female_ReedsBird = []
    
    baby_male_Cuckoo = []
    baby_female_Cuckoo = []
    
    PROB = 0.75
    PROB_1 = 0.7
    Life = 2
    dp_g1 = 0.05
    dp_g2 = 0.01
    
    def __init__(self, Sig_Male_ReedsBird, Sig_Female_ReedsBird):
        self.Sig_Male_ReedsBird = Sig_Male_ReedsBird
        self.Sig_Female_ReedsBird = Sig_Female_ReedsBird
        
    def getSigMaleReedsBirdNum(self):
        if not self.Sig_Male_ReedsBird:
            return 0
        else:
            return len(self.Sig_Male_ReedsBird)
    
    def getSigFemaleReedsBirdNum(self):
        if not self.Sig_Female_ReedsBird:
            return 0
        else:
            return len(self.Sig_Female_ReedsBird)
    
    def getReedsBirdGroupDetectProb(self):
        return self.PROB_1
    
    def setReedsBirdGroupDetectProb(self, P):
        self.PROB_1 = P
    
    def getReedsBirdPairNum(self):
        return self.getNonOccupiedReedsBirdPairNum() + self.getOccupiedReedsBirdPairNum()
    
    def getTotalMaleReedsBirdNum(self):
        return self.getSigMaleReedsBirdNum() + self.getNonOccupiedReedsBirdPairNum() + self.getOccupiedReedsBirdPairNum()
    
    def getTotalFemaleReedsBirdNum(self):
        return self.getSigFemaleReedsBirdNum() + self.getNonOccupiedReedsBirdPairNum() + self.getOccupiedReedsBirdPairNum()
    
    def getTotalReedsBirdNum(self):
        return self.getTotalMaleReedsBirdNum() + self.getTotalFemaleReedsBirdNum()
    
    def getSigFemaleReedsBird(self):
        return self.Sig_Female_ReedsBird
    
    def getSigMaleReedsBird(self):
        return self.Sig_male_ReedsBird
    
    def getReedsBirdPairs(self):
        return self.ReedsBirdPairs
    
    def AddSigMaleReedsBird(self, male):
        self.Sig_Male_ReedsBird.append(male)
    
    def AddSigFemaleReedsBird(self, female):
        self.Sig_Female_ReedsBird.append(female)
        
    def AddReedsBirdPair(self, pair):
        self.ReedsBirdPairs.append(pair)
    
    def addOneAge2ReedsBird(self):
        Sig_Male_Num = self.getSigMaleReedsBirdNum()
        Sig_Female_Num = self.getSigFemaleReedsBirdNum()
        Occupied_Num = self.getOccupiedReedsBirdPairNum()
        Non_Occupied_Num = self.getNonOccupiedReedsBirdPairNum()
        for i in range(Sig_Female_Num):
            self.Sig_Female_ReedsBird[i].growReedsBird()
        for i in range(Sig_Male_Num):
            self.Sig_Male_ReedsBird[i].growReedsBird()
        for i in range(Occupied_Num):
            self.Occupied_pairs[i].growReedsBirdinPair()
        for i in range(Non_Occupied_Num):
            self.Non_occupied_pairs[i].growReedsBirdinPair()
    
    def RemoveDeadReedsBird(self):
        Sig_Male_Num = self.getSigMaleReedsBirdNum()
        Sig_Female_Num = self.getSigFemaleReedsBirdNum()
        Occupied_Num = self.getOccupiedReedsBirdPairNum()
        Non_Occupied_Num = self.getNonOccupiedReedsBirdPairNum()
        o0 = Occupied_Num - 1
        n0 = Non_Occupied_Num - 1
        m0 = Sig_Male_Num - 1
        f0 = Sig_Female_Num - 1
        while o0 >= 0:
            if self.Occupied_pairs[o0].getFemaleReedsBirdinPair().isReedsBirdDead() \
            and self.Occupied_pairs[o0].getMaleReedsBirdinPair().isReedsBirdDead():
                self.Occupied_pairs.pop(o0)
            elif self.Occupied_pairs[o0].getFemaleReedsBirdinPair().isReedsBirdDead():
                self.Sig_Male_ReedsBird.append(self.Occupied_pairs[o0].getMaleReedsBirdinPair())
                self.Occupied_pairs.pop(o0)
            elif self.Occupied_pairs[o0].getMaleReedsBirdinPair().isReedsBirdDead():
                self.Sig_Female_ReedsBird.append(self.Occupied_pairs[o0].getFemaleReedsBirdinPair())
                self.Occupied_pairs.pop(o0)
            o0 = o0 - 1
        
        while n0 >= 0:
            if self.Non_occupied_pairs[n0].getFemaleReedsBirdinPair().isReedsBirdDead() \
            and self.Non_occupied_pairs[n0].getMaleReedsBirdinPair().isReedsBirdDead():
                self.Non_occupied_pairs.pop(n0)
            elif self.Non_occupied_pairs[n0].getFemaleReedsBirdinPair().isReedsBirdDead():
                self.Sig_Male_ReedsBird.append(self.Non_occupied_pairs[n0].getMaleReedsBirdinPair())
                self.Non_occupied_pairs.pop(n0)
            elif self.Non_occupied_pairs[n0].getMaleReedsBirdinPair().isReedsBirdDead():
                self.Sig_Female_ReedsBird.append(self.Non_occupied_pairs[n0].getFemaleReedsBirdinPair())
                self.Non_occupied_pairs.pop(n0)
            n0 = n0 - 1
        
        while f0 >= 0:
            if self.Sig_Female_ReedsBird[f0].isReedsBirdDead():
                self.Sig_Female_ReedsBird.pop(f0)
            f0 = f0 - 1    
        while m0 >= 0:
            if self.Sig_Male_ReedsBird[m0].isReedsBirdDead():
                self.Sig_Male_ReedsBird.pop(m0)
            m0 = m0 - 1
    
    def BuildNewReedsBirdPair(self):
        to_Pair_Num = min(self.getSigFemaleReedsBirdNum(), self.getSigMaleReedsBirdNum())
        random.shuffle(self.Sig_Male_ReedsBird)
        random.shuffle(self.Sig_Female_ReedsBird)
        for i in range(to_Pair_Num):
            temp_NonOccupiedPair = NonOccupiedReedsBirdPair(self.Sig_Male_ReedsBird.pop(0), self.Sig_Female_ReedsBird.pop(0), False)
            temp_NonOccupiedPair.calReedsBirdPairDectProb()
            self.Non_occupied_pairs.append(temp_NonOccupiedPair)
    
    def clearOccupiedReedsBirdPair(self):
        while self.Occupied_pairs:
            male_reedsbird = self.Occupied_pairs[0].getMaleReedsBirdinPair()
            female_reedsbird = self.Occupied_pairs[0].getFemaleReedsBirdinPair()
            temp_NonOccupiedPair = NonOccupiedReedsBirdPair(male_reedsbird, female_reedsbird, False)
            temp_NonOccupiedPair.calReedsBirdPairDectProb()
            self.Occupied_pairs.pop(0)
            self.Non_occupied_pairs.append(temp_NonOccupiedPair)
            
    def getNonOccupiedReedsBirdPairNum(self):
        if not self.Non_occupied_pairs:
            return 0
        else:
            return len(self.Non_occupied_pairs)
    
    def getOccupiedReedsBirdPairNum(self):
        if not self.Occupied_pairs:
            return 0
        else:
            return len(self.Occupied_pairs)
        
    def updateNonOccupiedReedsBirdPairs(self, ind, cuckooEgg):
        male_reedsbird = self.Non_occupied_pairs[ind].getMaleReedsBirdinPair()
        female_reedsbird = self.Non_occupied_pairs[ind].getFemaleReedsBirdinPair()
        temp_OccupiedPair = OccupiedReedsBirdPair(male_reedsbird, female_reedsbird, False, cuckooEgg)
        temp_OccupiedPair.calReedsBirdPairDectProb()        
        self.Non_occupied_pairs.pop(ind)
        self.Occupied_pairs.append(temp_OccupiedPair)

    def getBabyMaleReedsBirdPopulation(self):
        count = 0
        Male_Num = self.getSigMaleReedsBirdNum()
        Non_Occupied_Num = self.getNonOccupiedReedsBirdPairNum()
        Occupied_Num = self.getOccupiedReedsBirdPairNum()
        for i in range(Male_Num):
            if self.Sig_Male_ReedsBird[i].getReedsBirdAge() == 0:
                count = count + 1
        for i in range(Non_Occupied_Num):
            if self.Non_occupied_pairs[i].male_reedsbird.getReedsBirdAge() == 0:
                count = count + 1
        for i in range(Occupied_Num):
            if self.Occupied_pairs[i].male_reedsbird.getReedsBirdAge() == 0:
                count = count + 1
        return count
    
    def getBabyFemaleReedsBirdPopulation(self):
        count = 0
        Female_Num = self.getSigFemaleReedsBirdNum()
        Non_Occupied_Num = self.getNonOccupiedReedsBirdPairNum()
        Occupied_Num = self.getOccupiedReedsBirdPairNum()
        for i in range(Female_Num):
            if self.Sig_Female_ReedsBird[i].getReedsBirdAge() == 0:
                count = count + 1
        for i in range(Non_Occupied_Num):
            if self.Non_occupied_pairs[i].female_reedsbird.getReedsBirdAge() == 0:
                count = count + 1
        for i in range(Occupied_Num):
            if self.Occupied_pairs[i].female_reedsbird.getReedsBirdAge() == 0:
                count = count + 1
        return count
    
    def getBabyCuckooHatchedbyReedsBird(self):
        return self.baby_male_Cuckoo,self.baby_female_Cuckoo
    
    def ResetBabyCuckooHatchedbyReedsBird(self):
        self.baby_female_Cuckoo = []
        self.baby_male_Cuckoo = []
    
    def ReedsBirdFirstGaming(self):
        OccReedsBirdPairNum = self.getOccupiedReedsBirdPairNum()
        NonReedsBirdPairNum = self.getNonOccupiedReedsBirdPairNum()
    #    SigFemaleReedsBirdNum = reedsbirdgroup.getSigFemaleReedsBirdNum()
    #    SigMaleReedsBirdNum = reedsbirdgroup.getSigFemaleReedsBirdNum()
        for i in range(OccReedsBirdPairNum):
            self.Occupied_pairs[i].calReedsBirdPairDectProb()
            self.Occupied_pairs[i].LearnReedsBirdDectProbFromPair()
        for i in range(NonReedsBirdPairNum):
            self.Non_occupied_pairs[i].calReedsBirdPairDectProb()
            self.Non_occupied_pairs[i].LearnReedsBirdDectProbFromPair()
        self.addOneAge2ReedsBird()
        
    def ReedsBirdSecondGaming(self):
        OccReedsBirdPairNum = self.getOccupiedReedsBirdPairNum()
        NonReedsBirdPairNum = self.getNonOccupiedReedsBirdPairNum()
        # if not occupied
        for i in range(NonReedsBirdPairNum):
            Baby_male, Baby_female = self.Non_occupied_pairs[i].NonOccupiedOperation()
            Baby_male_num = len(Baby_male) if Baby_male else 0
            Baby_female_num = len(Baby_female) if Baby_female else 0
            for j in range(Baby_male_num):
                self.AddSigMaleReedsBird(Baby_male[j])
            for j in range(Baby_female_num):
                self.AddSigFemaleReedsBird(Baby_female[j])
            self.Non_occupied_pairs[i].ReedsBridPairBreedLearning()
        # if occupied
        for i in range(OccReedsBirdPairNum):
            Dect_prob = self.Occupied_pairs[i].getReedsBirdPairDectProb() - self.Occupied_pairs[i].getOccupiedCuckooEgg().getCuckooEggCheatingReinFac()
            Cuckoo_Hatch_prob = self.Occupied_pairs[i].getOccupiedCuckooEgg().getCuckooEggHatchingProb()
            if IsReallyDetected(Dect_prob):
                Baby_male, Baby_female = self.Occupied_pairs[i].OccupiedReeWinOperation()
                Baby_male_num = len(Baby_male) if Baby_male else 0
                Baby_female_num = len(Baby_female) if Baby_female else 0
                for j in range(Baby_male_num):
                    self.AddSigMaleReedsBird(Baby_male[j])
                for j in range(Baby_female_num):
                    self.AddSigFemaleReedsBird(Baby_female[j])
            else:
                if IsReallyHatched(Cuckoo_Hatch_prob):
                    Breed_Prob = self.Occupied_pairs[i].getReedsBirdPairRealBreedCap()
                    if IsReallyAlive(Breed_Prob):
                        self.Occupied_pairs[i].OccupiedCucWinOperation()
                        cuckooEgg = self.Occupied_pairs[i].getOccupiedCuckooEgg()
                        if IsFemaleBaby(0.5):
                            prob, life, age, prob_1, dp1, dp0, N, is_Preg, DP = cuckooEgg.HatchFemaleEgg()
                            baby_female_cuckoo = FemaleCuckoo(prob, life, age, prob_1, dp1, dp0, N, is_Preg)
                            baby_female_cuckoo.setTotalCuckooReinFac(DP)
                            self.baby_female_Cuckoo.append(baby_female_cuckoo)
                        else:
                            prob, life, age = cuckooEgg.HatchMaleEgg()
                            self.baby_male_Cuckoo.append(MaleCuckoo(prob, life, age))
                else:
                    Baby_male, Baby_female = self.Occupied_pairs[i].OccupiedCucDeadEggOperation()
                    Baby_male_num = len(Baby_male) if Baby_male else 0
                    Baby_female_num = len(Baby_female) if Baby_female else 0
                    for j in range(Baby_male_num):
                        self.AddSigMaleReedsBird(Baby_male[j])
                    for j in range(Baby_female_num):
                        self.AddSigFemaleReedsBird(Baby_female[j])
            self.Occupied_pairs[i].ReedsBridPairBreedLearning()
                
             
    def ReedsBirdFinalGaming(self):
        self.RemoveDeadReedsBird()
        self.clearOccupiedReedsBirdPair()
        self.ResetBabyCuckooHatchedbyReedsBird()
        self.BuildNewReedsBirdPair()
    
    def countReedsBirdProp(self):
        Female_Num = self.getTotalFemaleReedsBirdNum()
        Male_Num = self.getTotalMaleReedsBirdNum()
        Total_Num = self.getTotalReedsBirdNum()
        New_Female_Num = self.getBabyFemaleReedsBirdPopulation()
        New_Male_Num = self.getBabyMaleReedsBirdPopulation()
        res = [Female_Num, Male_Num, Total_Num, New_Female_Num, New_Male_Num]
        return res