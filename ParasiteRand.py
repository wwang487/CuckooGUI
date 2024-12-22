#========================================================          Package Area         ====================================================
import numpy
import random
import math
from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt

#========================================================          Function Area         ===================================================

def SatisfyThresh(thresh):
    temp_number = numpy.random.uniform(0,1)
    if temp_number <= thresh:
        return True
    else:
        return False

def IsFemaleBaby(female_thresh):
    return SatisfyThresh(female_thresh)

def IsReallyHatched(hatch_thresh):
    return SatisfyThresh(hatch_thresh)

def IsReallyAlive(breed_thresh):
    return SatisfyThresh(breed_thresh)
        
def IsReallyDetected(detect_thresh):
    return SatisfyThresh(detect_thresh)

def IsReallyLaid(laid_thresh):
    return SatisfyThresh(laid_thresh)

def TribasedAge(peak_age, max_age):
    r1 = numpy.random.uniform(0,1)
    delta_age = max_age - peak_age
    thresh = float(peak_age / max_age)
    if r1 >= thresh:
        out = max_age - delta_age * math.sqrt((1 - r1) / (1 - thresh))
    else:
        out = peak_age * math.sqrt(r1 / thresh)
    return out

def genNormalSampleValue(mean, sigma, x_low, x_high):
    is_found = False
    max_p = getNormalPdf(mean, mean, sigma)
    while not is_found:
        temp_number = numpy.random.uniform(x_low,x_high)
        temp_W = getNormalPdf(temp_number, mean, sigma)
        temp_p = numpy.random.uniform(0, max_p)
        if temp_p < temp_W:
            is_found = True
    return temp_number
    
def genWeibullSampleValue(mean, sigma, x_low, x_high):
    l, k = getWeibullParam(mean, sigma)
    max_p = getMaxWeibull(l, k)
    is_found = False
    while not is_found:
        temp_number = numpy.random.uniform(x_low,x_high)
        temp_W = getWeibullpdf(temp_number, l, k)
        temp_p = numpy.random.uniform(0, max_p)
        if temp_p < temp_W:
            is_found = True
    return temp_number

def getWeibullParam(mean, sigma):
    k = (sigma / mean) ** (-1.806)
    l = mean / (gamma(1 + 1 / k))
    return l, k

def getWeibullpdf(x, l, k):
    if x < 0:
        return 0
    else:
        return (k / l) * (x / l) ** (k - 1) * np.exp(-(x / l) ** k)

def getMaxWeibull(l, k):
    if k <= 1:
        x = 0
    else:
        x = l * ((k - 1) / k) ** (1 / k)
    return x

def getNormalPdf(x, mean, sigma):
    return (1 / (math.sqrt(math.pi) * sigma )) * math.exp((- (x - mean) ** 2) / (2 * sigma ** 2))

def RandomBabyNormalValue(mean, sigma):
    return random.normalvariate(mean, sigma)

# =======================================================      Params Setting Area       ===================================================
#mean = 1
#sigma = 0.8
#x_low = 0
#x_high = 10
#LinN = 100
#N = 1000
    
# ===========================================================         Test        Area     =================================================
#x = numpy.linspace(x_low, x_high, LinN)
#p1 = [0] * LinN
#p2 = [0] * LinN
#l, k = getWeibullParam(mean, sigma)
#for i in range(LinN):
#    p1[i] = getWeibullpdf(x[i], l, k)
#    p2[i] = getNormalPdf(x[i], mean, sigma)
#plt.plot(x, p1)
#plt.plot(x, p2)
