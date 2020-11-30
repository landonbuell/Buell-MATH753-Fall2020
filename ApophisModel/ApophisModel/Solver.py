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

    def __init__(self,func=None):
        """ Initialize DormandPrinceSolver Instance """
        self._func = func
        self._X = self.ConstantsMatrix

    def SetODE (self,func):
        """ Set the ODE to solve in form of f(t,y) """
        self._func = func

    @property
    def ConstantsMatrix(self):
        X = np.empty(shape=(8,7))
        X[0] = np.zeros(shape=(7))
        X[1] = np.array([0.2,0,0,0,0,0,0])
        X[2] = np.array([3/40,9/40,0,0,0,0,0])
        X[3] = np.array([44/45,-56/15,9/40,0,0,0,0])
        X[4] = np.array([19732/6561,-25360/2187,64448/6561,-212/729,0,0,0])
        X[5] = np.array([9017/3168,-355/33,46732/5247,49/167,-5103/18656,0,0])
        X[6] = np.array([35/384,0,500/1113,125/192,-2187/6784,11/84,0])
        X[7] = np.array([5179/57600,0,7571/16695,393/640,-92097/339200,187/2100,1/40])
        return X
        
    def NextStep (self,t,w):
        """ 
        Compute Constants Array  
        --------------------------------
        func (callable) : Function to solve
        t (float) : Current time index
        w (float) : Current position index
        --------------------------------
        """
        self._S = np.zeros(shape=(7,len(w)))       # array to hold [c1,c2,c3,....]
        tSteps = np.array([0,1/5,3/10,4/5,8/9,1,0]) # for each timeStep

        s0 = self._func(t,w)                        # inital function call        
        self._S[0] = s0

        # Compute Each entry
        for i in range (1,7):                       # each "s" in DP-Solver
            dotProd = np.dot(self._X[i].transpose(),self._S)                            # w + h * (...)
            Si = self._func(t + self._h*tSteps[i] , w + self._h*dotProd)    # f(t+h(...) , w + h(...)
            self._S[i] = Si          # add to array
            if i == 6:      # for the 6-th iter
                self._Z = w + self._h*dotProd   # save the value fo err
        nextStep = w + self._h*np.dot(self._X[7],self._S)
        return nextStep     # return next step

    def Call (self,t,w,tol):
        """ Run Solver For System """
        nSteps = len(t)
        path = np.empty(shape=(nSteps,len(w)))
        path[0] = w
        self._h = t[1] - t[0]   
        for i in range(nSteps):
            nextStep = self.NextStep(t[i],path[i])  # compute next step
            err = self._Z - nextStep                # error in step

            # need to test error tol
            path[i] = nextStep

        plt.plot(t,path[:,0])
        plt.plot(t,path[:,1])
        plt.show()

        return self


            
            