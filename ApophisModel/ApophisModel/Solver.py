"""
Landon Buell
Mark Lyon
MATH 753.01 - HW10
13 November 2020
"""

            #### IMPORTS ####

import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

            #### CLASS DEFINITIONS ####

class DormandPrinceSolver :
    """
    Dormand Prince Solver for Systems of ODEs
    """

    def __init__(self):
        """ Initialize DormandPrinceSolver Instance """

        
    @property
    def ConstantsMatrix():
        """ Define Matrix of Constants for Solver """
        c2 = np.array([0.2,0,0,0,0,0,0])
        c3 = np.array([])

    def Call (self,func,t,w):
        """ Run Solver For System """
        nSteps = len(t)
        h = t[1] - t[0]
        for i in range(nSteps):
            c = np.zeros(shape=(1,7))           # array to hold c1,c2,c3,....
            c[0] = func(t[i],w[i])
            c[1] = func(t[i] + h/5 , pass)
            c[2] = func(t[i] + h/5 , pass)
            c[3] = func(t[i] + h/5 , pass)
            c[4] = func(t[i] + h/5 , pass)
            c[5] = func(t[i] + h/5 , pass)