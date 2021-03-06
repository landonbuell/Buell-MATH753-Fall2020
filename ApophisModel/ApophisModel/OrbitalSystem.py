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
from Body import *

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

    def __init__(self,name,bodyList=[]):
        """
        Constructor for Orbital System 
        """
        self._name = name
        self._bodyList = bodyList
        self._nBodies = len(self._bodyList)
        self._G = 6.67e-20
      
    def AddBody (self,newBody):
        """ Add 'newBody' to List of Bodies """
        self._bodyList.append(newBody)
        self._nBodies += 1
        return self

    def PopBody (self,index=-1):
        """ Remove & Return Body at Index """
        raise NotImplementedError()

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

    def GetPositionIndex(self,index):
        """ Get Position[index] for each body in the system """
        assert index in [0,1,2]
        return np.array([body._pos[index] for body in self._bodyList])

    def GetVelocityIndex(self,index):
        """ Get Velocity[index] for each body in the system """
        assert index in [0,1,2]
        return np.array([body._vel[index] for body in self._bodyList])

    def GetAccelerationIndex(self,index):
        """ Get Acceleration[index] for each body in the system """
        assert index in [0,1,2]
        return np.array([body._acl[index] for body in self._bodyList])

    def CallSystem(self,t,y):
        """ Call System at time t w/ state vector y """
        
        # Reshape state vector - each row represents body
        y = np.reshape(y,newshape=(-1,6))       # [x,y,z,dx,dy,dz]
        newState = np.empty(shape=y.shape)      # empty array to hold update

        for i in range (len(y)):        # each body
            posA = y[i,0:3]             # position vector
            aclVec = np.zeros(3)        # empty acl vector
            for j in range (len(y)):    # each body
                if i == j:              # same body?
                    continue            # skip
                posB = y[j,0:3]         # position vector
                
                # Compute Aceelration of A due to B (r is a 3-vector)
                dr = (posB - posA) / np.abs(posB - posA + 1e-10)**3     # r/|r|^3
                aclVec += self._G*self.GetMasses[j]*dr                  # add acl to this body

            # new state vector for this body 
            newState[i,0:3] = y[i,3:6]
            newState[i,3:6] = aclVec
            # Row Format: [dx,dy,dz,d2x,d2y,d2z]
        return newState.ravel()         # return the new state

    @property
    def GetCenterOfMass(self):
        """ Compute [x,y,x] center of mass """
        weightedPositions = np.array([body._mass * body._pos for body in self._bodyList])
        weightedSum = np.sum(weightedPositions,axis=0)
        return weightedSum / self.GetMasses.sum()

    def LoadSystem(self,filePath):
        """ Load a System from parameters in local .CSV File """
        systemFile = pd.read_csv(filePath,header=0)
        systemArray = systemFile.to_numpy()
        for body in systemArray:        # each row od CSV file
            posVec = np.array(body[3:6],dtype=np.float64)
            velVec = np.array(body[6:9],dtype=np.float64)
            newBody = BodyObject(body[0],float(body[1]),float(body[2]),
                                 pos=posVec,vel=velVec)
            self.AddBody(newBody)
        return self

    def ExportSystem(self,filePath):
        """ Export the Current State of a System to File """
        systemFile = pd.DataFrame(data=None,index_col=False)
        systemFile['name'] = self.GetNames
        systemFile['mass'] = self.GetMasses
        systemFile['radius'] = self.GetRadii
        for idx,comp in enumerate(['X','Y','Z']):
            systemFile[comp] = self.GetPositionIndex(idx)
        for idx,comp in enumerate(['dX','dY','dZ']):
            systemFile[comp] = self.GetVelocityIndex(idx)
        systemFile.to_csv(filePath,index=False)
        return self

    @property
    def GetCurrentState(self):
        """ Return [X,Y,Z,dX,dY,dZ] for all Bodies in System as 1D Array """
        currentState = np.array([])
        for body in self._bodyList:     # each body
            currentState = np.append(currentState,body.GetStateVector)
        return currentState

    def SetCurrentState(self,stateVector):
        """ Set [X,Y,Z,dX.dY,dZ] for all bodies in system """
        stateVector = np.reshape(stateVector,newshape=(self._nBodies,6))
        for i in range(self._nBodies):     # each body
            self._bodyList[i].SetStateVector(stateVector[i])
        return self

    def StoreHistories(self,stateHistories):
        """ Store [X,Y,Z] for each system """
        nSteps = stateHistories.shape[0]        # number of steps
        states = np.reshape(stateHistories,newshape=(self._nBodies,6,nSteps))
        for i in range(self._nBodies):
            history = states[i,0:3,:]
            self._bodyList[i].SetHistoryArrays(history)
        return self
            
    def __repr__(self):
        """ Return Documentation String on this Orbital System Object """
        return self._name 

class PlottingFunctions :
    """
    Static Class with Methods to Visulize Current State or Path of System
    """

    @staticmethod
    def PlotCurrentState(System):
        """ Plot the Current System in the XY-plane """
        plt.figure(figsize=(16,12))
        plt.ylabel("Y-Axis",size=20,weight='bold')
        plt.xlabel("X-Axis",size=20,weight='bold')

        xPositions = System.GetPositionIndex(0)
        yPositions = System.GetPositionIndex(1)
        
        # Plot All Bodies
        plt.scatter(x=xPositions,y=yPositions,
                    s=np.log(System.GetRadii),marker='o')
        for x,y,s in zip(xPositions,yPositions,System.GetNames):
            plt.text(x,y,s)

        # Plot Center of Mass
        #centerOfMass = System.GetCenterOfMass
        #plt.scatter(centerOfMass[0],centerOfMass[1],marker="X",cmap=plt.cm.jet)
        #plt.text(centerOfMass[0],centerOfMass[1],"Center of Mass")

        plt.grid()
        plt.tight_layout()
        plt.show() 

    @staticmethod
    def PlotHistoricalState(System):
        """ Plot the Current System in the XY-plane """
        plt.figure(figsize=(16,12))
        plt.ylabel("Y-Axis",size=20,weight='bold')
        plt.xlabel("X-Axis",size=20,weight='bold')

        xPositions = System.GetPositionIndex(0)
        yPositions = System.GetPositionIndex(1)
        
        # Plot All Paths
        for i in range(len(System._bodyList)):     # each body
            plt.plot(System._bodyList[i]._xHist,System._bodyList[i]._yHist)

        # Plot Current Positions
        plt.scatter(x=xPositions,y=yPositions,
                    s=np.log(System.GetRadii),marker='o')
        for x,y,s in zip(xPositions,yPositions,System.GetNames):
            plt.text(x,y,s)

        plt.grid()
        plt.tight_layout()
        plt.show() 