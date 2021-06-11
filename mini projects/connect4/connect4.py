PLACEHOLDER="#"

def initializeBoard():
    '''()->2D list
    
    Initializes 6x7 board with placeholders.
    '''
    board=[]
    for i in range(6):
        board+=[[PLACEHOLDER,PLACEHOLDER,PLACEHOLDER,PLACEHOLDER,PLACEHOLDER,PLACEHOLDER,PLACEHOLDER]]
    return board

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

def inputCol(player):
    '''
    (String) -> int
    Preconditions: User input is int between 1-7
    
    Player either Red or Yellow, user input for column to drop counter.
    '''
    Check=True
    while Check:
        col=(input(player+", enter column: "))
        
        if(col.isnumeric()):
            col=int(col)-1
            if(col>6 or col<0):
                print("Only accepts inputs from 1-7, enter again\n")
            else:
                RCheck=True
                return col
        else:
            print("Invalid characters, only digits from 1-7, enter again:\n")

def dropCounter(board,player,icon):
    '''
    (2-D List, String, String) -> None
    Preconditions: 2-D List size is 6x7 and objects within are either PLACEHOLDER string, "R", or "Y", icon is a character.
    
    Drawing character on 6x7 board based on players inputs.
    '''
    done=False
    while not done:
        colRed=inputCol(player)
        i=len(board)-1
        while i>=0:
            if(board[i][colRed]==PLACEHOLDER):
                board[i][colRed]=icon
                done=True
                break
            if(i==0):
                print("Column is full, choose another column:\n")
            i-=1
        printBoard(board)

board=initializeBoard()
printBoard(board)
done=False
while not done:
    dropCounter(board,"RED","R")
    dropCounter(board,"YELLOW","Y")