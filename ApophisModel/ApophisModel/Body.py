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

class BodyObject () :
    """
    Represents an Celestial Body: Planet, Asteroid, Star, etc.
        Contaisn finer details / Extra params
    --------------------------------
    name (str) : Name to identify Body Object
    mass (float) : Mass of Body in Kg
    rad (float) : Equitorial Radius of body
    pos (arr) : Position of body as 3-vector in [m]
    vel (arr) : Velcity of body as 3-vector in [m/s]
    --------------------------------
    Return Instantiated Body Object
    """

    def __init__(self,name,mass,rad,pos=np.zeros(3),vel=np.zeros(3)):
        """ Initialize body Object Instance """

        # Scalar Attributes
        self._name = name
        self._mass = mass
        self._rad = rad
        self._vol = (4/3)*np.pi*self._rad**3
        self._den = self._mass / self._vol

        # Vector atrribtues
        self._pos = pos
        self._vel = vel
        self._acl = np.zeros(3)

    @property
    def GetStateVector (self):
        """ Get the State vector for this body """
        stateVector = np.empty(shape=(6))
        stateVector[0:3] = self._pos
        stateVector[3:6] = self._vel
        return stateVector

    @property
    def GetStateVectorDeriv (self):
        """ Get the State vector for this body """
        stateVector = np.empty(shape=(6))
        stateVector[0:3] = self._vel
        stateVector[3:6] = self._acl
        return stateVector

    def SetStateVector(self,value):
        """ Get the State vector for this body """
        self._pos = value[0:3]
        self._vel = value[3:6]
        return self

    def SetHistoryArrays(self,xHist,yHist,zHist):
        """ Attatch Object Path to Self """
        self._xHist = xHist
        self._yHist = yHist
        self._zHist = zHist
        return self

    def SavePaths (self,x,y,z):
        """ Save X,Y,Z paths in local Object """
        pass



