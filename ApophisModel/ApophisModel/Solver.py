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

    def SetODE (self,func):
        """ Set the ODE to solve in form of f(t,y) """
        self._func = func

    def SetTime(self,start,finish):
        """ Set Time Range for Solver """
        self._t0 = start
        self._tf = finish
        return self
        
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
        err = h*np.abs((71/57600)*S[0] - (71/16695)*S[2] + (71/1920)*S[3] - (17253/339200)*S[4] + (22/525)*S[5] - (1/40)*S[6])
        return Z,S,err

    def CallSolver (self,w0,tol):
        """ Run Solver For System """

        # Initialize Positions & Time
        h = (self._tf - self._t0)/32
        currentState = w0
        currentTime = self._t0
        self._stepCounter = 0
        self._rejectCounter = 0
        nBodies = int(len(w0)/6)

        # Inititialize History Objects
        self._states = np.copy(currentState)
        self._times = np.array([currentTime])

        while currentTime < self._tf:
            
            # Compute next Step w/ Error
            Z,S,err = self.NextStep(currentTime,currentState,h)
            threshold = tol*h/(self._tf - self._t0)

            if min(err) < threshold:            # acceptable error (we get T/F)
                # Compute step and add to current state & time
                step = h*((5179/57600)*S[0] + (7571/16695)*S[2] + (393/640)*S[3] - (92097/339200)*S[4] + (187/2100)*S[5] + (1/40)*S[6])
                currentState += step
                currentTime += h

                # add to state histories
                self._states = np.vstack((self._states,currentState))
                self._times = np.append(self._times,currentTime)
                self._stepCounter += 1
                print(self._stepCounter)     
            else:
                # Error is too large, half the time step
                h /= 2
                self._rejectCounter += 1
            if np.min(err) < (1/16)*threshold:    # error to small?
                # Small error, double time step
                h *= 2
                self._rejectCounter += 1
            else:
                pass

            
        return self
