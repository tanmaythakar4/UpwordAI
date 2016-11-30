import requests
import json
from time import sleep
import BoardD.rack as rack 
import Generator.board as board

# Replace with the correct URL
url = "http://localhost:62027/api/"





def joinGame():

    myResponse = requests.get(url+"user")


    #print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.text)

        #print("The response contains {0} properties".format(len(jData)))

        for key in jData:
<<<<<<< HEAD
            print (str(key) + " : " + str(jData[key]))
=======
            print ()
>>>>>>> ab623f7ab618074f8bd2228c0fdf18f8635b5086
    else:
      # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return jData["Hash"],jData["ID"]

def getGameState(hash,ID):

    myResponse = requests.get(str(url+"game/"+str(ID)) , headers={"Hash":str(hash)})

    #print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.text)

        #print("The response contains {0} properties".format(len(jData)))

        for key in jData:
<<<<<<< HEAD
            print ()
=======
           print ()
>>>>>>> ab623f7ab618074f8bd2228c0fdf18f8635b5086
    else:
      # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return jData["Board"],jData["Letters"],jData["Turn"]

def sendMove(ID, hash, Board):
    d = {}
    d['Board'] = Board
    
    print("json.dumps(d)",str(json.dumps(d)))
    head = {"Hash": str(hash), "Move": str(json.dumps(d))}
    print("head=========",head)
    myResponse = requests.post(str(url + "game/" + str(ID)), headers=head)
    
    # print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
    if (myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.text)
<<<<<<< HEAD

=======
        
>>>>>>> ab623f7ab618074f8bd2228c0fdf18f8635b5086
        # print("The response contains {0} properties".format(len(jData)))
        for key in jData:
            print (str(key) + " : " + str(jData[key]))
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    #return jData["Board"], jData["Letters"], jData["Turn"]

def main():
    hash,ID = joinGame()
    print (hash,ID)
<<<<<<< HEAD
    Turn=0
=======
    # here we call the player file and send board,letter,turn
    tnp(0,True,hash,ID)
    #player.Player(ID,hash)
    
def tnp(Turn,IsFirstTurn,hash,ID):
>>>>>>> ab623f7ab618074f8bd2228c0fdf18f8635b5086
    while(Turn!=ID):
        BoardMain,Letters,Turn = getGameState(hash,ID)
        sleep(0.1)

<<<<<<< HEAD
    print(Letters)
    play =[]
    letter = input("Type a letter, an X, and a Y in form \"A 4 5\"")
    while (letter != ""):
        play = letter.split(' ')
        Board[0][int(play[1])][int(play[2])] = play[0]
        Board[1][int(play[1])][int(play[2])] = str(int(Board[1][int(play[1])][int(play[2])]) + 1)
        letter = input("Type a letter, an X, and a Y in form \"A 4 5\"")
    i = 4
    for letter in word:

        i=i+1
    print (Board)
    input()
    sendMove(ID, hash, Board, Letters, Turn)


=======
    theBoard = BoardMain[0]
    print("theBoard====",theBoard)
    board_Obj = board.Board(theBoard,Letters)
    rack_Obj = rack.Rack(board_Obj,Letters)
        
        
    playedMove = board_Obj.executeMove(IsFirstTurn) 

    if(playedMove):
            (success,inPlay,boardx) = rack_Obj.Play(IsFirstTurn) # here there are three option for sucess True,False,End
            print("successsuccess=========================",success)
            if success == "END":
                print("Picture abhi baki hey mere DOST")
            elif success:
                print("inPlay",inPlay)
                for (x,y) in inPlay:
                    print(boardx[x][y].letter)
                    BoardMain[0][x][y] = boardx[x][y].letter
                    BoardMain[1][x][y] = str(int(BoardMain[1][x][y]) + 1)
                    
                sendMove(ID, hash, BoardMain)
                tnp(0,False,hash,ID)
            else:
                print("AI think It has a move but it doesn't")
    
>>>>>>> ab623f7ab618074f8bd2228c0fdf18f8635b5086
main()