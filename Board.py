class Board:
    def __init__(self, row=6, col=7):
        #min board size is 4x4
        if( row < 4 ):
            print("Sorry the minimum is 4 rows")
            row = 4
        if( col < 4 ):
            print("Sorry the minimum is 4 cols")
            col = 4

        #setters
        self.row = row
        self.col = col
        self.win = False
        self.winner = None

        #Board is populated with No Player [None], Player 1 [0], and Player 2 [1]
        self.board = []
        for x in range(self.row):
            hold_row = []
            for y in range(self.col):
                hold_row += [None]
            self.board += [hold_row]
    
    def __str__(self):
        hold_row = ""
        hold_board=""
        for row in range(self.row):
            hold_row = "| "
            for col in range(self.col):
                curr_pos = self.board[row][col]
                if( curr_pos == "0" ):
                    hold_row += "O "
                elif( curr_pos == "1" ):
                    hold_row += "X "
                else: 
                    hold_row += "_ "
            hold_row += "|\n"
            hold_board += hold_row

        hold_row = "| "
        for col in range(self.col):
            hold_row += str(col) + " "   
        hold_row += "|\n"
        hold_board += hold_row
        return hold_board
    
    def checkWin(self):
        for row in range( self.row ):
            for col in range( self.col ):
                #four in a row
                if( col+3 < self.col ): 
                    one, two, three, four = self.board[row][col], self.board[row][col+1], self.board[row][col+2], self.board[row][col+3]
                    if( one==two and two==three and three==four and four != None ):
                        self.win=True
                        self.winner=self.board[row][col]
                #four in a column
                if( row+3 < self.row ):
                    one, two, three, four = self.board[row][col], self.board[row+1][col], self.board[row+2][col], self.board[row+3][col]
                    if( one==two and two==three and three==four and four != None ):
                        self.win=True
                        self.winner=self.board[row][col]
                #four diagonally bottom-up, right
                if( col+3 < self.col and row-3 > 0 ):
                    one, two, three, four = self.board[row][col], self.board[row-1][col+1], self.board[row-2][col+2], self.board[row-3][col+3]
                    if( one==two and two==three and three==four and four != None ):
                        self.win=True
                        self.winner=self.board[row][col]
                #four diagonally bottom-up, left
                if( col-3 > 0 and row-3 > 0 ):
                    one, two, three, four = self.board[row][col], self.board[row-1][col-1], self.board[row-2][col-2], self.board[row-3][col-3]
                    if( one==two and two==three and three==four and four != None ):
                        self.win=True
                        self.winner=self.board[row][col]
        if( self.win==True ):
            print("Congratulations on winning!")
        return self.win

    #player places checker piece into columm
    #returns true if piece is placed, false if not placed
    def place(self, player, col):
        #reject col if not on board
        if( col < 0 or col > self.col ):
            print("This column is not on the board, please choose another")
            return False
        #checks if the column is full
        if( self.board[0][col] != None ):
            print("This column is full, please choose another")
            return False
        else:
            #check from bottom row up
            for row in range(self.row-1,-1,-1):
                curr_pos = self.board[row][col]
                if( curr_pos == None ):
                    self.board[row][col] = str(player)
                    return True
    
