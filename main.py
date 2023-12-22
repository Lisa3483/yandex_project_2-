import pygame
from map.Map import mapp

from start_window.StartWindow import StartStateMenu


if __name__ == '__main__':
    pygame.init()
    StartStateMenu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

    pygame.quit()
