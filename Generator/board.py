# -*- coding: utf-8 -*-

'''
it will use to genearte next move and handle the board so methos will be

to generate board String[][]
getstatus from rack and board
generateword
validate(word,score,timing)
check upwordrules

'''
import dictionary, time
import BoardD.tile as tile
class Board:
    
    Debug_errors = True
    DICTIONARY_FILE = '../dictionary.txt'
    BOARD_SIZE = 10
    START_POSITION = [(4,4),(4,5),(5,4),(5,5)]
                      
    def __init__(self):
        self.tiles = []
        self.tray = []
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
    Resets all timers
    '''
    def resetAllMetrics(self):
        self.scoringTime = 0
        self.crosswordValidationTime = 0
        self.dictionaryValidationTime = 0
        self.quickValidationTime = 0
        self.invalidWordCount = 0
        self.crosswordErrors = 0
        
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
        startTime = time.time()
        if self.Debug_errors:
         self.maxWordTimeStamp = startTime
         self.validationTime = 0
         #self.theBoard.dictionary.resetLookupTime()
         self.resetAllMetrics()
         self.theWordsConsidered = ""
         self.maxScore = -1
        
        
        
        
        self.theWordsConsidered = ""
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
                                
                        
        print("seeds",seeds)
            
        (maxpoint,maxtile) = -1000,None
        self.numValidations = 0
        self.numRawValidations = 0
    
        
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
        print(len(tileSlots))
                            
        for tileslot in tileSlots:
            emptySlots = []
            wordBuilt = []
            slotPosition= {}
            for (x,y) , tile in tileslot:
                slotPosition[(x,y)] = True
                if tile == None:
                    emptySlots.append((x,y))
                wordBuilt.append(tile)
            #print("execturn=(emptyslot)==",emptySlots)
            #print("execturn=(wordBuilt)==",wordBuilt)
            #print("tray====",len(self.tray),isFirstMove)
            
            
            (point, tiles, blankes) = self.tryallPermutation(isFirstMove,wordBuilt,emptySlots,self.tray) 
             
            
            # NOw we have best tile so play them 
             #
             #TO BE CONTINUE
        '''
        Here we have given a set of position ,this function will try all the combination of tray tiles 
        that could be inserted and return the score and tile placed of the highest scoring combination by asking the board
        
        word = wordbuilt
        slots = emptyslots 
        '''
    def tryallPermutation(self,isFirstMove, word, slots, traytiles, tilesPlaced = []):
        print("tryallPermutationord",slots)
        if len(slots) == 0:
            if self.Debug_errors:
                startValidation = time.time()

            blankAssignment = []
            seedRatio = (-1, -1)
            
            # find a word before a validation
            i=0
            spelling= ""
            print("word",word)
            for tile in word:
                if tile != None:
                    spelling += tile.letter
                    print("spelling",spelling);
                    
                else:
                    #spelling += tilesplaced[i][1].letter
                    print("BBBBBBB",tilesPlaced[i][1].letter);
                    spelling += tilesPlaced[i][1].letter
                    i+=1
                  
            # if there no blank
            if not ' ' in spelling:
                if self.dictionaryf.isValid(spelling) or len(slots) == 1:
                    print("spelling233====",spelling);
                    if self.Debug_errors:
                            self.numValidations += 1
                            self.numRawValidations +=1
                            if self.numValidations % 10 == 0:
                                self.theWordsConsidered += "\n"
                       
                            self.theWordsConsidered += spelling + ","
                    
                    # validate the word
                    (score, dummy, seedRatio) = self.validateWords(isFirstMove, tilePlayed = tilesPlaced)
                    print("score, dummy, seedRatio=============================",score, dummy, seedRatio)
                else:
                    score = -1000
            else:
                # get all the assignments that orrespond to real word
                blankAssignment = self.dictionaryf.matchWithBlanks(spelling)
                rawValidation = 0
                if len(blankAssignment) >0:
                    for assignmensts in blankAssignment:
                        
                        #Apply assignment to the blank
                        i = 0
                        assignedSpelling = ''
                        for (x,y),tile in tilesPlaced: 
                            if tile.isBlank:
                                tile.letter = assignmensts[i]
                                i += 1
                            assignedSpelling += tile.letter
                        if self.Debug_errors:
                            self.numValidations += 1
                            rawValidation = 1
                            if self.numValidations % 10 == 0:
                                self.theWordsConsidered += "\n"
                       
                            self.theWordsConsidered += assignedSpelling + ", "
                        
                        # validate the word
                        (score, dummy, seedRatio) = self.validateWords(isFirstMove, tilePlayed = tilesPlaced)
                        
                        if score>0:
                            blankAssignment = assignmensts
                            break
                else:
                    score = -1000            
                 
                if self.Debug_errors:
                    self.numRawValidations += rawValidation
                    
            if self.Debug_errors:
                endValidation = time.time()
                self.validationTime += endValidation-startValidation
            '''
                   heuristic function after first word generate
                   '''
            
                #score += self.heuristic.adjust(trayTiles = self.tray, playTiles = tilesPlaced, seedRatio = seedRatio)    
                
            if score > self.maxScore:
                self.maxScore = score
                self.maxWordTimeStamp = time.time()
                  
                
            print("score, tilesPlaced, blankAssignment===", score, tilesPlaced, blankAssignment)      
            return (score, tilesPlaced, blankAssignment)            
        else:
            print("HELLLLO")
            slot = slots[0]
            
            print("slot",slot);
            (maxScore, maxTiles, maxBlanks) = (-1000, None, None)
            for tile in traytiles:
                    print(tile.letter);
                    newTilesPlaced = tilesPlaced[:]
                    newTilesPlaced.append((slot, tile))
                    trayRemaining = traytiles[:]
                    trayRemaining.remove(tile)
                    print("trayRemaining",len(trayRemaining))
                    print("Sloat[1:]",slots[1:])
                    (score,tilesTried,blankAssignment) = self.tryallPermutation(isFirstMove,word,slots[1:],trayRemaining,newTilesPlaced)
                    if score > maxScore:
                        maxScore, maxTiles, maxBlanks = score, tilesTried, blankAssignment
                    
            return (maxScore, maxTiles, maxBlanks)
    
 
            
      #puts a tile on board
    def setPiece(self, value ,tile):
          x = value[0]
          y = value[1]
          assert x>=0 and y>=0 and x < self.BOARD_SIZE and y < self.BOARD_SIZE
          assert self.tiles[x][y] == None
          self.tiles[x][y] = tile
      
    # Remove tiles if we know already where they are
    def pullTilesFast(self,tilesPlayed):
        if tilesPlayed != None:
            for (x,y),tile in tilesPlayed:
                assert self.tiles[x][y] != None
                assert self.tiles[x][y].locked == False
                if self.tiles[x][y].isBlank:
                    self.tiles[x][y].letter = ' '
                
                self.tiles[x][y] = None
 
    '''
    Calculates the number of seeds and number of tiles and returns them as a tuple
    '''
    def calculateSeedRatio(self):
        numSeeds = 0
        numTiles = 0
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if self.tiles[x][y] != None:
                    numTiles += 1
                elif ((x > 0 and self.tiles[x-1][y] != None) or
                      (x < self.BOARD_SIZE-1 and self.tiles[x+1][y] != None) or
                      (y > 0 and self.tiles[x][y-1] != None) or
                      (y < self.BOARD_SIZE-1 and self.tiles[x][y+1] != None)):
                    numSeeds += 1
                
        
        #If the board is empty, then there is one seed        
        if numSeeds == 0:
            numSeeds = 1
            
        return (numSeeds, numTiles)

    '''
     Check if all the word played are valid or not and calculate the score too 
     used for two purpose
     (1) as we are calling the function play() after that
     (2) Independently for the AI verification check
     
     '''
     
    def validateWords(self, isFirstMove , tilePlayed= None, inPlay= None ):
         if self.Debug_errors:
             startTime = time.time()
             
         wordsBuilt = [] # a list contain the ((x,y),tile)
         
         # IF we are doing this step seprstly from noramal  play , put the tils on the run
         # the Algorithm (normalplay and algorithm play)
         
         if tilePlayed != None:
             inPlay = []
             for pos,tile in tilePlayed:
                 self.setPiece(pos,tile)
                 inPlay.append(pos)
                 
         if self.Debug_errors:
             crosswordTimeStart = time.time()
             self.quickValidationTime += crosswordTimeStart - startTime
             
         seedRatio = self.calculateSeedRatio()
             
         # calculate the seed ratio to return to for heuristics
         # nilay to be continue
         
         # keep a list of 'words built'    
         '''
         Algorithm description: We can find all the crosswords by going through all the rows
         and columns which contain tentative tiles. These are potential 'words'. Then we start
         with a tentative tile on that row/col and expand outward in both directions until we
         hit a blank on both ends. That becomes the 'word' created. Finally, we go through the
         words and confirm that a previously played tile was used
         '''
  
          # first build a list of possible word rows and cols ( include x and y  for first seed  )
         rowsToCheck = []
         colsToCheck = []
         colset = []
         rowset = []
         for (x,y) in inPlay:
              if not x in colset:
                  colset.append(x)
                  colsToCheck.append((x,y))
              if not y in rowset:
                  rowset.append(y)
                  rowsToCheck.append((x,y))
                  
                  
         #Build Word alongs the row
         
         for (col,row) in rowsToCheck:
             
             # build left
             left = col
             while left-1 >=0 and self.tiles[left-1][row] != None:
                 left -=1
                 
             # build right
             right = col
             while right+1 < self.BOARD_SIZE and self.tiles[right+1][row] != None:
                 right +=1
             
             # add the word if it has atleast two letter
             if left != right:
                 wordsBuilt.append([((x,row),self.tiles[x][row]) for x in range(left , right+1)])
         
         
         
           #build word alongs the cols
         
         for (col,row) in colsToCheck:
             
             # build up
             up = row
             while up-1 >=0 and self.tiles[up-1][row] != None:
                 up -=1
                 
             # build down
             down = row
             while down+1 < self.BOARD_SIZE and self.tiles[down+1][row] != None:
                 down +=1
             
             # add the word if it has atleast two letter
             if up != down:
                 wordsBuilt.append([((col,y),self.tiles[col][y]) for y in range(up , down+1)])
            
         crossWordMade = False
         for word in wordsBuilt:
               for ((x,y), tile) in word:
                   if tile.locked:
                       crossWordMade = True
                
            
         if self.Debug_errors:
             validationTimeStart = time.time()
             self.crosswordValidationTime += time.time() - crosswordTimeStart

            
         if not crossWordMade and not isFirstMove:
               # fail , word is not attached
               if self.Debug_errors:
                   self.crosswordErrors += 1
                   if tilePlayed == None:
                       print("word placed must formed one crossword")
               self.pullTilesFast(tilePlayed)
               return (-1, None, seedRatio)  
              
            # Step SIx --- To check all the words in wordbuilt are in dictionary
            
         spellings = []
         for word in wordsBuilt:
                spelling = ""
                for (pos,tile) in word:
                    spelling += tile.letter
                spellings.append(spelling)
                if not self.dictionaryf.isValid(spelling):
                    # fail word is not in dictionary
                    if self.Debug_errors:
                        self.invalidWordCount += 1
                    if tilesPlayed == None:
                        print("isn't in the dictionary")
                self.pullTilesFast(tilesPlayed)
                return (-1, None, seedRatio)
               
         if self.DEBUG_ERRORS:
            scoringTimeStart = time.time()
            self.dictionaryValidationTime += time.time() - validationTimeStart

                
         # calculate the score
         totalScore = 0
             
         '''
              here might possible we have to add or delete the policy according to Upwordsss
             
             #(1) 50 point bonus for using all tray
                    
         '''
            
         if len(inPlay) == len(self.tray):
                totalScore += 50
                
         wordScore = {} # contain word score for all words
         wordScoreOptimize = [] #stores words where word bonuses are conflicted
         i = 0
         for word in wordBuilt:
                wordScore[i] = 0
                wordBonus = 1
                marks=[] # we get bonus for only one word;
                for (x,y), tile in word:
                    letterScore = 1 # here we assume that all the letter have equal value
                    # bonus logic if exist
                    wordScore[i] += letterScore
                wordScore[i] *= wordBonus
                i += 1
                
          #if are conflict then all go through all permutation to retrive the highest possible score
          #to be continue

          # now add all the word score to get total score
         for score in wordScore.values():
             totalScore += score
            
         if Board.Debug_errors:
               self.scoringtime = time.time() - scoringTimeStart

            # pull the tiles if we put that in this call
            #left
         
         return (totalScore, spellings, seedRatio)
         
                    
 #TEST        
if __name__ == '__main__':    
  boards = Board()
  #Testing
  boards.BOARD_SIZE = 5
  boards.tiles = [[None,None,None,None,None],[None,None,tile.Tile('G'),None,None],[None,None,tile.Tile('O'),None,None],
                      [None,None,tile.Tile('A'),None,None],[None,None,tile.Tile('L'),None,None]]
                      
  boards.tray = [tile.Tile('B'),tile.Tile('C'),tile.Tile('D')]
        
  boards.executeMove(False)    
                    