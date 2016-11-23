# -*- coding: utf-8 -*-
'''
Initial distribution of tiles(letter)
This file maintain the bag of all characters or tiles which we are using through out the game.

Methods:     --> Explanation

add()         --> Initially add all tiles to the bag.
shuffle()     --> Shuffule the bag.
grab()        --> Grab the tiles from the bag randomly.
isEmpty()    --> Check whether bag is empty or not.
putBack()    --> Swapping of tiles from the tray and bag. But if anybody uses swap then it will count 
                as one move. 
'''

import random, tile

class Bag:

    def __init__(self):
        self.tiles = []

        # Add initial distribution of tiles.
        self.add('A', 7)
        self.add('B', 3)
        self.add('C', 4)
        self.add('D', 5)
        self.add('E', 8)
        self.add('F', 3)
        self.add('G', 3)
        self.add('H', 3)
        self.add('I', 7)
        self.add('J', 1)
        self.add('K', 2)
        self.add('L', 5)
        self.add('M', 5)
        self.add('N', 5)
        self.add('O', 7)
        self.add('P', 3)
        self.add('Qu', 1)
        self.add('R', 5)
        self.add('S', 6)
        self.add('T', 5)
        self.add('U', 5)
        self.add('V', 1)
        self.add('W', 2)
        self.add('X', 1)
        self.add('Y', 2)
        self.add('Z', 1)

        random.shuffle(self.tiles)

    # Add all the letter tiles into bag.
    def add(self, ltr, n):
        for i in range(n):
            self.tiles.append(tile.Tile(ltr))
    
    def shuffle(self):
        random.shuffle(self.tiles)

    def isEmpty(self):
        if len(self.tiles) == 0:
            return True
        return False

    def putBack(self, tile):
        self.tiles.append(tile)
  
    #   Grabs one tile from the bag and returns it (None if there aren't any left).
    def grab(self):
        if self.isEmpty():
            return None
        else:
            tile = self.tiles[0]
            self.tiles = self.tiles[1:]
            return tile
#TEST        
if __name__ == '__main__':    
    
    thebag = Bag()
    print(thebag.isEmpty())
    print(thebag.shuffle())
    print(thebag.grab())
    a = tile.Tile('M')
    print(thebag.putBack(a))