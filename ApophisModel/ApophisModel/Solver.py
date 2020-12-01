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

from Body import *

            #### CLASS DEFINITIONS ####

class DormandPrinceSolver :
    """
    Dormand Prince Solver for Systems of ODEs
    """

    def __init__(self,func=None,masses=None):
        """ Initialize DormandPrinceSolver Instance """
        self._func = func
        self._masses = masses
        self._X = self.ConstantsMatrix

    def SetODE (self,func):
        """ Set the ODE to solve in form of f(t,y) """
        self._func = func

    def SetMasses (self,masses):
        """ Set masses from parent orbital system """
        self._masses = masses

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
        self._S = np.zeros(shape=(7,len(w)))        # array to hold [c1,c2,c3,....]
        tSteps = np.array([0,1/5,3/10,4/5,8/9,1,0]) # for each timeStep
        s0 = self._func(t,w,self._masses)           # inital function call        
        self._S[0] = s0

        # Compute Each entry
        for i in range (1,7):               # each "s" in DP-Solver
            dotProd = np.dot(self._X[i].transpose(),self._S)            # w + h * (...)

            # Call 'func' w/ t , w/ w and w/ masses
            self._S[i] = self._func(t + self._h*tSteps[i] , w + self._h*dotProd , self._masses)

            if i == 6:                      # for the 6-th iter
                self._Z = w + self._h*dotProd   # save the value fo err

        nextStep = w + self._h*np.dot(self._X[7],self._S)
        return nextStep                     # return next step

    def Call (self,t,w0,tol):
        """ Run Solver For System """

        # Initialize Path Array
        self._nSteps = len(t)       
        self._stateHistories = np.empty(shape=(self._nSteps,len(w0)))
        self._stateHistories[0] = w0

        # Intialize Step Size & Tolerance Params
        self._h = t[1] - t[0]  
        self._tolParam = tol*self._h

        # Iterate through Time
        state = w0
        for i in range(self._nSteps-1):
            state = self.NextStep(t[i],state)   # compute next step
            err = self._Z - state               # error in step

            # need to test error tol

            self._stateHistories[i+1] = state

        self._lastState = state
        return self


class OrbitalSystemCallable:
    """ Class Contains static callable method for DP-Solver to execute """

    @staticmethod
    def CallSystem(t,y,masses):
        """ Call System at time t w/ state vector y """
        G = 6.67e-20
        y = np.reshape(y,newshape=(-1,6))       # each row represents body
        newState = np.empty(shape=y.shape)      # empty array to hold new state

        for i in range (len(y)):        # each body
            posA = y[i,0:3]             # position vector
            aclVec = np.zeros(3)        # empty acl vector
            for j in range (len(y)):    # each body
                if i == j:              # same body?
                    continue            # skip
                posB = y[j,0:3]         # position vector
                
                # Compute Aceelration of A due to B
                dr = (posB - posA) / np.abs(posB - posA)**3
                aclVec += G*masses[j]*dr

            # new state vector for this body
            newState[i] = np.concatenate((y[i,3:6],aclVec),axis=None)    
        return newState.ravel()         # return the new state


            
            