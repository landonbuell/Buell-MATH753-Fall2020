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
    SolarSystem.LoadSystem("AphophisModel_2020.11.12.csv")

    PlottingFunctions.PlotCurrentState(SolarSystem)
    initConds = SolarSystem.GetCurrentState 
     
    # INITIALIZE DORMAND-PRINCE SOLVER
    timeStart, timeFinish = 0, 3600*24*356
    Solver = DormandPrinceSolver(func=SolarSystem.CallSystem)
    
    # CALL THE SOLVER
    Solver.SetTime(timeStart,timeFinish)
    Solver.CallSolver(initConds,1e-4)

    # GET LAST POSITION
    lastState = Solver._states[-1]
    SolarSystem.SetCurrentState(lastState)
    SolarSystem.StoreHistories(Solver._states)
    
    PlottingFunctions.PlotCurrentState(SolarSystem)
    print("=)")

    