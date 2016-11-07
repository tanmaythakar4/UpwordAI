# -*- coding: utf-8 -*-

'''
it will use to genearte next move and handle the board so methos will be

to generate board String[][]
getstatus from rack and board
generateword
validate(word,score,timing)
check upwordrules

'''
import dictionary
class Board:
    
    Debug_errors = True
    DICTIONARY_FILE = '../dictionary.txt'
    BOARD_SIZE = 10
    START_POSITION = [(4,4),(4,5),(5,4),(5,5)]
                      
    def __init__(self):
        self.tiles = []
        for x in range(Board.BOARD_SIZE):
            self.tiles.append([])
            for y in range(Board.BOARD_SIZE):
                #here we are adding tile and some status but as of now we dont know 
                #which status will helpfull so it's tile only
                self.tiles[x].append((None))
        
        # Load the dictionary        
        self.dictionaryf = dictionary.Dictionary(Board.DICTIONARY_FILE)
        
        # load dictionary frequency usage (Working)
        #self.wordfreq = wordFrequency.wordFrequency()
        
        #self.resetBoard()
    
        
    '''
    now will proceed like first we will generate 
    (a) the tentative moves from executemove function() 
    (b) then we call play function which find the valid move (checking all the rules) return (tiles,point)
    (c) add that tile into board and add the point 
    and finally send this board to server , tiles[][]    
    
    
        
    '''
    '''
    (a) calculate the best move and place the tile on board and call play function (b)
    
    
    This is our basic algorithm where we start with the brute force .because if its not take
    longer time then this algorithm give high scoring move,
    Steps for (a)
    
    (1) First create a list of seed if its first turn then add START_POSITION or 
        else add all the blank and adjecent to the unoccupied tile into seed.
    (2)    
    
    '''
    
    def executeMove(self,isFirstMove):

        
        # calculate the time still working
        
        
        #(1)
        seeds = []

        if isFirstMove:
                seeds = START_POSITION
        else:
            for x in range(self.BOARD_SIZE):
                for y in range(self.BOARD_SIZE):
                    if self.tiles[x][y] != None:
                        
                        # go up and add tile till end
                        if y>0 and self.tiles[x][y-1] == None:
                            if (x,y-1) not in seeds:
                                seeds.append((x,y-1))
                                
                        # go down and add tile till end
                        if y< self.BOARD_SIZE - 1 and self.tiles[x][y+1] == None:
                            if (x,y+1) not in seeds:
                                seeds.append((x,y+1))
                    
                                
                        # go left and add tile till end
                        if x>0 and self.tiles[x-1][y] == None:
                            if (x-1,y) not in seeds:
                                seeds.append((x-1,y))
                                
                                
                        # go right and add tile till end
                        if x<self.BOARD_SIZE - 1 and self.tiles[x+1][y] == None:
                            if (x+1,y) not in seeds:
                                seeds.append((x+1,y))
                                
                        
        print(seeds)
            
        (maxpoint,maxtile) = -1000,None
        
        tileSlots = []
        # Step 2: add all the horizontal and verticle tiles where we can put the word
        #initiate tray (Remaining)
        for (x,y) in seeds:
            for lo in range(0,len(self.tray)):
                for hi in range(0,len(self.tray)-lo):
                    
                    #Horizontal tile slot
                     horz = [((x,y),self.tiles[x][y])]
                     loCount = 0
                     hiCount = 0
                     
                     #left
                     xPos,yPos = x-1,y
                     while xPos>0 and (loCount<lo or self.tiles[xPos][yPos] != None):
                         loCount += 1
                         horz.insert(0,((xPos,yPos),self.tiles[xPos][yPos]))
                         xPos -=1
                         
                     #RIGHT
                     xPos,yPos = x+1,y
                     while xPos<self.BOARD_SIZE-1 and (hiCount<hi or self.tiles[xPos][yPos] != None):
                         hiCount += 1
                         horz.append(((xPos,yPos),self.tiles[xPos][yPos]))
                         xPos +=1
                    
                        
                    #verticle tile slot
                     vert = [((x,y),self.tiles[x][y])]
                     loCount = 0
                     hiCount = 0
                     
                     #up
                     xPos,yPos = x,y-1
                     while yPos>0 and (loCount<lo or self.tiles[xPos][yPos] != None):
                         loCount += 1
                         vert.insert(0,((xPos,yPos),self.tiles[xPos][yPos]))
                         yPos -=1
                         
                     #down
                     xPos,yPos = x,y+1
                     while yPos<self.BOARD_SIZE-1 and (hiCount<hi or self.tiles[xPos][yPos] != None):
                         hiCount += 1
                         vert.append(((xPos,yPos),self.tiles[xPos][yPos]))
                         yPos +=1
                            
                             
                     tileSlots.append(horz)
                     tileSlots.append(vert)
       # print(tileSlots)
                     #print("horz",horz)
                     #print("vert",vert)
                    
                    
        #remove all the duplicates
        tileslotsmap = {}
        i = 0
        orignalsize = len(tileSlots)
        numEliminate = 0
        while i < len(tileSlots):
            slot = tileSlots[i]
            (x1,y1) = slot[0]
            (x2,y2) = slot[-1]
            
            if tileslotsmap.get((x1,y1,x2,y2),False):
                            tileSlots.pop(i)
                            numEliminate += 1
            else:
                tileslotsmap[x1,y1,x2,y2] = True
                i += 1
        print(tileSlots)
                            
        for tileslot in tileSlots:
            emptySlots = []
            wordBuilt = []
            slotPosition= {}
            for (x,y) , tile in tileslot:
                slotPosition[(x,y)] = True
                if tile == None:
                    emptySlots.append((x,y))
                wordBuilt.append(tile)
            print(emptySlots)
            print(wordBuilt)
            print(slotPosition)
            
            (point, tiles, blankes) = self.tryallPermutation(isFirstMove,wordBuilt,emptySlots,self.tray) 
             # NOw we have best tile so play them 
             #
             #TO BE CONTINUE
        '''
        Here we have given a set of position ,this function will try all the combination of tray tiles 
        that could be inserted and return the score and tile placed of the highrest scoring combinayion bybasking the board
        
        
        '''
    def tryallPermutation(self,isFirstMove, word, slots, traytiles, tilesPlaced = []):
        
        if len(slots) == 0:
            
            blankAssignment = []
            seedRation = (-1, -1)
            
            # find a word before a validation
            i=0
            spelling= ""
            for tile in word:
                if tile != None:
                    spelling += tile.letter
                    
                else:
                    #spelling += tilesplaced[i][1].letter
                    spelling += tilesplaced[i]
                    i+=1
                    
            # if there no blank
            if not ' ' in spelling:
                if self.dictionaryf.isValid(spelling) or len(slots) == 1:
                    
                    
                
                
                    
        
            
                    
                    
                    
 #TEST		
if __name__ == '__main__':	
  boards = Board()
  #Testing
  boards.BOARD_SIZE = 5
  boards.tiles = [[None,None,None,None,None],[None,None,'G',None,None],[None,None,'O',None,None],
                      [None,None,'A',None,None],[None,None,'L',None,None]]

                      
  boards.tray = ['B','C','D','E','F','G','H',]
        
  boards.executeMove(False)    
                    