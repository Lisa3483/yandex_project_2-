import pygame
from start_window.StartWindow import StartStateMenu
from Exit_window.exit import Exit
from Statistic.stats_window import Statistics
from Name_window.name import Name
from Save.save_game import SaveGame
from Save.load_game import Saves
from End_windows.death_window import Death
from End_windows.end_game_window import EndGame
from Side_Menu.side_menu import SideMenu
from Music.Menu_music import Music
from map.game import Game

flag = 1


class Main:
    def __init__(self, screen):
        global flag
        self.first_time = True
        Music()
        self.clock = 0
        self.screen = screen
        self.name = ''
        pygame.display.set_caption('The little world')
        running = True
        self.f = True
        self.menu = 'start'
        self.animation_count = 0
        self.unic_number = 0
        self.fc = StartStateMenu(self.screen)

        while running:
            self.windows()
            self.events()
            self.rer()
            self.flags()

    def events(self):
        self.fc.all_events()

    def windows(self):
        self.fc.okno()

    def rer(self):
        global flag
        flag = self.fc.flagg()

    def flags(self):
        global flag
        if flag == 1:
            self.menu = 'start'
            self.fc = StartStateMenu(self.screen)

        if flag == 3:
            self.fc = Statistics(self.screen, self.menu)

        elif flag == 4:
            self.fc = Exit(self.screen, self.menu)

        elif flag == 5:
            self.fc = Name(self.screen)
            self.name = Name(self.screen).names()

        elif flag == 7:
            self.fc = Game(self.screen, self.first_time)
            self.first_time = False
            self.menu = 'side'
            self.clock = Game(self.screen, self.first_time).get_clock()

        elif flag == 2:
            self.fc = Saves(self.screen, self.menu)
            self.f = Saves(self.screen, self.menu).ff()
            self.name = Saves(self.screen, self.menu).get_name()
            print(self.name)
            if not self.f:
                self.unic_number = Saves(self.screen, self.menu).game()
                flag = self.fc.new_game()
                self.f = True

        elif flag == 8:
            self.fc = Death(self.screen)
            self.first_time = True

        elif flag == 9:
            self.fc = EndGame(self.screen, self.unic_number)
            self.first_time = True

        elif flag == 10:
            self.fc = SideMenu(self.screen)
            self.first_time = True

        elif flag == 12:
            self.fc = SaveGame(self.screen, self.name, self.menu, self.unic_number)
            self.f = SaveGame(self.screen, self.name, self.menu, self.unic_number).ff()
            if self.unic_number == 0:
                self.unic_number = SaveGame(self.screen, self.name, self.menu, 0).get_unic_number()
            if not self.f:
                flag = self.fc.new_game()
                self.f = True



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    Main(screen)


