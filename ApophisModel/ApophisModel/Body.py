"""
Landon Buell
Mark Lyon
MATH 753.01 - HW10
13 November 2020
"""

            #### IMPORTS ####

import numpy as np

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

    def SetStateVector(self,value):
        """ Get the State vector for this body """
        self._pos = value[0:3]
        self._vel = value[3:6]
        return self

    def SetHistoryArrays(self,stateHistory):
        """ Attatch Object Path to Self """
        self._xHist = stateHistory[0]
        self._yHist = stateHistory[1]
        self._zHist = stateHistory[2]
        return self


