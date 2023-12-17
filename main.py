import pygame
from random import randint

from start_window.StartWindow import StartMenu


if __name__ == '__main__':
    pygame.init()
    StartMenu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
            