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

    def __init__(self,func=None,start=0,finish=0):
        """ Initialize DormandPrinceSolver Instance """
        self._func = func
        self._t0 = start
        self._tf = finish
        self._X = self.ConstantsMatrix

    def SetODE (self,func):
        """ Set the ODE to solve in form of f(t,y) """
        self._func = func

    def SetTime(self,start,finish):
        """ Set Time Range for Solver """
        self._t0 = start
        self._tf = finish
        return self

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
        
    def NextStep (self,t,w,h):
        """ 
        Compute Constants Array  
        --------------------------------
        func (callable) : Function to solve
        t (float) : Current time index
        w (arr) : Current state vector (k,)
        --------------------------------
        """
        S = np.empty(shape=(7,len(w)))        # array to hold [c1,c2,c3,....]
        # Compute elements in S-vector, 
        S[0] = self._func(t, w) 
        S[1] = self._func(t + (1/5)*h,
            w + h*((1/5)*S[0]))
        S[2] = self._func(t + (3/10)*h, 
            w + h*((3/40)*S[0] + (9/40)*S[0]))
        S[3] = self._func(t + (4/5)*h, 
            w + h*((44/45)*S[0] - (56/15)*S[1]+ + (32/9)*S[2]))
        S[4] = self._func(t + (8/9)*h,
            w + h*((19732/6561)*S[0] - (25360/2187)*S[1] + (64448/6561)*S[2] - (212/72)*S[3]))
        S[5] = self._func(t + h,
            w + h*((9017/3168)*S[0] - (355/33)*S[1] + (46732/5247)*S[2] + (49/167)*S[3] - (5103/18656)*S[4]))
        # "Z" is used to comput error in the step
        Z = w + h*((35/384)*S[0] + (500/1113)*S[2] + (125/192)*S[3] - (2187/6784)*S[4] + (11/84)*S[5])
        S[6] = self._func(t + h, Z)
        # Compute the Next Step
        nextStep = w + h*((5179/57600)*S[0] + (7571/16695)*S[2] + (393/640)*S[3] - (92097/339200)*S[4] + \
            (187/2100)*S[5] + (1/40)*S[6])
        # Return the next step & The "Z" vector
        return nextStep,Z

    def CallSolver (self,w0,tol):
        """ Run Solver For System """

        # Initialize Positions & Time
        h = (self._tf - self._t0)/4
        currentState = w0
        currentTime = self._t0
        self._stepCounter = 0

        # Inititialize History Objects
        self._states = np.copy(currentState)
        self._times = np.array([currentTime])

        while currentTime < self._tf:
            # Compute potential next step
            W,Z = self.NextStep(currentTime,currentState,h)  # CHECK THIS!!!
            err = np.abs(Z - W)         

            if np.min(err < tol*h/(self._tf - self._t0)) > 0:   # error is acceptable
                # Update the State & the time
                currentState = W        # update state vector
                currentTime += h        # update time scalar               
                # Store the state & time
                self._states = np.vstack((self._states,currentState))
                self._times = np.append(self._times,currentTime)
                self._stepCounter += 1

            elif np.min(err < (1/50)*tol*h/(self._tf - self._t0)) > 0:               
                h *= 2      # Error is small, increase step
            else:                
                h /= 2      # Error is large, decrease step
        return self


class OrbitalSystemCallable:
    """ Class Contains static callable method for DP-Solver to execute """

    @staticmethod
    def CallSystem(t,y,masses):
        """ Call System at time t w/ state vector y """

        raise NotImplementedError()

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


            
            