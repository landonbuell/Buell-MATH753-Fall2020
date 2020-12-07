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

    # INITIALIZE SYSTEM & ADD BODIES
    SolarSystem = OrbitalSystem("Solar System")
    SolarSystem.LoadSystem("DemoSystem.csv")

    #PlottingFunctions.PlotCurrentState(SolarSystem)
    initConds = SolarSystem.GetCurrentState 
     
    # INITIALIZE DORMAND-PRINCE SOLVER
    timeStart, timeFinish = 0, 3600*24*356
    Solver = DormandPrinceSolver(func=SolarSystem.CallSystem)
    Solver.SetTime(timeStart,timeFinish)

    # CALL THE SOLVER
    Solver.CallSolver(initConds,1e-4)

    # GET LAST POSITION
    lastState = Solver._states[-1]
    lastState = np.reshape(lastState,shape=(-1,6))
    

    print("=)")

    