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
            print ()
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
        
        # print("The response contains {0} properties".format(len(jData)))
       
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    #return jData["Board"], jData["Letters"], jData["Turn"]

def main():
    hash,ID = joinGame()
    print (hash,ID)
    # here we call the player file and send board,letter,turn
    tnp(0,True,hash,ID)
    #player.Player(ID,hash)
    
def tnp(Turn,IsFirstTurn,hash,ID):
    while(Turn!=ID):
        BoardMain,Letters,Turn = getGameState(hash,ID)
        sleep(0.1)

    theBoard = BoardMain[0]
    print("theBoard====",theBoard)
    board_Obj = board.Board(theBoard,Letters)
    rack_Obj = rack.Rack(board_Obj)
        
        
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
                #input("Sucsses wait for reply")    
                sendMove(ID, hash, BoardMain)
                
                tnp(0,False,hash,ID)
            else:
                print("AI think It has a move but it doesn't")
                sendMove(ID, hash, BoardMain)
    else:
        #input("Blank Move")
        sendMove(ID, hash, BoardMain)
    
main()