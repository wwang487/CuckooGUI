from ReedsBird import *
from CuckooEgg import *
from ParasiteRand import *

class ReedsBirdPair:
    Pair_Base_Prob = 0
    Pair_Detect_Prob = 0
    Pair_Hatch_Prob = 0
    Pair_Life = 0
    Pair_d_Mom = 0
    Pair_d_Sec = 0
    def __init__(self, male_reedsbird, female_reedsbird, is_occupied):
        self.male_reedsbird = male_reedsbird
        self.female_reedsbird = female_reedsbird
        self.is_occupied = is_occupied    
        self.Pair_Hatch_Prob = (male_reedsbird.getReedsBirdHatchProb() + female_reedsbird.getReedsBirdHatchProb()) / 2
        self.Pair_Breed_Prob = (male_reedsbird.getReedsBirdBreedProb() + female_reedsbird.getReedsBirdBreedProb()) / 2
        self.Pair_Base_Prob = (male_reedsbird.getReedsBirdBaseDectProb() + female_reedsbird.getReedsBirdBaseDectProb()) / 2
        self.Pair_Detect_Prob = max(self.male_reedsbird.getReedsBirdDectProb(), self.female_reedsbird.getReedsBirdDectProb())        
        self.Pair_Life = (male_reedsbird.getReedsBirdLife() + female_reedsbird.getReedsBirdLife()) / 2
        self.Pair_d_Mom = (male_reedsbird.getReedsBirdMomReinFac() + female_reedsbird.getReedsBirdMomReinFac()) / 2
        self.Pair_d_Sec = (male_reedsbird.getReedsBirdTrainReinFac() + female_reedsbird.getReedsBirdTrainReinFac()) / 2
        self.Pair_d_Bre = (male_reedsbird.getReedsBirdBreedReinFac() + female_reedsbird.getReedsBirdBreedReinFac()) / 2
    
    def getReedsBirdPairDectProb(self):
        return max(self.male_reedsbird.getReedsBirdDectProb(), self.female_reedsbird.getReedsBirdDectProb())
        
    def getMaleReedsBirdinPair(self):
        return self.male_reedsbird
    
    def getFemaleReedsBirdinPair(self):
        return self.female_reedsbird
    
    def getNestOccupyCond(self):
        return self.is_occupied
    
    def getReedsBirdPairReinDectProb(self):
        return (self.male_reedsbird.getTotalReedsBirdReinFac() + self.female_reedsbird.getTotalReedsBirdReinFac())/2
    
    def getReedsBirdPairTheoBreedCap(self):
        return (self.male_reedsbird.getTotalBreedingCap() + self.female_reedsbird.getTotalBreedingCap()) / 2
    
    def getReedsBirdPairRealBreedCap(self):
        Base = (self.male_reedsbird.getTotalBreedingCap() + self.female_reedsbird.getTotalBreedingCap()) / 2
        return genNormalSampleValue(Base, 0.1, 0, 1)
    
    def setMaleReedsBirdinPair(self, male):
        self.male_reedsbird = male
    
    def setFemaleReedsBirdinPair(self, female):
        self.female_reedsbird = female
    
    def setNestOccupyCond(self, o_status):
        self.is_occupied = o_status
    
    def calReedsBirdPairDectProb(self):
        self.Pair_Detect_Prob = max(self.male_reedsbird.getReedsBirdDectProb(), self.female_reedsbird.getReedsBirdDectProb())
    
    def LearnReedsBirdDectProbFromPair(self):
        P = max(self.male_reedsbird.getReedsBirdDectProb(), self.female_reedsbird.getReedsBirdDectProb())
        self.male_reedsbird.setReedsBirdDectProb(P)
        self.female_reedsbird.setReedsBirdDectProb(P)
        
    def isReedsBirdPairRuined(self):
        if self.female_reedsbird.isReedsBirdDead() or self.male_reedsbird.isReedsBirdDead():
            return True
        else:
            return False
    
    def growReedsBirdinPair(self):
        self.female_reedsbird.growReedsBird()
        self.male_reedsbird.growReedsBird()
        
    def ReedsBridPairBreedLearning(self):
        self.female_reedsbird.updateTotalBreedingCap()
        self.male_reedsbird.updateTotalBreedingCap()

