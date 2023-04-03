"""
Solution for SIT215: Computational Intelligence Task 1
"""



def findStart():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S": # Starting position
                DFS(maze, i,j, visited)      

def isSafe(maze, r, c, visited):
    if r >= 0 and r < len(maze) and c >= 0 and c < len(maze[0]):
        if maze[r][c] != "#" and not visited[r][c]:
            return True
    return False


# Depth-First Search using starting pos and end pos
def DFS(maze, r, c, visited):
    # Check if we have reached the end point
    if maze[r][c] == "E":
        return True
    
    visited[r][c] = True

    # Loop for north, south, east, and west sections
    for row, col in [(1,0),(-1,0),(0,1),(0,-1)]:
        newR, newC = r + row, c + col
        if isSafe(maze, newR, newC, visited):
            
            if DFS(maze, newR, newC, visited):
                maze[newR][newC] = "*"
                return True
    return False
    

# Reads maze configuration from input.txt file
with open('Assignment 1 Files\input.txt') as f:
        maze = [list(line.strip()) for line in f]
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        



