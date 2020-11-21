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

from Solver import *

            #### CLASS DEFINITIONS ####

class OrbitalSystem :
    """ 
    Model an Orbital System with a Collection of Interacting Bodies 
    --------------------------------
    name (str) : Name To indentify 
    bodyList (list) : List of 'Body' Objects in this system
    solver (DP) : Dormand-Prince ODE Solver Method
    --------------------------------
    Return Instantiated Orbital System
    """

    def __init__(self,name,bodyList=[],time=[]):
        """
        Constructor for Orbital System 
        """
        self._name = name
        self._bodyList = bodyList
        self._time = time
        self.Solver = DormandPrinceSolver()
      
    def AddBody (self,newBody):
        """ Add 'newBody' to List of Bodies """
        self._bodyList.append(newBody)
        return self

    def PopBody (self,index=-1):
        """ Remove & Return Body at Index """
        raise NotImplementedError()

    @property
    def GetTime(self):
        """ Return Time-Axis """
        return self._time

    @GetTime.setter
    def SetTime(self,value):
        """ Set Time-Axis """
        self._time = value

    def GetPositionIndex(self,index):
        """ Get Position for each body in the system """
        assert index in [0,1,2]
        return np.array([body._pos[index] for body in self._bodyList])

    def GetVelocityIndex(self,index):
        """ Get Position for each body in the system """
        assert index in [0,1,2]
        return np.array([body._vel[index] for body in self._bodyList])

    def GetAccelerationIndex(self,index):
        assert index in [0,1,2]
        return np.array([body._acl[index] for body in self._bodyList])

    @property
    def GetNames(self):
        """ Get array of names for all bodies in this system """
        return np.array([body._name for body in self._bodyList])

    @property
    def GetMasses(self):
        """ Get array of masses for all bodies in this system """
        return np.array([body._mass for body in self._bodyList])

    @property
    def GetRadii(self):
        """ Get array of radii for all bodies in this system """
        return np.array([body._rad for body in self._bodyList])

    @property
    def GetCenterOfMass(self):
        """ Compute [x,y,x] center of mass """
        weightedPositions = np.array([body._mass * body._pos for body in self._bodyList])
        weightedSum = np.sum(weightedPositions,axis=0)
        return weightedSum / self.GetMasses.sum()

    def CallSystem(self,nIters):
        """ Call the System - Execute ODE Solver For Iterations """
        
        # Build function to Pass into Dormand-Prince Solver




    def PlotCurrentState(self):
        """ Plot the Current System in the XY-plane """
        plt.figure(figsize=(16,12))
        plt.ylabel("Y-Axis",size=20,weight='bold')
        plt.xlabel("X-Axis",size=20,weight='bold')

        xPositions = self.GetPositionIndex(0)
        yPositions = self.GetPositionIndex(1)
        
        # Plot All Bodies
        plt.scatter(x=xPositions,y=yPositions,
                    s=np.log(self.GetRadii),marker='o')
        for x,y,s in zip(xPositions,yPositions,self.GetNames):
            plt.text(x,y,s)

        # Plot Center of Mass
        centerOfMass = self.GetCenterOfMass
        plt.scatter(centerOfMass[0],centerOfMass[1],
                    marker="X",cmap=plt.cm.jet)
        plt.text(centerOfMass[0],centerOfMass[1],"Center of Mass")

        plt.grid()
        plt.tight_layout()
        plt.show()
            

    def __repr__(self):
        """ Return Documentation String on this Orbital System Object """
        return self._name
