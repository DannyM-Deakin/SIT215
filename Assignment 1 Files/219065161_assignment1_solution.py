"""
Solution for SIT215: Computational Intelligence Task 1
"""

          
def findStart():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S": # Starting position
                DFS(i,j)      


# Depth-First Search using starting pos and end pos
def DFS(r, c):
    # Check if we have reached the end point
    if maze[r][c] == "E":
        return True
    if maze[r][c-1] == " ":
        maze[r][c-1] = "*"
        if DFS(r-1, c):
            return True
        else:
            maze[r][c-1] == ' '
            DFS(r, c-1)
            return False

    if maze[r-1][c] == " ":
        maze[r-1][c] = "*"
        if DFS(r-1, c):
            return True
        else:
            maze[r-1][c] == ' '
            DFS(r-1,c)
            return False

    if maze[r+1][c] == " ":
        maze[r+1][c] == '*'
        if DFS(r+1, c):
            return True
        else:
            maze[r+1][c] == ' '
            DFS(r+1, c)
            return False


    if maze[r][c+1] == " ":
        maze[r][c+1] == '*'
        if DFS(r, c+1):
            return True
        else:
            maze[r][c+1] == ' '
            DFS(r, c+1)
            return False

    
    # If no path is found, return False
    return False




# Reads maze configuration from input.txt file
with open('Assignment 1 Files\input.txt') as f:
        maze = [list(line.strip()) for line in f]
        findStart()
        for row in maze:
            for char in row:
                if char == "*":
                    print("\033[91m{}\033[0m".format(char), end="")
                else:
                    print(char, end="")
            print()



    