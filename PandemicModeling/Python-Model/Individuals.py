"""
Landon Buell
Pandemic Model
Classes - Individuals
9 September 2020
"""

        #### IMPORTS ####

import numpy as np

        #### CLASS DEFINITIONS ####

class Individual :
    """
    Class For Parent 'Individual' Object
        An individual can be a carrier of a diseases
    """

    def __init__(self,name,number,loc):
        """ 
        Initialize Class Object Instance
        --------------------------------
        name (str) : Name of Individual Instance
        number (str) : Number for individual
        --------------------------------
        Return None
        """
        self.number = number
        self.condition = 0
        self.daysSick = 0;

        self.xloc = loc[0]
        self.yloc = loc[1]


    def Condition (self,cond=None):
        """ Get or Set Current Condition (0,1,2) for Individual """
        if cond == None:
            return self.condition
        else:
            assert(type(cont) == int)
            self.condition = cond
            return self