class OccupiedReedsBirdPair(ReedsBirdPair):
    def __init__(self, male_reedsbird, female_reedsbird, is_occupied, cuckooEgg):
        super(OccupiedReedsBirdPair,self).__init__(male_reedsbird, female_reedsbird, is_occupied)  
        self.cuckooEgg = cuckooEgg
    
    def getOccupiedCuckooEgg(self):
        return self.cuckooEgg
    
    def setOccupiedCuckooEgg(self, cuckooEgg):
        self.cuckooEgg = cuckooEgg
        
    def OccupiedCucWinOperation(self):
        female_prob1 = self.female_reedsbird.getReedsBirdDectProb() + self.female_reedsbird.getReedsBirdTrainReinFac()
        self.female_reedsbird.setReedsBirdDectProb(female_prob1)
        male_prob1 = self.male_reedsbird.getReedsBirdDectProb() + self.male_reedsbird.getReedsBirdTrainReinFac()
        self.male_reedsbird.setReedsBirdDectProb(male_prob1)
        self.LearnReedsBirdDectProbFromPair()
        
                
    def OccupiedReeWinOperation(self):
        Baby_Male_ReedsBird = []
        Baby_Female_ReedsBird = []
        Egg_Num = self.getFemaleReedsBirdinPair().getReedsBirdEggNum()
        Actual_Egg_Num = Egg_Num - 1
        Hatch_Prob = self.getFemaleReedsBirdinPair().getReedsBirdHatchProb()
        Breed_Prob = self.getReedsBirdPairRealBreedCap()
        for i in range(Actual_Egg_Num):
            if IsReallyHatched(Hatch_Prob) and IsReallyAlive(Breed_Prob):
                p_1 = self.Pair_Hatch_Prob
                p_2 = self.Pair_Breed_Prob
                p_3 = self.Pair_Base_Prob + self.Pair_d_Mom
                p_4 = p_3
                life = self.Pair_Life
                age = 0
                dp_1 = self.Pair_d_Sec
                dp_2 = self.Pair_d_Mom
                dp_3 = self.Pair_d_Bre
                if IsFemaleBaby(0.5):
                    Baby_Female_ReedsBird.append(FemaleReedsBird(p_1, p_2, p_3, p_4, life, age, dp_1, dp_2, dp_3, Egg_Num))
                else:
                    Baby_Male_ReedsBird.append(MaleReedsBird(p_1, p_2, p_3, p_4, life, age, dp_1, dp_2, dp_3))
        return Baby_Male_ReedsBird, Baby_Female_ReedsBird
        
    def OccupiedCucDeadEggOperation(self):
        Baby_Male_ReedsBird = []
        Baby_Female_ReedsBird = []
        Egg_Num = self.getFemaleReedsBirdinPair().getReedsBirdEggNum()
        Actual_Egg_Num = Egg_Num - 1
        Hatch_Prob = self.getFemaleReedsBirdinPair().getReedsBirdHatchProb()
        Breed_Prob = self.getReedsBirdPairRealBreedCap()
        for i in range(Actual_Egg_Num):
            if IsReallyHatched(Hatch_Prob) and IsReallyAlive(Breed_Prob):
                p_1 = self.Pair_Hatch_Prob
                p_2 = self.Pair_Breed_Prob
                p_3 = self.Pair_Base_Prob + self.Pair_d_Mom
                p_4 = p_3
                life = self.Pair_Life
                age = 0
                dp_1 = self.Pair_d_Sec
                dp_2 = self.Pair_d_Mom
                dp_3 = self.Pair_d_Bre
                if IsFemaleBaby(0.5):
                    Baby_Female_ReedsBird.append(FemaleReedsBird(p_1, p_2, p_3, p_4, life, age, dp_1, dp_2, dp_3, Egg_Num))
                else:
                    Baby_Male_ReedsBird.append(MaleReedsBird(p_1, p_2, p_3, p_4, life, age, dp_1, dp_2, dp_3))
        return Baby_Male_ReedsBird, Baby_Female_ReedsBird
        
        
class NonOccupiedReedsBirdPair(ReedsBirdPair):
    def NonOccupiedOperation(self):
        Baby_Male_ReedsBird = []
        Baby_Female_ReedsBird = []
        Egg_Num = self.getFemaleReedsBirdinPair().getReedsBirdEggNum()
        Hatch_Prob = self.getFemaleReedsBirdinPair().getReedsBirdHatchProb()
        Breed_Prob = self.getReedsBirdPairRealBreedCap()
        for i in range(Egg_Num):
            if IsReallyHatched(Hatch_Prob) and IsReallyAlive(Breed_Prob):
                p_1 = self.Pair_Hatch_Prob
                p_2 = self.Pair_Breed_Prob
                p_3 = self.Pair_Base_Prob + self.Pair_d_Mom
                p_4 = p_3
                life = self.Pair_Life
                age = 0
                dp_1 = self.Pair_d_Sec
                dp_2 = self.Pair_d_Mom
                dp_3 = self.Pair_d_Bre
                if IsFemaleBaby(0.5):
                    Baby_Female_ReedsBird.append(FemaleReedsBird(p_1, p_2, p_3, p_4, life, age, dp_1, dp_2, dp_3, Egg_Num))
                else:
                    Baby_Male_ReedsBird.append(MaleReedsBird(p_1, p_2, p_3, p_4, life, age, dp_1, dp_2, dp_3))
        return Baby_Male_ReedsBird, Baby_Female_ReedsBird
    


   
    
    