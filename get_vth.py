# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal, interpolate
from matplotlib import pylab as plt

def get_candidateVthLine(list_t, list_y):
    """ get y = at + b by y and t """
    list_ab = []
    for num, (t2, y2) in enumerate(zip(list_t, list_y)): 
        if num == 0:
            t1 = t2
            y1 = y2
        else:
            a = (y2-y1)/(t2-t1)
            b = y1 - a * t1
            list_ab.append([a,b])
            t1 = t2
            y1 = y2
    return list_ab

def validate_VthLine(a, b):
    """validate Vth check"""
    if a <= 0:
        valide_Vth = False
    else:
        valide_Vth = True

    return valide_Vth


def get_Vth(list_t, list_y):
    """get Vth"""
    candidate_Vth = []
    list_ab = get_candidateVthLine(list_t, list_y)
    for a, b in list_ab:
        valide = validate_VthLine(a, b)
        if valide == True:
            Vth = - b/a
            candidate_Vth.append(Vth)
        
    print("candidate Vth is : ", candidate_Vth)
    print("max Vth = ", max(candidate_Vth))
    return max(candidate_Vth)



if __name__ == '__main__':
    t = np.linspace(0, 10, 11)
    y = np.exp(t)

    list_ab = (get_candidateVthLine(t, y))
    Vth = (get_Vth(t, y))
    print(Vth)

    y1 = list_ab[0][0] * t + list_ab[0][1]
    y2 = list_ab[1][0] * t + list_ab[1][1]
    y3 = list_ab[2][0] * t + list_ab[2][1]
    y7 = list_ab[7][0] * t + list_ab[7][1]
    y8 = list_ab[8][0] * t + list_ab[8][1]
    y9 = list_ab[9][0] * t + list_ab[9][1]

    plt.figure(figsize=(12, 9))
    plt.plot(t, y, "-o")
    plt.plot(t, y1, "-x")
    plt.plot(t, y7, "-x")
    plt.plot(t, y8, "-x")
    plt.plot(t, y9, "-x")
    plt.show()
