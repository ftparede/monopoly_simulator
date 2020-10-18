# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# https://towardsdatascience.com/7-strategies-to-win-monopoly-a89ead18b062
#https://stat-jet-asu.github.io/Datasets/InstructorDescriptions/monopoly.html
import pandas as pd
import numpy as np

from lib.board import board, runSim
        
pd.set_option('mode.chained_assignment', None)        
myBoard = runSim(steps = 200)
print(myBoard.statPositions)
        
