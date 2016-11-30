# -*- coding: utf-8 -*-

import board, bag

def main():
    USERDATA = loadUser()


def runGame(USERDATA):
    theBag = bag.Bag()
    theBoard = board.Board()
        

'''
This function resolves the action of the player to try to pick up a tile. Two Situations:
a) The player has a piece in hand:
    - If it's on the board, attempt to place the piece there. If it doesn't work,
      do nothing. If it does work, empty the hand and update the board.
    - If it's on the tray, swap positions and set the hand to none.
b) The player doesn't have a piece in hand:
    - If it's on the board and the pice is not locked, return it to the tray (at the end)
    - If it's on the tray, highlight that piece and put it in hand.
'''

def tileGrab(x, y, hand, theBoard):
    