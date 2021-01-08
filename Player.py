from Lib import copy
import math
class Player:
    #You can either be player 1 or player 2
    def __init__(self, playerTurn, ai=False):
        self.playerTurn = playerTurn
        self.winCount = 0
        self.ai = ai

    def ai_best(self, turn, board, depth):
        #avg = sum([x for x in range(board.col)])/board.col
        #arr = [math.exp(-(x-avg)**2/2)/(2*math.pi)**(1/2) for x in range(board.col)]
        arr = [0 for x in range(board.col)] 
        self.ai_place(turn, board, depth, arr)
        print(arr)
        return arr.index(max(arr))

    def ai_place(self, turn, board, depth, arr):
        if( depth > 0 ):
            for col in range(board.col):
                #place piece in col 
                deepBoard = copy.deepcopy(board)
                if( not deepBoard.place( turn, col ) ):
                    return -1
                
                #check if board is win
                if( deepBoard.win ):
                    print("here")
                    arr = [-100 for x in range(board.col) if x != col] 
                    return 100

                print( deepBoard, turn, depth, arr)
                
                arr[col] += self.ai_place( (turn+1)%2, deepBoard, depth-turn, arr )
        return 0                


        

