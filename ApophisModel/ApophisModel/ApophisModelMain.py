"""
Landon Buell
Mark Lyon
MATH 753.01 - HW10
13 November 2020
"""

            #### IMPORTS ####

import numpy as np
import os

import ApophisModelUtils as Utils

if __name__ == "__main__":

    # INITIALIZE SYSTEM & ADD BODIES
    SolarSystem = Utils.OrbitalSystem("Solar System")

    SolarSystem.AddBody(Utils.Body("Alpha",1e20,1e8,
                    pos=np.array([1e3,0,0]),vel=np.array([0,+10,0])))
    SolarSystem.AddBody(Utils.Body("Beta",1e20,1e8,
                    pos=np.array([-1e3,0,0]),vel=np.array([0,-10,0])))

    SolarSystem.PlotCurrentState()