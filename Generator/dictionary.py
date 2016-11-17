# -*- coding: utf-8 -*-
'''
this file contain methos to
generate a list of word from dictionary
find out word (here we can implement different different method for that 
like to find word from prefix or regular expression
)
validate word
setcount(wordcount part of statstic)
sequence of words

here I asume that before we start to run this we make another textfile from dictionary which contain 
 word and usage which we are going to maintain
 Question :
     Here worsmith have that textfile which contain count from last 1600 game so it's look good . can we use that file ?
     Or
    at inital stage we need to initialize with 0.
    
'''

import board,time
class Dictionary:
    
    def __init__(self,filename):
        
        '''
        list of words from text file
        '''
        self.words = {}
        self.lookuptime = 0
        dictionaryfile = open(filename,'r')
        for line in dictionaryfile:
            line = line.rstrip();
            tokens = line.split();
            if len(tokens) == 1:
                self.words[tokens[0]] = 1;
            else:
                self.words[tokens[0]] = int(tokens[1]) 
            
            
    
    def findlength(self):
        return self.words.__len__()
        
    def isValid(self,word):
        print(word)
        #print(word in self.words)
        # if you want to find out the time to find it's valid or not . it's for if it takes longer you can stop
        
        if board.Board.Debug_errors:
            start = time.time()
        if word in self.words:
            print("word============================================================",word)
            sucsess = True
        else:
            sucsess = False
            
        if board.Board.Debug_errors:
            timespent = time.time() - start
            self.lookuptime += timespent
        return sucsess
        
    # here we replace the blank with the word because they append the blanks to the adjecent blank from board
    
    def matchWithBlanks(self,word,assignment=[]):
        
        if not ' ' in word:
            if self.isValid(word):
                return [assignment]
            else:
                return []
        else:
            i = word.find(' ')
            blanAssignment = []
            for num in range(ord('A'),ord('Z')+1):
                char = chr(num)
                if i==0:
                    newword = char + word[1:]
                elif i == len(word)-1:
                    newword = word[i:-1] + char
                else:
                    newword = word[:i] + char + word[i+1:]
            newAssignment = assignment[:]
            newAssignment.append(char)
            results = self.matchWithBlanks(newword,newAssignment)
            for result in results:
                blanAssignment.append(result)
                
            return blanAssignment
            
    # set the word count in dictionary for future use
    
    def setUsage(self,word,usage):
        word = word.upper().rstrip()
        if self.isValid(word):
            self.words[word] = usage
            return True
        else:
            return False
            
    # Save the dictionary in file
    
    def savDictionory(self,fileName):
        with open(fileName,'W') as output:
            keyList = self.words.keys()
            keyList.sort()
            for w in keyList:
                output.write(W+"\t"+str(words[w]+"\n"))
                
                
    # reset the looktime we manage for game
    def resetLookup(self):
         self.lookuptime = 0
         
                
    

            
#TEST
if __name__ == '__main__':
    dic = Dictionary('../dictionary.txt')
    print(dic.findlength())
    
    print(dic.isValid(d))
    #print(dic.lookuptime)
     
    e = "HOME"
    #print(dic.isValid(e))
   # print(dic.lookuptime)
    
    
    #print(dic.matchWithBlanks('H'+' '+'M'+'E'))
    