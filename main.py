import pygame
from map.Map import mapp

if __name__ == '__main__':
    pygame.init()
    running = True
    while running:
        mapp(pygame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
