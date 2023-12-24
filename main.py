import pygame
# from map.Map import mapp

from start_window.StartWindow import StartStateMenu, Buttons


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    StartStateMenu(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Buttons(screen)
    pygame.quit()
