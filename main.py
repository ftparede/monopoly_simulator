# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# https://towardsdatascience.com/7-strategies-to-win-monopoly-a89ead18b062
#https://stat-jet-asu.github.io/Datasets/InstructorDescriptions/monopoly.html

import pandas as pd
import numpy as np
from random import randrange


class board:
    
    def __init__(self):
        self.boardRef = pd.read_csv("./data/monopolygame.csv")
        print("init")
        print(self.boardRef)
        self.boardState = pd.DataFrame({'P0':[0], 'P1':[0], 'P2':[0], 'P3':[0], 'lastPlayer':[0], "nextRepeatPlayer":[False]})
        self.playerOrder = [0,1,2,3]
        
    def rolldice(self):
        roll1 = randrange(1,7)
        roll2 = randrange(1,7)
        return {"value": roll1+roll2, "reroll": roll1 == roll2}
    
    def nextPlayer(self):
        lastPlayer = self.boardState['lastPlayer'].iloc[-1]
        if self.boardState["nextRepeatPlayer"].iloc[-1]:
            return lastPlayer
        else:
            if lastPlayer + 1 > 3:
                return 0
            else:
                return lastPlayer +1
        
    def playturn(self):
        print(self.boardState)
        # next player
        next_player = self.nextPlayer()
        current_pos = self.boardState["P"+str(next_player)].iloc[-1]
        # roll the dice
        throw = self.rolldice()
        # get new position
        new_pos = throw["value"]+current_pos
        if new_pos > self.boardRef.shape[0]:
            new_pos = new_pos - self.boardRef.shape[0]
        # correct position according to rules
        # PENDING
        # create new state vector
        newState = self.boardState.iloc[-1]
        newState["P"+str(next_player)] = new_pos
        newState["nextRepeatPlayer"] = throw["reroll"]
        newState["lastPlayer"] = next_player
        self.boardState = self.boardState.append(newState, ignore_index= True)
        print(newState)
        
        
        
myBoard = board()
for i in range(1,10):
    myBoard.playturn()
        
