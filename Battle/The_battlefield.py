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
                                         pygame.Color(100 - self.board[y][x] * 5, 100 + self.board[y][x] * 5, 100),
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

    def round_move(self, enemy_or_no):
        Un = Unit()
        lst = Un.the_sequence_of_the_move()
        cast_point = 0
        if self.battle_is_running:
            for id in lst:
                if int(id[0]) <= 5 and not enemy_or_no:
                    conn = sqlite3.connect('../DataBase/game.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        f'''SELECT * FROM units_in_inventory''')
                    rows = cursor.fetchall()
                    # Закрываем соединение с базой данных
                    conn.close()
                    if cast_point == 0:
                        cast_point = 1
                elif enemy_or_no:
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
                                                if int(id[1]) - abs(x_last):
                                                    self.board[y_1][int(id[1]) - abs(x_last)] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                elif int(id[1]) - abs(y_last):
                                                    self.board[int(id[1]) - abs(y_last)][x_1] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                elif not int(id[1]) - abs(x_last):
                                                    self.board[y_0][x_last - int(id[1])] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                                elif not int(id[1]) - abs(y_last):
                                                    self.board[y_last - int(id[1])][x_last] = self.board[y_0][x_0]
                                                    self.board[y_0][x_0] = 0
                                            break
                                        break

    def the_sqarense_track(self):
        pass

    def may_attack(self, x_pos, y_pos, id_of_attack, id_of_def):
        if self.battle_is_running:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for y in range(self.height):
                        for x in range(self.width):
                            pass
                # при нажатии левой кнопки мыши, проверяет есть-ли вражеский юнит на данной позиции

    def attack(self):
        Un = Unit()
        return Un.get_total_damage(1, 2)

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
    board.start_battle(5)  # тут номер битвы, так думаю будет удобно и просто, просто пронумеровать все битвы
    board.set_view(80, 90, 90)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    board.round_move(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    board.round_move(0)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
