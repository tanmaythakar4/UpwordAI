# -*- coding: utf-8 -*-
'''

'''
from BoardD import tile

class TileStack:
        
    def __init__(self, maxStackHeight = 5):
        self.maxStackHeight = maxStackHeight
        self.tiles = []
        self.tileStack = []
    
    
    #   Method to check whether the tileStack is empty or not.
    def isEmpty(self):
        if len(self.tileStack) == 0:
            return True
        else:
            return False
        #return (self.tileStack == [])
    
    def isFull(self):
        if len(self.tileStack) == self.maxStackHeight:
            return True
        else:
            return False
    
    #   Method for pushing a tile on tileStack.
    def push(self, tileStack):
        if not self.isFull():
            self.tileStack.append(tileStack)
            return "OK"
        else:
            return "ERR_STACK_FULL"
    
    #   Method for popping a tile from tileStack.
    def pop(self):
        if not self.isEmpty():
            output = self.tileStack(len(self.tileStack) - 1)
            del self.tileStack[len(self.tileStack) - 1]
            return output, "OK"
        else:
            return "ERR_STACK_EMPTY"
    
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