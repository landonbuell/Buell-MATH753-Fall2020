"""
Landon Buell
Pandemic Model
Main Executable
9 September 2020
"""

        #### IMPORTS ####

import numpy as np

import Models
import Individuals
import Locations

        #### MAIN EXECUTABLE ####

if __name__ == '__main__':

    MODEL = Models.SingleLocationModel("SIR-TEST")
    
    MODEL.AddLocation(Locations.Community(name="COM1",position=(0,0),size=(101,101)))


    print("=)")