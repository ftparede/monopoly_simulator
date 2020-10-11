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
        self.boardState = pd.DataFrame({'P0':[0], 'P1':[0], 'P2':[0], 'P3':[0], 'lastPlayer':[0], "nextRepeatPlayer":[False], "drawn" : [""]})
        self.playerOrder = [0,1,2,3]
        self.chanceDeck = pd.read_csv("./data/chance.csv").sample(frac=1).reset_index(drop=True)
        self.chestDeck = pd.read_csv("./data/chest.csv").sample(frac=1).reset_index(drop=True)
        print(self.chanceDeck)
        print(self.chestDeck)
        
    def drawChance(self):
        return_value = self.chanceDeck.iloc[0]
        self.chanceDeck = self.chanceDeck.drop(self.chanceDeck.index[0]).append(return_value)
        return return_value
    
    def drawChest(self):
        return_value = self.chestDeck.iloc[0]
        self.chestDeck = self.chestDeck.drop(self.chestDeck.index[0]).append(return_value)
        return return_value
        
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
            
    def checkNewPosition(self, pos):
        # check if it is in jail
        if pos >= self.boardRef.shape[0]:
            pos = int(pos - self.boardRef.shape[0])
        if pos < 0:
            pos = int(pos + self.boardRef.shape[0])
        if(self.boardRef["type"].iloc[pos] == "goto"):
            return 10
        # land on chest
        if(self.boardRef["type"].iloc[pos] == "chance"):
            drawn_card = self.drawChest()
            if(drawn_card["type"]=='absoluteM'):
                return drawn_card["number"]
            if(drawn_card["type"]=='relativeM'):
                return pos + drawn_card["number"] 
            if (drawn_card["type"]=='conditionM'):
                if(drawn_card["name"]=="Advance to Railroad"):
                    if(pos<=5):
                        return 5
                    if(pos<=15):
                        return 15
                    if(pos<=25):
                        return 25
                    if(pos<=35):
                        return 35
                if(drawn_card["name"]=="Advance to Utility"):
                    if(pos<=12):
                        return 12
                    if(pos<=28):
                        return 28
        # land on chance
        if(self.boardRef["type"].iloc[pos] == "chest"):
            drawn_card = self.drawChance()
            if(drawn_card["type"]=='absoluteM'):
                return drawn_card["number"]
            if(drawn_card["type"]=='relativeM'):
                return pos + drawn_card["number"] 
            if (drawn_card["type"]=='conditionM'):
                if(drawn_card["name"]=="Advance to Railroad"):
                    if(pos<=5):
                        return 5
                    if(pos<=15):
                        return 15
                    if(pos<=25):
                        return 25
                    if(pos<=35):
                        return 35
                if(drawn_card["name"]=="Advance to Utility"):
                    if(pos<=12):
                        return 12
                    if(pos<=28):
                        return 28
        # DEFAULT return same value
        return pos
        
    def playturn(self):
        print(self.boardState)
        # next player
        next_player = self.nextPlayer()
        current_pos = self.boardState["P"+str(next_player)].iloc[-1]
        # roll the dice
        throw = self.rolldice()
        # get new position
        new_pos = int(throw["value"]+current_pos)
        if new_pos > self.boardRef.shape[0]:
            new_pos = int(new_pos - self.boardRef.shape[0])
        # correct position according to rules
        new_pos = self.checkNewPosition(new_pos)
        # PENDING
        # create new state vector
        newState = self.boardState.iloc[-1]
        newState["P"+str(next_player)] = new_pos
        newState["nextRepeatPlayer"] = throw["reroll"]
        newState["lastPlayer"] = next_player
        self.boardState = self.boardState.append(newState, ignore_index= True)
        print(newState)
        
        
pd.set_option('mode.chained_assignment', None)        
myBoard = board()
for i in range(1,100000):
    myBoard.playturn()
        
