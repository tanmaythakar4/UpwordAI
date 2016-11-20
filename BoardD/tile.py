# -*- coding: utf-8 -*-

'''
It contain all the property related to the tiles in the board like its empty or theres's a character
and if there's some charater then how many because in upword we can add 5 charater on tile or status 
like lock or not (to help algo to add word) find the status like(Doubleword,doubleletter,Tripleword,
Tripleletter we discussed ) from board.
'''
import time
class Tile:
    

    # Initializes a new tile with a letter and number of points.
    def __init__(self, ltr):
      
     
          if(ltr == ' '):
              self.isBlank = True
          else:
              self.isBlank = False
            
          self.letter = ltr
          self.locked = False
         
          
          
    def pulse(self):
        self.lastPulseTime = time.time()
        self.dirty = True