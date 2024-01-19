import os
import sqlite3
import sys

import pygame

from Units import Unit
from database_creator_1 import DataBasecreator


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
        self.sprite_image_angel = pygame.image.load('sprites/img_of_angel.png')
        self.sprite_image_dark_horse = pygame.image.load('sprites/img_of_dark_horse.png')
        self.sprite_image_skelet = pygame.image.load('sprites/img_of_skelet.png')
        self.sprite_image_skelet_warrior = pygame.image.load('sprites/img_of_skeleton-wariorr.png')
        self.sprite_image_spear = pygame.image.load('sprites/img_of_spear.png')
        self.sprite_image_sword = pygame.image.load('sprites/img_of_sword.png')
        self.sprite_image_paladin = pygame.image.load('sprites/img_of_paladin.png')
        self.sprite_image_ghost = pygame.image.load('sprites/img_of_gost.png')
        self.sprite_image_horse = pygame.image.load('sprites/img_of_horse.png')
        self.sprite_image_dragon = pygame.image.load('sprites/img_of_dragon.png')

    def retr_selfrect_x(self, x):
        return self.cell_size * x + self.left + 5

    def retr_selfrect_y(self, y):
        return self.cell_size * y + self.top + 5

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('sprites', name)
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
        if self.battle_is_running:
            for y in range(self.height):
                for x in range(self.width):
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size,
                        self.cell_size), 1)
            # отрисовка клеточек на клеточном поле
            pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                             (0, 0, self.width * self.cell_size + (2 * self.left), self.top))
            pygame.draw.rect(screen, pygame.Color(202, 196, 176), (
                0, self.height * self.cell_size + self.top, self.width * self.cell_size + (2 * self.left),
                self.height * self.cell_size + (self.top * 2)))
            pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                             (0, 0, self.left, self.height * self.cell_size + self.top * 2))
            pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                             (self.width * self.cell_size + (1 * self.left), 0, self.left,
                              self.height * self.cell_size + self.top * 2))
            for x in range(self.width):
                for y in range(self.height):
                    if self.board[y][x]:
                        font = pygame.font.Font(None, 36)
                        if self.board[y][x] == 5:
                            screen.blit(self.sprite_image_angel,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[4]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 1:
                            screen.blit(self.sprite_image_spear,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[0]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 2:
                            screen.blit(self.sprite_image_sword,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[1]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 3:
                            screen.blit(self.sprite_image_horse,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[2]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 4:
                            screen.blit(self.sprite_image_paladin,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[3]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 6:
                            screen.blit(self.sprite_image_skelet,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[5]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 7:
                            screen.blit(self.sprite_image_skelet_warrior,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[6]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 8:
                            screen.blit(self.sprite_image_ghost,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[7]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 9:
                            screen.blit(self.sprite_image_dark_horse,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[8]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
                        elif self.board[y][x] == 10:
                            screen.blit(self.sprite_image_dragon,
                                        (self.cell_size * x + self.left + 5, self.cell_size * y + self.top + 5))
                            text = font.render(f"{self.units_qualitys[9]}", True, (255, 255, 255))
                            place = text.get_rect(center=(
                            self.cell_size * x + self.left + 5 + 40, self.cell_size * y + self.top + 5 + 75))
                            screen.blit(text, place)
            # отрисовка рамок для клеточного поля
        else:
            pygame.draw.rect(screen, pygame.Color(200, 10, 87),
                             (0, 0, self.width * self.cell_size + (2 * self.left),
                              self.height * self.cell_size + 2 * self.top))
            # думаю стоит добавить сюда отрисовку уведомления об окончание боя, и вывести статистику потерь(это скореее для меня)

    def start_battle(self, number_of_battle):
        data_b = DataBasecreator()
        data_b.create()
        self.battle_is_running = True
        un = Unit()
        self.lst = un.the_sequence_of_the_move()
        conn = sqlite3.connect('../DataBase/game.db')

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM units_in_inventory')
        rows = cursor.fetchall()
        # Закрываем соединение с базой данных
        conn.close()
        self.units_qualitys = [row[1] for row in rows]
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
        conn = sqlite3.connect('../DataBase/game.db')

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
        conn = sqlite3.connect('../DataBase/game.db')
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
        fl = False
        cast_point = 0
        un = Unit()
        if self.battle_is_running:
            for id in self.lst:
                if int(id[0]) <= 5:
                    conn = sqlite3.connect('../DataBase/game.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        f'''SELECT * FROM units_in_inventory''')
                    rows = cursor.fetchall()
                    # Закрываем соединение с базой данных
                    conn.close()
                    if cast_point == 0:
                        cast_point = 1

                    for x_0 in range(self.width):
                        for y_0 in range(self.height):
                            if int(self.board[y_0][x_0]) == int(id[0]):
                                fl = False
                                while True:
                                    if not fl:
                                        for e in pygame.event.get():
                                            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                                                print(pygame.mouse.get_pos())
                                                x_1, y_1 = (pygame.mouse.get_pos()[0] - self.left) // self.cell_size, (
                                                        pygame.mouse.get_pos()[1] - self.top) // self.cell_size
                                                if self.board[y_1][x_1] == 0:
                                                    self.board[y_1][x_1] = int(id[0])
                                                    self.board[y_0][x_0] = 0
                                                if self.board[y_1][x_1] > 5:
                                                    conn = sqlite3.connect('../DataBase/game.db')
                                                    cursor = conn.cursor()
                                                    cursor.execute(
                                                        f"SELECT unit_hp FROM units WHERE id = '{self.board[y_1][x_1]}'")
                                                    fetch = cursor.fetchall()
                                                    conn.close()
                                                    hp = int(fetch[0][0]) * int(
                                                        self.lst[self.board[y_1][x_1]][1])
                                                    hp = hp - int(
                                                        un.get_total_damage(self.board[y_0][x_0], self.board[y_1][x_1]))
                                                    if hp // int(fetch[0][0]):
                                                        self.units_qualitys[self.board[y_1][x_1]] = hp // int(
                                                            fetch[0][0])
                                                        self.lst[self.board[y_1][x_1] - 1] = \
                                                            self.lst[self.board[y_1][x_1] - 1][0], self.units_qualitys[
                                                                self.board[y_1][x_1]]
                                                    else:
                                                        self.board[y_1][x_1] = 0
                                                fl = True
                                    if fl:
                                        break
                            break
                        break

    def round_move_enemy(self):
        un = Unit()
        lst = un.the_sequence_of_the_move()
        if self.battle_is_running:
            for id in lst:
                if int(id[0]) <= 5:
                    pass
                else:
                    conn = sqlite3.connect('../DataBase/game.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        f'''SELECT * FROM enemy_units_in_battle WHERE number_of_battle="{self.number_of_battle}"''')
                    rows = cursor.fetchall()
                    # Закрываем соединение с базой данных
                    conn.close()
                    for x_0 in range(self.width):
                        for y_0 in range(self.height):
                            if int(self.board[y_0][x_0]) == int(id[0]):
                                for x_1 in range(self.width):
                                    for y_1 in range(self.height):
                                        if int(self.board[y_1][x_1]) <= 5:
                                            x_last = 0
                                            y_last = 0
                                            if x_0 > x_1 and y_0 > y_1:
                                                x_last = x_0 - x_1 - 1
                                                y_last = y_0 - y_1 + 1
                                            elif x_0 < x_1 and y_0 > y_1:
                                                x_last = x_1 - x_0 + 1
                                                y_last = y_0 - y_1 + 1
                                            elif x_0 < x_1 and y_0 < y_1:
                                                x_last = x_1 - x_0 + 1
                                                y_last = y_1 - y_0 - 1
                                            elif x_0 > x_1 and y_0 < y_1:
                                                x_last = x_0 - x_1 - 1
                                                y_last = y_1 - y_0 - 1
                                            if abs(x_last) + abs(y_last) <= int(id[1]):
                                                self.board[y_1][x_1] = self.board[y_0][x_0]
                                                self.board[y_0][x_0] = 0
                                            else:
                                                if int(id[1]) - abs(x_last) and self.board[y_1][
                                                    int(id[1]) - abs(x_last)] == 0:
                                                    self.board[y_1][int(id[1]) - abs(x_last)] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                elif int(id[1]) - abs(y_last) and self.board[int(id[1]) - abs(y_last)][
                                                    x_1] == 0:
                                                    self.board[int(id[1]) - abs(y_last)][x_1] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                elif not int(id[1]) - abs(x_last) and self.board[y_0][
                                                    x_last - int(id[1])] == 0:
                                                    self.board[y_0][x_last - int(id[1])] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                elif not int(id[1]) - abs(y_last) and self.board[y_last - int(id[1])][
                                                    x_last] == 0:
                                                    self.board[y_last - int(id[1])][x_last] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                            break
                                        break
                continue

    def the_sqarense_track(self):
        un = Unit()
        lst = un.the_sequence_of_the_move()
        for id in lst:
            if int(id[0]) <= 5:
                pass

    def units_on_board(self, *args, enemy_units):
        # args - id юнитов в инвинтаре игрока, звыисит от того, как они будут передаваться из бд. enemy_units -
        # список id юнитов врага, который даётся на вход при начале абсолютно любого боя
        for hero_unit in args:
            pass
        for enemy_unit in enemy_units:
            pass
        # вроде как-то бесполезно получилось, нигде не используется


class Image1(pygame.sprite.Sprite):
    bfelld = Thebattlefield(8, 16)
    image = bfelld.load_image("img_of_bf.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Image1.image
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 90

    def update(self):
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Сражение')
    im = Image1()
    sprites = pygame.sprite.Group()
    sprites.add(im)
    pygame.mixer.music.load("music/music_1.mp3")
    pygame.mixer.music.play(-1)

    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    board = Thebattlefield(16, 8)
    board.start_battle(1)  # тут номер битвы, так думаю будет удобно и просто, просто пронумеровать все битвы
    board.set_view(80, 90, 90)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    board.round_move_invent()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    board.round_move_enemy()
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
