import pygame
from random import randint

if __name__ == '__main__':
    pygame.init()
    while running:
        start_main_window(pygame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
            