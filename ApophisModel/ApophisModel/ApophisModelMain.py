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

    #PlottingFunctions.PlotCurrentState(SolarSystem)
    
    # SET TIME AXIS & GET INITIAL VALUES
    SolarSystem.SetTime(np.arange(0,int(1e6),100))
    initConds = SolarSystem.GetCurrentState  

    # INITIALIZE DORMAND-PRINCE SOLVER
    Solver = DormandPrinceSolver(func=OrbitalSystemCallable.CallSystem)
    Solver.SetMasses(SolarSystem.GetMasses) 

    # CALL THE SOLVER
    Solver.Call(SolarSystem._time,initConds,1e-4)

    # GET MOST RECENT STATE & Apply to System
    lastState = Solver._lastState
    lastState = np.reshape(lastState,newshape=(-1,6))
    for i in range(len(SolarSystem._bodyList)):     # each body
        SolarSystem._bodyList[i].SetStateVector(lastState[i])

    # APPLY POSITION HISTORITES TO BODIES
    stateHistory = Solver._stateHistories.reshape((Solver._nSteps,6,-1))
    for i in range(len(SolarSystem._bodyList)):     # each body
        xHist = stateHistory[:,i,0]
        yHist = stateHistory[:,i,1]
        zHist = stateHistory[:,i,2]
        SolarSystem._bodyList[i].SetHistoryArrays(xHist,yHist,zHist)

    PlottingFunctions.PlotHistoricalState(SolarSystem)

    print("=)")

    