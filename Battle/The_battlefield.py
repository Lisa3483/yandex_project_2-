import os
import sqlite3
import sys

import pygame

sys.path.append('../')

from End_windows.death_window import Death
from End_windows.end_game_window import EndGame
from Battle.Units import Unit
from Battle.database_creator_1 import DataBasecreator
from Battle.spell_book import Spell_book


class Thebattlefield:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 0
        self.battle_is_running = False
        self.quality = 0
        self.units_qualitys = []
        self.board = [[0] * width for _ in range(height)]
        self.number_of_battle = 0
        self.lst = []
        self.sprite_image_angel = pygame.image.load('Battle/sprites//img_of_angel.png')
        self.sprite_image_dark_horse = pygame.image.load('Battle/sprites/img_of_dark_horse.png')
        self.sprite_image_skelet = pygame.image.load('Battle/sprites/img_of_skelet.png')
        self.sprite_image_skelet_warrior = pygame.image.load('Battle/sprites/img_of_skeleton-wariorr.png')
        self.sprite_image_spear = pygame.image.load('Battle/sprites/img_of_spear.png')
        self.sprite_image_sword = pygame.image.load('Battle/sprites/img_of_sword.png')
        self.sprite_image_paladin = pygame.image.load('Battle/sprites/img_of_paladin.png')
        self.sprite_image_ghost = pygame.image.load('Battle/sprites/img_of_gost.png')
        self.sprite_image_horse = pygame.image.load('Battle/sprites/img_of_horse.png')
        self.sprite_image_dragon = pygame.image.load('Battle/sprites/img_of_dragon.png')
        self.sprite_image_spell = pygame.image.load('Battle/sprites/img_of_book.png')
        self.sprite_image_bolt = pygame.image.load('Battle/sprites/bolt.png')
        self.half_hp_lst = [4, 7, 12, 30, 120, 4, 8, 9, 33, 100]
        self.cast_point = 0
        self.tick = [0, 0, 0]

    def retr_selfrect_x(self, x):
        return self.cell_size * x + self.left + 5

    def retr_selfrect_y(self, y):
        return self.cell_size * y + self.top + 5

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('Battle//sprites/', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            pass
        return image

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.screen = screen
        if self.battle_is_running:
            for y in range(self.height):
                for x in range(self.width):
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top - 30,
                        self.cell_size,
                        self.cell_size), 1)
            # отрисовка клеточек на клеточном поле
            pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                             (0, 0, self.width * self.cell_size + (2 * self.left), self.top - 30))
            pygame.draw.rect(screen, pygame.Color(202, 196, 176), (
                0, self.height * self.cell_size + self.top - 30, self.width * self.cell_size + (2 * self.left),
                self.height * self.cell_size + (self.top * 2) - 30))
            pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                             (0, 0, self.left, self.height * self.cell_size + self.top * 2))
            pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                             (self.width * self.cell_size + (1 * self.left), 0, self.left,
                              self.height * self.cell_size + self.top * 2))
            screen.blit(self.sprite_image_spell,
                        (self.cell_size * 16 + self.left - 40, self.cell_size * 8 + self.top - 25))

            for x in range(self.width):
                for y in range(self.height):
                    if self.board[y][x]:
                        if self.units_qualitys[self.board[y][x] - 1] <= 0:
                            self.board[y][x] = 0
                        font = pygame.font.Font(None, 36)
                        if self.board[y][x] == 5:
                            screen.blit(self.sprite_image_angel,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[4]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 1:
                            screen.blit(self.sprite_image_spear,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[0]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 2:
                            screen.blit(self.sprite_image_sword,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[1]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 3:
                            screen.blit(self.sprite_image_horse,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[2]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 4:
                            screen.blit(self.sprite_image_paladin,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[3]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 6:
                            screen.blit(self.sprite_image_skelet,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[5]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 7:
                            screen.blit(self.sprite_image_skelet_warrior,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[6]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 8:
                            screen.blit(self.sprite_image_ghost,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[7]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 9:
                            screen.blit(self.sprite_image_dark_horse,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[8]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 10:
                            screen.blit(self.sprite_image_dragon,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5 - 30))
                            text = font.render(f"{self.units_qualitys[9]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                                self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 - 30 + 75))
                            screen.blit(text, place)

            if self.tick[0] > 0:
                self.tick[0] -= 1
                screen.blit(self.sprite_image_bolt,
                            (self.cell_size * self.tick[1] + self.left + 5,
                             self.cell_size * self.tick[2] + self.top + 5 - 30))
        elif self.units_on_board():
            en = EndGame(screen)
            en.okno()
        else:
            en = Death(screen)
            en.okno()

    def start_battle(self, number_of_battle):
        self.cast_point = 407
        data_b = DataBasecreator()
        data_b.create()
        self.number_of_battle = number_of_battle
        self.battle_is_running = True
        un = Unit()
        self.lst = un.the_sequence_of_the_move()
        conn = sqlite3.connect('DataBase/game.db')

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM units_in_inventory')
        rows = cursor.fetchall()
        # Закрываем соединение с базой данных
        conn.close()
        self.units_qualitys = [row[2] for row in rows]
        self.units_qualitys = self.units_qualitys[:5]
        conn = sqlite3.connect('DataBase/game.db')

        cursor = conn.cursor()
        cursor.execute(f'''SELECT * FROM enemy_units_in_battle WHERE number_of_battle="{number_of_battle}"''')
        ows = cursor.fetchall()
        # Закрываем соединение с базой данных
        conn.close()
        for i in range(1, len(ows[0]), 2):
            self.units_qualitys.append(ows[0][i + 1])
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) == (0, 0) and rows[0]:
                    self.board[y][x] = rows[0][1]
                if (x, y) == (0, 2) and rows[1]:
                    self.board[y][x] = rows[1][1]
                if (x, y) == (0, 4) and rows[2]:
                    self.board[y][x] = rows[2][1]
                if (x, y) == (0, 6) and rows[3]:
                    self.board[y][x] = rows[3][1]
                if (x, y) == (0, 7) and rows[4]:
                    self.board[y][x] = rows[4][1]
        conn = sqlite3.connect('DataBase/game.db')

        cursor = conn.cursor()
        cursor.execute(f'''SELECT * FROM enemy_units_in_battle WHERE number_of_battle="{number_of_battle}"''')
        rows = cursor.fetchall()
        # Закрываем соединение с базой данных
        conn.close()
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) == (15, 0) and rows[0][1]:
                    self.board[y][x] = rows[0][1]
                if (x, y) == (15, 2) and rows[0][3]:
                    self.board[y][x] = rows[0][3]
                if (x, y) == (15, 4) and rows[0][5]:
                    self.board[y][x] = rows[0][5]
                if (x, y) == (15, 6) and rows[0][7]:
                    self.board[y][x] = rows[0][7]
                if (x, y) == (15, 7) and rows[0][9]:
                    self.board[y][x] = rows[0][9]
        self.number_of_battle = number_of_battle

    def end_battle(self):
        self.battle_is_running = False
        conn = sqlite3.connect('DataBase/game.db')
        cursor = conn.cursor()
        for i in self.units_qualitys:
            cursor.execute(f'''
            INSERT INTO units_in_inventory (quantity)
            VALUES ('{i}')
            ''')
        # Закрываем соединение с базой данных
        conn.close()
        # значения таблицы quality меняются на те, что были получены в результате боя

    def round_move_invent(self):
        un = Unit()
        self.lst = sorted(self.lst, key=lambda x: x[1], reverse=True)
        if self.battle_is_running:
            for id in self.lst:
                self.render(self.screen)
                if int(id[0]) <= 5:
                    fl = False
                    for x_0 in range(self.width):
                        for y_0 in range(self.height):
                            if int(self.board[y_0][x_0]) == int(id[0]):
                                while True:
                                    for e in pygame.event.get():
                                        if not fl:
                                            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                                                x_1, y_1 = (pygame.mouse.get_pos()[0] - self.left) // self.cell_size, (
                                                        pygame.mouse.get_pos()[1] - self.top) // self.cell_size
                                                if x_1 <= 15 and y_1 <= 7:
                                                    if self.board[y_1][x_1] == 0:
                                                        self.board[y_1][x_1] = int(id[0])
                                                        fl = True
                                                        self.board[y_0][x_0] = 0
                                                    if self.board[y_1][x_1] > 5:
                                                        conn = sqlite3.connect('DataBase/game.db')
                                                        cursor = conn.cursor()
                                                        cursor.execute(
                                                            f"SELECT unit_hp FROM units WHERE id = '{self.board[y_1][x_1]}'")
                                                        fetch = cursor.fetchall()
                                                        conn.close()
                                                        damage = un.get_total_damage(self.board[y_0][x_0],
                                                                                     self.board[y_1][x_1])

                                                        hp = (int(fetch[0][0])) * int(
                                                            self.units_qualitys[self.board[y_1][x_1] - 1] - 1) + + \
                                                                 self.half_hp_lst[self.board[y_1][x_1] - 1]
                                                        hp = hp - int(damage)
                                                        self.half_hp_lst[self.board[y_1][x_1] - 1] = hp % int(
                                                            fetch[0][0])
                                                        if hp // int(fetch[0][0]) + self.half_hp_lst[
                                                            self.board[y_1][x_1] - 1] > 0 and \
                                                                self.half_hp_lst[self.board[y_1][x_1] - 1]:
                                                            self.units_qualitys[self.board[y_1][x_1] - 1] = hp // int(
                                                                fetch[0][0]) + 1
                                                            if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                                if y_1 - 1 > 0 and y_1 + 1 <= 7:
                                                                    if self.board[y_1 - 1][x_1] == 0:
                                                                        self.board[y_1 - 1][x_1] = id[0]
                                                                    elif self.board[y_1 - 1][x_1 - 1] == 0:
                                                                        self.board[y_1 - 1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1 - 1][x_1 + 1] == 0:
                                                                        self.board[y_1 - 1][x_1 + 1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1 - 1] == 0:
                                                                        self.board[y_1 + 1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1][x_1 - 1] == 0:
                                                                        self.board[y_1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1][x_1 + 1] == 0:
                                                                        self.board[y_1][x_1 + 1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1 + 1] == 0:
                                                                        self.board[y_1 + 1][x_1 + 1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1] == 0:
                                                                        self.board[y_1 + 1][x_1] = id[0]
                                                                else:
                                                                    if self.board[y_1 - 1][x_1] == 0:
                                                                        self.board[y_1 - 1][x_1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1] == 0:
                                                                        self.board[x_1 + 1][x_1] = id[0]
                                                            else:
                                                                if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                                    if self.board[y_1][x_1 - 1] == 0:
                                                                        self.board[y_1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1][x_1 + 1] == 0:
                                                                        self.board[y_1][x_1 + 1] = id[0]
                                                        elif hp // int(fetch[0][0]) > 0:
                                                            self.units_qualitys[self.board[y_1][x_1] - 1] = hp // int(
                                                                fetch[0][0])
                                                            if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                                if y_1 - 1 > 0 and y_1 + 1 <= 7:
                                                                    if self.board[y_1 - 1][x_1] == 0:
                                                                        self.board[y_1 - 1][x_1] = id[0]
                                                                    elif self.board[y_1 - 1][x_1 - 1] == 0:
                                                                        self.board[y_1 - 1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1 - 1][x_1 + 1] == 0:
                                                                        self.board[y_1 - 1][x_1 + 1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1 - 1] == 0:
                                                                        self.board[y_1 + 1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1][x_1 - 1] == 0:
                                                                        self.board[y_1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1][x_1 + 1] == 0:
                                                                        self.board[y_1][x_1 + 1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1 + 1] == 0:
                                                                        self.board[y_1 + 1][x_1 + 1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1] == 0:
                                                                        self.board[y_1 + 1][x_1] = id[0]
                                                                else:
                                                                    if self.board[y_1 - 1][x_1] == 0:
                                                                        self.board[y_1 - 1][x_1] = id[0]
                                                                    elif self.board[y_1 + 1][x_1] == 0:
                                                                        self.board[x_1 + 1][x_1] = id[0]
                                                            else:
                                                                if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                                    if self.board[y_1][x_1 - 1] == 0:
                                                                        self.board[y_1][x_1 - 1] = id[0]
                                                                    elif self.board[y_1][x_1 + 1] == 0:
                                                                        self.board[y_1][x_1 + 1] = id[0]

                                                        else:
                                                            self.board[y_1][x_1] = self.board[y_0][x_0]
                                                            self.board[y_0][x_0] = 0
                                                        fl = True

                                        if fl:
                                            break
                                    if fl:
                                        break

                            if fl:
                                break
                        if fl:
                            break

                elif int(id[0]) >= 6:
                    fl_enemy = False
                    conn = sqlite3.connect('DataBase/game.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        f'''SELECT * FROM enemy_units_in_battle WHERE number_of_battle="{self.number_of_battle}"''')
                    rows = cursor.fetchall()
                    # Закрываем соединение с базой данных
                    conn.close()
                    for x_0 in range(self.width):
                        for y_0 in range(self.height):
                            if int(self.board[y_0][x_0]) == int(id[0]):
                                fl_enemy = True
                                for x_1 in range(self.width):
                                    for y_1 in range(self.height):
                                        if int(self.board[y_1][x_1]) <= 5 and int(self.board[y_1][x_1]) > 0:
                                            x_last = 0
                                            y_last = 0
                                            if x_0 > x_1 and y_0 > y_1:
                                                x_last = x_0 - x_1 - 1
                                                y_last = y_0 - y_1 - 1
                                            elif x_0 < x_1 and y_0 > y_1:
                                                x_last = x_1 - x_0 + 1
                                                y_last = y_0 - y_1 + 1
                                            elif x_0 < x_1 and y_0 < y_1:
                                                x_last = x_1 - x_0 + 1
                                                y_last = y_1 - y_0 + 1
                                            elif x_0 > x_1 and y_0 < y_1:
                                                x_last = x_0 - x_1 + 1
                                                y_last = y_1 - y_0 + 1
                                            if abs(x_last) + abs(y_last) <= int(id[1]):
                                                conn = sqlite3.connect('DataBase/game.db')
                                                cursor = conn.cursor()
                                                cursor.execute(
                                                    f"SELECT unit_hp FROM units WHERE id='{self.board[y_1][x_1]}'")
                                                fetch = cursor.fetchall()
                                                conn.close()
                                                damage = un.get_total_damage(self.board[y_0][x_0],
                                                                             self.board[y_1][x_1])

                                                hp = (int(fetch[0][0])) * int(
                                                    self.units_qualitys[self.board[y_1][x_1] - 1] - 1) + + \
                                                         self.half_hp_lst[self.board[y_1][x_1] - 1]
                                                hp = hp - int(damage)
                                                self.half_hp_lst[self.board[y_1][x_1] - 1] = hp % int(
                                                    fetch[0][0])
                                                if hp // int(fetch[0][0]) + self.half_hp_lst[
                                                    self.board[y_1][x_1] - 1] and \
                                                        self.half_hp_lst[self.board[y_1][x_1] - 1]:
                                                    self.units_qualitys[self.board[y_1][x_1] - 1] = hp // int(
                                                        fetch[0][0]) + 1
                                                    if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                        if y_1 - 1 > 0 and y_1 + 1 <= 7:
                                                            if self.board[y_1 - 1][x_1] == 0:
                                                                self.board[y_1 - 1][x_1] = id[0]
                                                            elif self.board[y_1 - 1][x_1 - 1] == 0:
                                                                self.board[y_1 - 1][x_1 - 1] = id[0]
                                                            elif self.board[y_1 - 1][x_1 + 1] == 0:
                                                                self.board[y_1 - 1][x_1 + 1] = id[0]
                                                            elif self.board[y_1 + 1][x_1 - 1] == 0:
                                                                self.board[y_1 + 1][x_1 - 1] = id[0]
                                                            elif self.board[y_1][x_1 - 1] == 0:
                                                                self.board[y_1][x_1 - 1] = id[0]
                                                            elif self.board[y_1][x_1 + 1] == 0:
                                                                self.board[y_1][x_1 + 1] = id[0]
                                                            elif self.board[y_1 + 1][x_1 + 1] == 0:
                                                                self.board[y_1 + 1][x_1 + 1] = id[0]
                                                            elif self.board[y_1 + 1][x_1] == 0:
                                                                self.board[y_1 + 1][x_1] = id[0]
                                                        else:
                                                            if self.board[y_1 - 1][x_1] == 0:
                                                                self.board[y_1 - 1][x_1] = id[0]
                                                            elif self.board[y_1 + 1][x_1] == 0:
                                                                self.board[x_1 + 1][x_1] = id[0]
                                                    else:
                                                        if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                            if self.board[y_1][x_1 - 1] == 0:
                                                                self.board[y_1][x_1 - 1] = id[0]
                                                            elif self.board[y_1][x_1 + 1] == 0:
                                                                self.board[y_1][x_1 + 1] = id[0]
                                                elif hp // int(fetch[0][0]):
                                                    self.units_qualitys[self.board[y_1][x_1] - 1] = hp // int(
                                                        fetch[0][0])
                                                    if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                        if y_1 - 1 > 0 and y_1 + 1 <= 7:
                                                            if self.board[y_1 - 1][x_1] == 0:
                                                                self.board[y_1 - 1][x_1] = id[0]
                                                            elif self.board[y_1 - 1][x_1 - 1] == 0:
                                                                self.board[y_1 - 1][x_1 - 1] = id[0]
                                                            elif self.board[y_1 - 1][x_1 + 1] == 0:
                                                                self.board[y_1 - 1][x_1 + 1] = id[0]
                                                            elif self.board[y_1 + 1][x_1 - 1] == 0:
                                                                self.board[y_1 + 1][x_1 - 1] = id[0]
                                                            elif self.board[y_1][x_1 - 1] == 0:
                                                                self.board[y_1][x_1 - 1] = id[0]
                                                            elif self.board[y_1][x_1 + 1] == 0:
                                                                self.board[y_1][x_1 + 1] = id[0]
                                                            elif self.board[y_1 + 1][x_1 + 1] == 0:
                                                                self.board[y_1 + 1][x_1 + 1] = id[0]
                                                            elif self.board[y_1 + 1][x_1] == 0:
                                                                self.board[y_1 + 1][x_1] = id[0]
                                                        else:
                                                            if self.board[y_1 - 1][x_1] == 0:
                                                                self.board[y_1 - 1][x_1] = id[0]
                                                            elif self.board[y_1 + 1][x_1] == 0:
                                                                self.board[x_1 + 1][x_1] = id[0]
                                                    else:
                                                        if x_1 - 1 >= 0 and x_1 + 1 <= 15:
                                                            if self.board[y_1][x_1 - 1] == 0:
                                                                self.board[y_1][x_1 - 1] = id[0]
                                                            elif self.board[y_1][x_1 + 1] == 0:
                                                                self.board[y_1][x_1 + 1] = id[0]
                                                else:
                                                    self.board[y_1][x_1] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                    fl_enemy = True


                                            else:
                                                if int(id[1]) - abs(x_last) and \
                                                        self.board[y_1][int(id[1]) - abs(x_last)] == 0:
                                                    self.board[y_1][int(id[1]) - abs(x_last)] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                    fl_enemy = True
                                                elif int(id[1]) - abs(y_last) and self.board[int(id[1]) -
                                                                                             abs(y_last)][x_1] == 0:
                                                    self.board[int(id[1]) - abs(y_last)][x_1] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                    fl_enemy = True
                                                elif not int(id[1]) - abs(x_last) and \
                                                        self.board[y_0][x_last - int(id[1])] == 0:
                                                    self.board[y_0][x_last - int(id[1])] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                    fl_enemy = True
                                                elif not int(id[1]) - abs(y_last) and \
                                                        self.board[y_last - int(id[1])][x_last] == 0:
                                                    self.board[y_last - int(id[1])][x_last] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0

                                                    fl_enemy = True
                                        if fl_enemy:
                                            break
                                    if fl_enemy:
                                        break
                            if fl_enemy:
                                break
                        if fl_enemy:
                            break

    def cast(self):
        fl = 0
        sp = Spell_book()
        if self.cast_point:
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                        x_1, y_1 = (pygame.mouse.get_pos()[0] - self.left) // self.cell_size, (
                                pygame.mouse.get_pos()[1] - self.top) // self.cell_size
                        conn = sqlite3.connect('DataBase/game.db')
                        cursor = conn.cursor()
                        cursor.execute(
                            f"SELECT unit_hp FROM units WHERE id = '{self.board[y_1][x_1]}'")
                        fetch = cursor.fetchall()
                        conn.close()
                        if self.board[y_1][x_1]:
                            self.cast_point -= 1
                            hp = (int(fetch[0][0])) * int(
                                self.units_qualitys[self.board[y_1][x_1] - 1] - 1)
                            hp -= int(sp.bolt(self.number_of_battle))
                            if hp // int(fetch[0][0]):
                                self.units_qualitys[self.board[y_1][x_1] - 1] = hp // int(
                                    fetch[0][0]) + 1
                                self.tick = [90, x_1, y_1]
                                fl = 1
                                break
                            else:
                                fl = 1
                                self.tick = [90, x_1, y_1]
                                self.board[y_1][x_1] = 0
                                break
                        else:
                            break
                if fl:
                    break

    def units_on_board(self):
        enemy_sum = 0
        hero_sum = 0
        for hero_unit in self.units_qualitys[:5]:
            hero_sum += int(hero_unit)
        for enemy_unit in self.units_qualitys[5:]:
            enemy_sum += int(enemy_unit)
        if not hero_sum:
            self.end_battle()
            return 0
        if not enemy_sum:
            self.end_battle()
            return 1


class Image1(pygame.sprite.Sprite):
    bfelld = Thebattlefield(8, 16)
    image = bfelld.load_image("img_of_bf.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Image1.image
        self.rect = self.image.get_rect()
        self.rect.x = 80 - 30
        self.rect.y = 90 - 30

    def update(self):
        pass


def battle_window(number_of_battle):
    pygame.init()
    pygame.display.set_caption('Сражение')
    im = Image1()
    sprites = pygame.sprite.Group()
    sprites.add(im)
    pygame.mixer.music.load("Battle//music//music_1.mp3")
    pygame.mixer.music.play(-1)

    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    board = Thebattlefield(16, 8)
    board.start_battle(
        number_of_battle)  # тут номер битвы, так думаю будет удобно и просто, просто пронумеровать все битвы
    board.set_view(80, 90, 90)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    try:
                        board.round_move_invent()
                    except Exception:
                        board.end_battle()
                        if number_of_battle == 1:
                            fl_1 = False
                            return fl_1
                        else:
                            fl_2 = False
                            return fl_2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    board.cast()
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
        board.units_on_board()
