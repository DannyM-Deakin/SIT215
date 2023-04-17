import pygame
import sys
import time

# Reads maze configuration from input.txt file
with open('Assignment 1 Files\input.txt') as f:
        maze = [list(line.strip()) for line in f]
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

pygame.init()
size = width, height = 1920, 1080

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("Assignment 1 Files\OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("Assignment 1 Files\OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("Assignment 1 Files\OpenSans-Regular.ttf", 42)

start = False
boardSize = len(maze)-1
clock = pygame.time.Clock()
tile_size = 8*boardSize
tile_origin = (tile_size, tile_size)
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
                rect = pygame.Rect(
                    tile_origin[0] + newC * tile_size,
                    tile_origin[1] + newR * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)
                move = moveFont.render(str(maze[newR][newC]), True, red)
                moveRect = move.get_rect()
                moveRect.center = rect.center
                screen.blit(move, moveRect)
                pygame.display.update()
                pygame.time.delay(100)
                return True
    return False

def drawMaze():
    # Draw game board
         # Draw game board
        
        for i in range(0,boardSize+1):
            for j in range(0,boardSize):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)
                if maze[i][j] != "*":
                    move = moveFont.render(str(maze[i][j]), True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Title Screen, checks to make sure solution found before displaying.
    if not start:
        
        # Draw title
        title = largeFont.render("Maze", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw button
        beginButton = pygame.Rect((width / 4), (height / 1.05), width / 2, 50)
        begin = mediumFont.render("Begin", True, black)
        beginRect = begin.get_rect()
        beginRect.center = beginButton.center
        pygame.draw.rect(screen, white, beginButton)
        screen.blit(begin, beginRect)


        # Draw game board
        drawMaze()


        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if beginButton.collidepoint(mouse):
                time.sleep(0.2)
                start = True


    else:
        drawMaze()
        findStart()
        pygame.time.delay(500)

 
    pygame.display.flip()
    clock.tick(30)
