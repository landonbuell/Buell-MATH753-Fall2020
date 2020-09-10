"""
Landon Buell
Pandemic Model
Classes - Locations
9 September 2020
"""

        #### IMPORTS ####

import numpy as np

        #### CLASS DEFINITIONS ####

class BaseLocation :
    """
    Parent Class for All Location Objects 
    """

    def __init__(self,name,number,position,size):
        """ Intialize Class Object Instance """
        self.locationName = name
        self.locationNumber = number
        self.locationType = "Parent"

        self.xpos = position[0]
        self.ypos = position[1]
        self.width = size[0]
        self.height = size[1]

    @property
    def GetPosition (self):
        """ Return Lower Left Corner of location instance """
        return (self.xpos,self.ypos)

    @property
    def GetSize (self):
        """ Return Length, Width of location instance """
        return (self.width,self.height)