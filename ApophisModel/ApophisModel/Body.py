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

class BodyObject :
    """
    Represents an Celestial Body: Planet, Asteroid, Star, etc.
    --------------------------------
    name (str) : Name to identify Body Object
    mass (float) : Mass of Body in Kg
    rad (float) : Equitorial Radius of body
    pos (arr) : Position of body as 3-vectorin Km
    vel
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
        self._G = 6.67e-11

        # Vector atrribtues
        self._pos = pos
        self._vel = vel
        self._acl = np.zeros(shape=3)

    def ClearAccel(self):
        """ Return Acceleration Vector to zero-vector """
        self._acl = np.zeros(shape=3)
        return self

    def __add__(self,other):
        """ 'Add' Bodies together, add to net _acl on self """
        dr = (self._pos - other._pos) / np.abs(self._pos - other._pos)**2 