import random
import pygame
from tictactoe import *

#tictactoe()
#play()

pygame.init()

#Create new window of size WIDTH and HEIGHT constants, and window name
WIDTH, HEIGHT = 500, 500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

#main game loop
def main():
    running=True
    while running:
        for event in pygame.event.get():
            #Exit event when exiting window
            if event.type==pygame.QUIT:
                running=False
        
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(0,0,255),(250,250),75)
        pygame.display.flip()
    #Exit pygame
    pygame.quit()

if __name__ == "__main__":
    main()