import pygame
import sys
import time

import KnightsTour as kt

pygame.init()
size = width, height = 1920, 1080

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 42)

board = kt.board()
start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Title Screen, checks to make sure solution found before displaying.
    if not start:

        # Draw title
        title = largeFont.render("Knights Tour", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw size title
        size = largeFont.render("Size: " + str(kt.boardSize), True, white)
        sizeRect = size.get_rect()
        sizeRect.center = ((height / 4), 50)
        screen.blit(size, sizeRect)

        # Draw button
        beginButton = pygame.Rect((width / 4), (height / 2), width / 2, 50)
        begin = mediumFont.render("Begin", True, black)
        beginRect = begin.get_rect()
        beginRect.center = beginButton.center
        pygame.draw.rect(screen, white, beginButton)
        screen.blit(begin, beginRect)

        # Draw change size button
        sizeButton = pygame.Rect((width / 4), (height / 4), width / 2, 50)
        size = mediumFont.render("Change Size", True, black)
        sizeRect = size.get_rect()
        sizeRect.center = sizeButton.center
        pygame.draw.rect(screen, white, sizeButton)
        screen.blit(size, sizeRect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if sizeButton.collidepoint(mouse):
                time.sleep(0.2)
                kt.boardSize = int(input("New size: "))
                pygame.display.flip()
            elif beginButton.collidepoint(mouse):
                time.sleep(0.2)
                start = True
            

    else:

        # Draw game board
        tile_size = 10*kt.boardSize
        tile_origin = (tile_size, tile_size)
        for i in range(1,kt.boardSize+1):
            for j in range(1,kt.boardSize+1):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != -1:
                    move = moveFont.render(str(board[i][j]), True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)

            

    
        # Show title
        if board[1][1] != -1:
            title = f"Solved!"
        elif board[1][1] == -1:
            title = f"No Solution Found!"
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

         # Draw try again button
        againButton = pygame.Rect((width / 4), (height / 1.2), width / 2, 50)
        again = mediumFont.render("Again", True, black)
        againRect = again.get_rect()
        againRect.center = againButton.center
        pygame.draw.rect(screen, white, againButton)
        screen.blit(again, againRect)
        
        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if againButton.collidepoint(mouse):
                time.sleep(0.2)
                screen.fill(black)
                start = False
        
    pygame.display.flip()