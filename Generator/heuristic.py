# -*- coding: utf-8 -*-
'''
this file contains a heuristics function which we will use to generate a more 
intelligent move

for example from wordsmith

--Tile Quantile Heuristic--
	
	The motivation behind this heuristic is that some letters are
	more useful than others. Useful letters should be given a penalty,
	so that their value isn't wasted on low-scoring words. Similarly,
	unuseful letters should be encouraged to be discarded at higher
	rates since they represent a liability in the tray.
	
	The way this heuristic works is that it uses letterPlay data 
	previously collected to determine the quantile difference (defaults to .5 mass)
	between the play for all letters is at that quantile, versus the
	value of that particular letter.
	
	The adjustment is then the sum of all quantile differences multiplied
	by the weight of the heuristic (again, defaulting to .5)
	
	What the algorithm means:
		-Low quantiles means a more conservative adjustment (accepting a lot of luck)
		-High quantiles means a more aggressive adjustment (hoping to get lucky)
		-The weight impacts the strength of this heuristic relative to the raw score
		 and/or other heuristics
	
   
   '''