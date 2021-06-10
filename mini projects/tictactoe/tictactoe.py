# Text Based Tic Tac Toe game
# Author: Thulam Tran
# Year 2020

import random

def placeholder():
    '''
    () -> string
    
    Returns placeholder string.
    '''
    return "#"

def tictactoe():
    '''
    () -> None
    
    Game select for Tic Tac Toe game.
    '''
    print("Tic Tac Toe Game by Thulam T.\n")
    end=False
    while not end:
        gameSelect=input("Enter A for 1 player mode, enter B for 2 player mode, otherwise quit game: ").upper()
        if (gameSelect=="A"):
            print("ONE PLAYER MODE\n")
            onePlayer()
            end=True
        elif(gameSelect=="B"):
            print("TWO PLAYER MODE\n")
            twoPlayers()
            end=True
        else:
            end=True

def onePlayer():
    '''
    () -> None
    
    1 Player Tic Tac Toe game.
    '''
    board=[[placeholder(),placeholder(),placeholder()], [placeholder(),placeholder(),placeholder()], [placeholder(),placeholder(),placeholder()]]
    printBoard(board)
    done=False
    while not done:
        player1(board)
                
        printBoard(board)
        if(validateBoard(board)):
            done=True
            break

        oCheck=True
        while oCheck:
            rowO=random.randint(0,2)
            colO=random.randint(0,2)

            if(board[rowO][colO]==placeholder()):
                board[rowO][colO]="O"
                oCheck=False

        printBoard(board)
        
        if(validateBoard(board)):
            done=True
            break
        
def twoPlayers():
    '''
    () -> None
    
    2 Player Tic Tac Toe game.
    '''
    board=[[placeholder(),placeholder(),placeholder()],[placeholder(),placeholder(),placeholder()],[placeholder(),placeholder(),placeholder()]]
    printBoard(board)
    done=False
    while not done:
        player1(board)
                
        printBoard(board)
        if(validateBoard(board)):
            done=True
            break

        player2(board)
        printBoard(board)
        
        if(validateBoard(board)):
            done=True
            break
        
def player1(board):
    '''
    (2-D List) -> None
    Preconditions: 2-D List size is 3x3 and objects within are either placeholder() string, "O", or "X"
    
    Drawing X on 3x3 board.
    '''
    xCheck=True
    while xCheck:
        rowX=(input("X: enter row "))
        colX=(input("X: enter column "))
        
        if(rowX.isnumeric() and colX.isnumeric()):
            rowX=int(rowX)
            colX=int(colX)
            if(rowX>2 or rowX<0 or colX>2 or colX<0):
                print("Only accept inputs from 0-2, enter again\n")
                
            elif(board[rowX][colX]=="O" or board[rowX][colX]=="X"):
                print("Space already occupied, enter again\n")
            else:
                board[rowX][colX]="X"
                xCheck=False
        else:
            print("Invalid characters, only digits from 0-2, enter again\n")

def player2(board):
    '''
    (2-D List) -> None
    Preconditions: 2-D List size is 3x3 and objects within are either placeholder() string, "O", or "X"
    
    Drawing O on 3x3 board.
    '''
    oCheck=True
    while oCheck:
        rowO=(input("O: enter row "))
        colO=(input("O: enter column "))

        if(rowO.isnumeric() and colO.isnumeric()):
            rowO=int(rowO)
            colO=int(colO)
            if(rowO>2 or rowO<0 or colO>2 or colO<0):
                print("Only accept inputs from 0-2, enter again\n")

            elif(board[rowO][colO]=="O" or board[rowO][colO]=="X"):
                print("Space already occupied, enter again\n")
            else:
                board[rowO][colO]="O"
                oCheck=False

        else:
            print("Invalid characters, only digits from 0-2, enter again\n")

def validateBoard(board):
    '''
    (2-D List) -> boolean
    Preconditions: 2-D List size is 3x3 and objects within are either placeholder() string, "O", or "X"
    
    Returns True if board is is filled or a player has a line of 3, returns False otherwise.
    '''
    for i in range(len(board)):
        if(board[i][0] != placeholder() and board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][1]==board[i][2]):
            print ("WINNER "+board[i][0])
            return True
        elif(board[0][i] != placeholder() and board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[1][i]==board[2][i]):
            print ("WINNER "+board[0][i])
            return True
        elif(i==len(board)-1 and board[1][1]!=placeholder()):
            if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[1][1]==board[2][2]):
                print ("WINNER "+board[0][0])
                return True
            elif(board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[1][1]==board[2][0]):
                print ("WINNER "+board[0][2])
                return True
    if (fullBoard(board)):
        print ("TIE")
        return True
    
    return False


def printBoard(board):
    '''
    (2-D List) -> None
    Preconditions: 2-D List size is 3x3 and objects within are either placeholder() string, "O", or "X"
    
    Prints board rows one by one.
    '''
    print(board[0])
    print(board[1])
    print(board[2])
    print("")
    
def fullBoard(board):
    '''
    (2-D List) -> boolean
    Preconditions: 2-D List size is 3x3 and objects within are either placeholder() string, "O", or "X"
    
    Returns True if board is is filled with either "X" or "O", returns False otherwise.
    '''
    row0 = ( board[0][0]=="X" or  board[0][0]=="O")  and ( board[0][1]=="X" or  board[0][1]=="O") and ( board[0][2]=="X" or  board[0][2]=="O")
    row1 = ( board[1][0]=="X" or  board[1][0]=="O")  and ( board[1][1]=="X" or  board[1][1]=="O") and ( board[1][2]=="X" or  board[1][2]=="O")
    row2 = ( board[2][0]=="X" or  board[2][0]=="O")  and ( board[1][1]=="X" or  board[1][1]=="O") and ( board[1][2]=="X" or  board[1][2]=="O")
    return (row0 and row1 and row2)


def play():
    '''
    () -> None
    
    Replay or quit Tic Tac Toe game.
    '''
    end=False
    while not end:
        gameEnd=input("Do you still want to keep playing? Enter Y for yes, otherwise quit game: ").upper()
        if (gameEnd=="Y"):
            tictactoe()
        else:
            print("Thanks for playing!")
            end=True
            
tictactoe()
play()
