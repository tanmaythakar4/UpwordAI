# -*- coding: utf-8 -*-

'''
this file will maintain the statstic through out the game which we gonna use 
to generate next move and in heuristic function in future

Stats:  Timing
        Letter
        Seed
        Game
        
this will generate text file
        
'''


class AIStats():
    
    FILENAME = "Generator/aistats.txt"
    COLLECT_WORD_DATA = False
    COLLECT_GAME_DATA = False
    
    def __init__(self):
        
        self.timingInfo = []
        self.letterPlays = {}
        for code in range(ord('A'))