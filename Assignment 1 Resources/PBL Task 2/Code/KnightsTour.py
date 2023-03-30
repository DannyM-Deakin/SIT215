boardSize = 8

def board():
    return solve()


def isSafe(x,y,board):
    # Checks if x and y are bigger than 0 and if they are not bigger than the board itself
    if(x>= 1 and y>=1 and x <= boardSize and y <= boardSize and board[x][y] == -1):
        return True
    return False

# Debugging function to print the board manually. Depreciated.
def printSol(board):
    for i in range(1, boardSize+1):
        for j in range(1, boardSize+1):
            print(board[i][j],end=' ')
        print()

def solve():
    board = [[-1 for i in range(boardSize+1)]for i in range(boardSize+1)]

    moveX = [2, 1, -1, -2, -2, -1, 1, 2] # All possible moves a knight can do left or right
    moveY = [1, 2, 2, 1, -1, -2, -2, -1] # All possible moves a knight can do up or down

    board[1][1] = 0 # First Position for knight (This can be anywhere)

    # This checks to see if a solution exists else prints the solution
    if(not solveCheck(board, 1, 1, moveX, moveY, 1)):
        return [[-1 for i in range(boardSize+1)]for i in range(boardSize+1)]
    else:
        return board
    

def solveCheck(board, x, y, moveX, moveY, pos):
    #Checks to see if current position is last sqaure
    if(pos == boardSize**2):
        return True
    
    #Iterates and selects a new move to be done, checks if move is safe
    for i in range(0,8):
        newX = x + moveX[i]
        newY = y + moveY[i]
        if(isSafe(newX, newY, board)):
            board[newX][newY] = pos #pos now current square
            #Checks next move that leads from this move ( backtracking )
            if(solveCheck(board, newX, newY, moveX, moveY, pos+1)):
                return True
            board[newX][newY] = -1  #Solution is found and we can set the knight to outside the board
    return False

