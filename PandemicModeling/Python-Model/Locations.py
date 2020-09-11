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
    --------------------------------

    --------------------------------

    """

    def __init__(self,name,position,size):
        """ Intialize BaseLocation Object Instance """
        self.locationName = name
        self.locationNumber = None
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
    def GetShape (self):
        """ Return Length, Width of location instance """
        return (self.width,self.height)

class Community (BaseLocation):
    """ 
    Community Class Object, Inherits from BaseLocation
    --------------------------------
    Groups of Individuals Live Here, and only leave or inter-mingle occasionally
    Use to represent small towns, neighborhoods, or large families
    --------------------------------
    
    """

    def __init__(self,name,position,size):
       """ Initialize Community Location Object Instance """
       super().__init__(name,position,size)
       self.locationType = "Community"

class PublicArea (BaseLocation):
    """ 
    Public Area Class Object, Inherits from BaseLocation
    --------------------------------
    Groups of Individuals Live Here, and only leave or inter-mingle occasionally
    Use to represent public areas, schools, churches, gorcery stores
    --------------------------------
    
    """

    def __init__(self,name,position,size):
       """ Initialize Community Location Object Instance """
       super().__init__(name,position,size)
       self.locationType = "Community"

class Quarentine (BaseLocation):
    """ 
    Quarentine Class Object, Inherits from BaseLocation
    --------------------------------
    Individuals who test postive are placed here, and leave once recovered
    Use to represent isolated homes, hosptials
    --------------------------------
    
    """
    def __init__(self,name,position,size):
       """ Initialize Quarentine Location Object Instance """
       super().__init__(name,position,size)
       self.locationType = "Quarentine"