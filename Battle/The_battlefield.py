import sqlite3

import pygame

from Units import Unit


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
                        pygame.draw.rect(screen,
                                         pygame.Color(100 - self.board[y][x] * 10, 100 + self.board[y][x] * 10, 100),
                                         (self.cell_size * x + self.left + 5,
                                          self.cell_size * y + self.top + 5,
                                          80,
                                          80))
            # отрисовка рамок для клеточного поля
        else:
            pygame.draw.rect(screen, pygame.Color(200, 10, 87),
                             (0, 0, self.width * self.cell_size + (2 * self.left),
                              self.height * self.cell_size + 2 * self.top))
            # думаю стоит добавить сюда отрисовку уведомления об окончание боя, и вывести статистику потерь(это скореее для меня)

    def start_battle(self, number_of_battle):
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
        Un = Unit()
        lst = Un.the_sequence_of_the_move()
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
        Un = Unit()
        lst = Un.the_sequence_of_the_move()
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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Сражение')
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
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
