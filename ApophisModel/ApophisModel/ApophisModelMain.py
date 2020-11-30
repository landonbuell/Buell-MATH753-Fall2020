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
from Solver import *


if __name__ == "__main__":

    # Create Test ODE
    func = lambda t,y : np.array([0.5*y[0] , 1.5*y[1]])
    t = np.arange(0,100,0.1)
    w = np.array([1,2])
    DPSolver = DormandPrinceSolver(func)
    DPSolver.Call(t,w,tol=1e-4)


    # INITIALIZE SYSTEM & ADD BODIES
    SolarSystem = OrbitalSystem("Solar System")

    SolarSystem.AddBody(BodyObject("Alpha",2e20,1e8,
                    pos=np.array([1e3,0,0]),vel=np.array([0,+10,0])))
    SolarSystem.AddBody(BodyObject("Beta",1e20,1e8,
                    pos=np.array([-1e3,0,0]),vel=np.array([0,-10,0])))
    SolarSystem.AddBody(BodyObject("Gamma",1e15,1e8,
                    pos=np.array([0,1e4,0]),vel=np.array([0,-100,0])))

    SolarSystem.PlotCurrentState()