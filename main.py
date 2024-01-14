import pygame
# from map.Map import mapp
from start_window.StartWindow import StartStateMenu
from Exit_window.exit import Exit
from Statistic.stats_window import Statistics
from Name_window.name import Name
from Save.save_game import SaveGame
from Save.load_game import Saves
from End_windows.death_window import Death
from End_windows.end_game_window import EndGame
from Side_Menu.side_menu import SideMenu

flag = 10


class Main:
    def __init__(self, screen):
        global flag

        self.screen = screen
        self.name = ''
        pygame.display.set_caption('The little world')
        running = True
        self.menu = 'side'
        self.game = 0
        self.fc = SideMenu(self.screen)
        self.f = True

        while running:
            self.rer()
            self.flags()
            self.windows()
            self.events()

    def events(self):
        self.fc.all_events()

    def windows(self):
        self.fc.okno()

    def rer(self):
        global flag
        flag = self.fc.flagg()

    def flags(self):
        if flag == 1:
            self.fc = StartStateMenu(self.screen)

        elif flag == 3:
            self.fc = Statistics(self.screen, self.menu)

        elif flag == 4:
            self.fc = Exit(self.screen)

        elif flag == 5:
            self.fc = Name(self.screen)
            self.name = Name(self.screen).names()

        elif flag == 7:
            self.fc = SaveGame(self.screen, self.name)

        elif flag == 2:
            self.fc = Saves(self.screen)

        elif flag == 8:
            self.fc = Death(self.screen)

        elif flag == 9:
            self.fc = EndGame(self.screen, self.game)

        elif flag == 10:
            self.fc = SideMenu(self.screen)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    Main(screen)


