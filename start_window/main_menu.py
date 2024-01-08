import pygame
# from map.Map import mapp
from start_window.StartWindow import StartStateMenu, Buttons

flag = True


class Main:
    def __init__(self):
        global flag
        flag = True
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        StartStateMenu(screen)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Buttons(screen, flag)