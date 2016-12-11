# -*- coding: utf-8 -*-

'''
this file contain a method to gerate the pile or rack of 7 character which we are using 
through out the game to find out the word
like add,shuffle,regenerate,empty or not,
 etc.
 
'''
import time
from BoardD import tile
from Generator import board, aiStats

class Rack:
 
    TRAY_SIZE = 7
    
    initialized = False
    
    @staticmethod
    def initialize():
        Rack.initialized = True
        #Rack.aiStats = aiStats.AIStats()
    
    '''
    Initialize a new rack and score for a player.
    '''
    '''
    def __init__(self, name, theBoard, theBag):
    changed by tanmay 11/28/2016
    '''
            
    def __init__(self, board_Obj = None):
        if not Rack.initialized:
            Rack.initialize()
        
       
        self.score = 0
        #self.name = name
        self.theBoard = board_Obj
        self.tray = board_Obj.tray
        self.lastScore = 0
        
        #   Start with a full set of tiles.
        '''
        they are providing us tray every time so no need to grab as
        '''
        #self.grab()
    
    '''
    Returns false if the rack tries to draw new tiles and none exist in the bag (i.e., the game is finished).
    True if either tiles were successfully removed, or the tray isn't empty.
    '''
    def grab(self):
        if not self.theBag.isEmpty():
            #   Attempt to withdraw the needed number of tiles.
            numNeeded = Rack.TRAY_SIZE-len(self.tray)
            for i in range(numNeeded):
                newTile = self.theBag.grab()
                if newTile != None:
                    self.tray.append(newTile)
        
        #   If the bag was empty and our tray is empty, signal that play is over.
        elif len(self.tray) == 0:
            return False
    
        return True
    
    '''
    This function assumes the word was placed on the board by some mechanism by some tentative tiles.
    The board then plays the tentative tiles, locking them if they work, returning them as a list if they don't.
    In the latter case, put the words back on the tray, in the former add the points and grab new tiles.
    
    Returns True if the move was executed successfully (thus ending our turn) and False if it wasn't,
    forcing us to try again.
    '''
    def Play(self, firstTurn):
        (tiles,points, inPlay, board) = self.theBoard.play(firstTurn)
        #   The play was successful, add the points to our score and grab new tiles
        # tanmay changed 11/29/2016
        #  if tiles == None and points >= 0
        if tiles == None and points >= 0 :
            self.score += points
            self.lastScore = points
            #gameContinues = self.grab()
            #if gameContinues:
            return (True,inPlay,board)
            #else:
            #    return ("END",inPlay,board)
        
        #   Play didn't work, put the
        elif tiles != None:
            #   take the tiles back
            for t in tiles:
                self.take(t)
                assert len(self.tray) <= Rack.TRAY_SIZE
            
            return (False,inPlay,board)
        #   Simple case, we tried to play, but there were no tentative tiles!
        else:
            return (False,inPlay,board)
    
    '''
    Take a tile previously held, should only be called for returning tentative pieces to the tray.
    '''
    def take(self, tile):
        assert(len(self.tray) < Rack.TRAY_SIZE)
        if tile.isBlank:
            tile.letter = ' '
        self.tray.append(tile)