# -*- coding: utf-8 -*-
'''

'''
from BoardD import tile

class TileStack:
        
    def __init__(self, maxStackHeight = 5):
        self.maxStackHeight = maxStackHeight
        self.tileStack = []
    
    
    #   Method to check whether the tileStack is empty or not.
    def isEmpty(self):
        
        return (self.tileStack == [])
    
    def isFull(self):
        if len(self.tileStack) == self.maxStackHeight:
            return True
        else:
            return False
    
    #   Method for pushing a tile on tileStack.
    def push(self, tileTemp , before = -1):
        # add none if stack is not 1
        if before != -1 and before != 0:
            for i in range(before):
                self.tileStack.append(None)
                
        if not self.isFull():
            print(tileTemp.letter)
            self.tileStack.append(tileTemp)
        else:
            print("Stack FUlllll")
    
    #   Method for popping a tile from tileStack.
    def pop(self):
        if not self.isEmpty():
            output = self.tileStack.pop()
            return output
        else:
            return False
    
    #   Method to get the top of the tileStack.
    def topOfTilestack(self):
        if not self.isEmpty():
            return self.tileStack[len(self.tileStack) - 1]
    
  
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
    
    tstack.push(tile.Tile("A"))
    tstack.push(tile.Tile("B"))
    #tstack.push(tile.Tile("B"))
    #tstack.push(tile.Tile("D")) 
    #tstack.push(tile.Tile("E"))    
    print(tstack)
    
    tstack.pop()
    
    print(tstack.topOfTilestack().letter)
    if not tstack.isEmpty():
        print("NOTTT")
    tstack.pop()
    if tstack.isEmpty():
        print("YES")
