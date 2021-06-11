# Text Based Connect 4 game
# Author: Thulam Tran
# Year 2021

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

def fullBoard(board):
    '''
    (2-D List) -> boolean
    Preconditions: 2-D List size is 6x7 and objects within are either PLACEHOLDER string, "R", or "Y", icon is a character.
    
    Returns True if top row has no placeholders left, i.e. the board is full, False otherwise.
    '''
    if (board[0].count(PLACEHOLDER)==0):
        print("BOARD IS FULL")
        print("GAME OVER")
        return True
    return False

def horizontalConnect(board, icon):
    '''
    (2-D List, icon) -> boolean
    Preconditions: 2-D List size is 6x7 and objects within are either PLACEHOLDER string, "R", or "Y", icon is a character.
    
    Returns True if icon has horizontal connection of 4, False otherwise.
    '''
    for i in range(len(board)):
        for j in range(0,4):
            selection4=[board[i][j],board[i][j+1],board[i][j+2],board[i][j+3]]
            if selection4.count(icon)==4:
                return True
    return False
def verticalConnect(board, icon):
    '''
    (2-D List, icon) -> boolean
    Preconditions: 2-D List size is 6x7 and objects within are either PLACEHOLDER string, "R", or "Y", icon is a character.
    
    Returns True if icon has vertical connection of 4, False otherwise.
    '''
    for i in range(7):
        for j in range(0,3):
            selection4=[board[j][i],board[j+1][i],board[j+2][i],board[j+3][i]]
            if selection4.count(icon)==4:
                return True
    return False
def checkConnect(board, icon):
    '''
    (2-D List, icon) -> boolean
    Preconditions: 2-D List size is 6x7 and objects within are either PLACEHOLDER string, "R", or "Y", icon is a character.
    
    Returns True if icon has a connection of 4, False otherwise.
    '''
    if(horizontalConnect(board, icon) or verticalConnect(board, icon)):
        print(icon,"WINNER")
        print("GAME OVER")
        return True
    return False
    

board=initializeBoard()
printBoard(board)
done=False
while not done:
    dropCounter(board,"RED","R")
    if(checkConnect(board, "R") or fullBoard(board)):
        break

    dropCounter(board,"YELLOW","Y")
    if(checkConnect(board, "Y") or fullBoard(board)):
        break