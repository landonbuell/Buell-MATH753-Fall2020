"""
Landon Buell
Pandemic Model
Classes - Models
9 September 2020
"""

        #### IMPORTS ####

import numpy as np

import Individuals
import Locations

        #### CLASS DEFINITIONS ####

class BaseModel :
    """ 
    Parent Model Object 
    """

    def __init__(self,name):
        """ Intialize Object Instance """
        self.modelName = name
        self.modelType = "Parent"
        self.modelIndividuals = []

    def __repr__(self):
        return self.modelType+" Model Object"

    

    def Compile (self):
        """ Compile Model Instance """
        raise NotImplementedError()

   
    
class SingleLocationModel (BaseModel):
    """
    SIR model containing a single location
        Inherits from BaseModel
    """

    def __init__(self,name):
        """ Initialize Class Object Instance """
        super().__init__(name)
        self.modelType = "Single-Location"
        

    def AddIndividuals (self, numNew, names=None, locs=None):
        """ Add New Individuals to this Model """
        for i in range(numNew):         # each new person to add
            pass
        raise NotImplementedError()


class MultiLocationModel (BaseModel):
    """
    SIR model containing a single location
        Inherits from BaseModel
    """

    def __init__(self,name):
        """ Initialize Class Object Instance """
        super().__init__(name)
        self.modelType = "Mutli-Location"
        self.locations = []

    def AddLocation (self,newLoc):
        """ Add New Location to this Model """
        raise NotImplementedError()


    


    


