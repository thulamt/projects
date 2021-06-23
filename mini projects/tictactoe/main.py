import random
import os
import pygame
pygame.init()


#tictactoe()
#play()

#constants
WIDTH, HEIGHT = 500, 500
GRAY=(128, 128, 128)
FPS=60

#FIX PATHS LATER TO NOT USE ABSOLUTE 
BOARD_IMAGE=pygame.image.load("C:/Users/thula/dev/projects/projects/mini projects/tictactoe/Assets/board_image.png") #os.path.join('Assets', 'board_image.png')
BOARD_IMAGE=pygame.transform.scale(BOARD_IMAGE,(500,500))
CIRCLE=pygame.image.load("C:/Users/thula/dev/projects/projects/mini projects/tictactoe/Assets/circle.png") #os.path.join('Assets', 'circle.png')
CIRCLE=pygame.transform.scale(CIRCLE,(100,100))
CROSS=pygame.image.load("C:/Users/thula/dev/projects/projects/mini projects/tictactoe/Assets/cross.png") #os.path.join('Assets', 'cross.png')
CROSS=pygame.transform.scale(CROSS,(100,100))

#Create new window of size WIDTH and HEIGHT constants, and window name
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

def draw_window():
    #Fill background color
    screen.fill(GRAY)

    #Draw board_image
    screen.blit(BOARD_IMAGE, (0,0))
    screen.blit(CIRCLE, (40,40))
    screen.blit(CROSS, (200,200))
    #update display
    pygame.display.update()

#main game loop
def main():
    clock=pygame.time.Clock()
    running=True
    while running:
        clock.tick(FPS) #cap FPS
        for event in pygame.event.get():
            #Exit event when exiting window
            if event.type==pygame.QUIT:
                running=False
        
        draw_window()

    #Exit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
