# -*- coding: utf-8 -*-
'''

'''
from BoardD import tile as ts

class TileStack:
    
    MAX_STACK_HEIGHT = 5
    
    def __init__(self):
        self.tileStack = []
    
    #   Method for pushing a tile on tileStack.
    def push(self, tile_temp):
        self.tileStack.append(tile_temp)
    
    #   Method for remove a tile 
    
    #   Method to check whether the tileStack is empty or not.
    def isEmpty(self):
        return (self.tileStack == [])
    
    #   Method for popping a tile from tileStack.
    def pop(self):
        return self.tileStack.pop()
    
    #   Method to get the top of the tileStack.
    def topOfTilestack(self):
        return len(self.tileStack)
    
    def __str__(self):
        return str(self.tileStack)
    
    #   Method to get the tileStack.
    def gettileStack(self):
        return self.tileStack
    
    # Method to check whether adding of more tiles to tileStack is possible or not.
    def canAddTile(self):
        if (self.tileStack < self.MAX_STACK_HEIGHT):
            return True
        return False

if __name__ == "__main__":
    tstack = TileStack()
    
    tstack.push("A")
    tstack.push("B")
    tstack.push("C")
    tstack.push("D")
    tstack.push("E")
    
    print(tstack)
    
    tstack.pop()
    
    print(tstack)
    
    print(tstack.topOfTilestack())