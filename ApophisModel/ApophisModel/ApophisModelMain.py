"""
Landon Buell
Mark Lyon
MATH 753.01 - HW10
13 November 2020
"""

            #### IMPORTS ####

import numpy as np
import os

from OrbitalSystem import *
from Body import *


if __name__ == "__main__":

    # INITIALIZE SYSTEM & ADD BODIES
    SolarSystem = OrbitalSystem("Solar System")

    SolarSystem.AddBody(BodyObject("Alpha",2e20,1e8,
                    pos=np.array([1e3,0,0]),vel=np.array([0,+10,0])))
    SolarSystem.AddBody(BodyObject("Beta",1e20,1e8,
                    pos=np.array([-1e3,0,0]),vel=np.array([0,-10,0])))
    SolarSystem.AddBody(BodyObject("Gamma",1e15,1e8,
                    pos=np.array([0,1e4,0]),vel=np.array([0,-100,0])))

    SolarSystem.PlotCurrentState()