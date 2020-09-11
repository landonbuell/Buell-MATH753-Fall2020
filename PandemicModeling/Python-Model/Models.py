"""
Landon Buell
Pandemic Model
Classes - Models
9 September 2020
"""

        #### IMPORTS ####

import numpy as np
import scipy.sparse as sparse

import Individuals
import Locations

        #### CLASS DEFINITIONS ####

class BaseModel :
    """ 
    Parent Model Object 
    """

    def __init__(self,name,size=(1001,1001)):
        """ Intialize Object Instance """
        self.modelName = name
        self.modelType = "Parent"

        self.modelWidth = int(size[0])
        self.modelHeight = int(size[1])
        self.worldBoard = self.GenerateBoard()
        
        self.modelIndividuals = []
        self.modelLocations = []

    def GenerateBoard(self):
        """ Generate World Board, Given size """
        return np.zeros(self.GetShape,dtype=np.byte)

    def __repr__(self):
        return self.modelType+" Model Object"

    @property
    def GetBoard (self):
        """ Return current World Board as N x M matrix """
        return self.worldBoard

    @property
    def GetShape(self):
        """ Return tuple size (width,height) of this Model """
        return (self.modelWidth,self.modelHeight)

    @property
    def GetLocations(self):
        """ Return List of Locations in this Model """
        return (self.modelLocations)

    def AddLocation (self, newLoc):
        """ Add New Location to Model """
        self.modelLocations.append(newLoc)
        return self

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



    


    


