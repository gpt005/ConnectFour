from Board import Board
from Player import Player

class ConnectFour:
    def main():
        AI_DEPTH = 2 

        #Board Size
        boardChoice = input("Would you like a regular Connect 4 board? [y/n]: ").upper()
        board = None
        if( boardChoice == "Y" or boardChoice == "YES" ):
            print("Okay, a regular board it is")
            board = Board()
        else:
            boardChoiceRows = int(input("How many rows would you like? "))
            boardChoiceCols = int(input("How many cols would you like? "))
            board = Board(boardChoiceRows, boardChoiceCols)
        print(board) 
        
        #Choose First Player
        userTurn = input("Would you like to go first or second? [first/second]: ").upper()
        
        if( userTurn == "FIRST" ):
            userTurn = 0 
            print("Okay, you are going first")
        else:
            userTurn = 1
            print("Okay, you are going second")
       
        ai = input("Do you want to play against ai? [y/n]: ").upper()
        if( ai=="Y" or ai=="YES" ):
            ai = True
        else:
            ai = False

        playerOne = Player(0)
        playerTwo = Player(1, ai)
        
        while( not board.checkWin() ):
            if( playerTwo.ai and userTurn%2 == playerTwo.playerTurn ):
                print("Player " + str(userTurn%2+1) + " Turn" )
                board.place( playerTwo.playerTurn, playerTwo.ai_best(userTurn%2,board,AI_DEPTH) ) 
                
                userTurn+=1
                print(board)
            else:
                print("Player " + str(userTurn%2+1) + " Turn" )
                #place your checker
                colChoice = int(input("What column would you like to place your piece in? Column choices [0," + str(board.col-1) + "]: " ))
                while( colChoice >= board.col or colChoice < 0 ):
                    print("Invalid Column choice")
                    colChoice = int( input("What column would you like to place your piece in? " ))

                while( not board.place(userTurn%2, colChoice) ):
                    colChoice = int( input("What column would you like to place your piece in? " ))
                    
                userTurn+=1
                print(board)


    if __name__ == "__main__":
        main()
