# -*- coding: utf-8 -*-
'''
Initial distribution of tiles(letter)
This file maintain the bag of all characters or tiles which we are using through out the game.

Methods: 	--> Explanation

add() 		--> Initially add all tiles to the bag.
shuffle() 	--> Shuffule the bag.
grab()		--> Grab the tiles from the bag randomly.
isEmpty()	--> Check whether bag is empty or not.
putBack()	--> Swapping of tiles from the tray and bag. But if anybody uses swap then it will count 
				as one move. 
'''

class Bag:
	