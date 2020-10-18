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

# run sims
data = []
runs = 10
for i in range(0,runs):
    myBoard = runSim(steps = 200)
    data.append(myBoard)

#%%
# 1 get probability of every position
ppos = data[0].statPositions
for i in range(1,runs):
    ppos["q_visits"] = ppos["q_visits"] + data[i].statPositions["q_visits"]
ppos["q_visits"] = ppos["q_visits"]/sum(ppos["q_visits"])
# 2 get expected returns
ppos["exp_0"] = ppos["q_visits"] * data[0].boardRef["rent_0"]
ppos["exp_1"] = ppos["q_visits"] * data[0].boardRef["rent_1"]
ppos["exp_2"] = ppos["q_visits"] * data[0].boardRef["rent_2"]
ppos["exp_3"] = ppos["q_visits"] * data[0].boardRef["rent_3"]
ppos["exp_4"] = ppos["q_visits"] * data[0].boardRef["rent_4"]
ppos["exp_5"] = ppos["q_visits"] * data[0].boardRef["rent_hotel"]
# 3 get costs of every stage
ppos["cost_0"] = data[0].boardRef["cost"]
ppos["cost_1"] = data[0].boardRef["cost"] + data[0].boardRef["house_price"]
ppos["cost_2"] = data[0].boardRef["cost"] + 2*data[0].boardRef["house_price"]
ppos["cost_3"] = data[0].boardRef["cost"] + 3*data[0].boardRef["house_price"]
ppos["cost_4"] = data[0].boardRef["cost"] + 4*data[0].boardRef["house_price"]
ppos["cost_5"] = data[0].boardRef["cost"] + 5*data[0].boardRef["house_price"]
