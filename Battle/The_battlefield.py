import pygame
import sqlite3
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
        self.units_ids_on_board = []
        self.board = [[0] * width for _ in range(height)]

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
            # отрисовка рамок для клеточного поля
        else:
            pass
        # думаю стоит добавить сюда отрисовку уведомления об окончание боя, и вывести статистику потерь(это скореее для меня)

    def start_battle(self, number_of_battle):
        self.battle_is_running = True
        conn = sqlite3.connect('../DataBase/game.db')

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM units_in_inventory')
        rows = cursor.fetchall()
        # Закрываем соединение с базой данных
        conn.close()
        for row in rows:
            self.units_ids_on_board.append(row[0])
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) == (0, 0) and rows[0]:
                    self.board[y][x] = rows[0][1]
                if (x, y) == (0, 0) and rows[1]:
                    self.board[y][x] = rows[1][1]
                if (x, y) == (0, 0) and rows[2]:
                    self.board[y][x] = rows[2][1]
                if (x, y) == (0, 0) and rows[3]:
                    self.board[y][x] = rows[3][1]
                if (x, y) == (0, 0) and rows[4]:
                    self.board[y][x] = rows[4][1]

    def end_battle(self):
        self.battle_is_running = False

    def move(self):
        pass

    def may_attack(self):
        for y in range(self.height):
            for x in range(self.width):
                pass

    def attack(self):
        return Unit.get_total_damage(1, 1)

    def units_on_board(self, *args, enemy_units):
        # args - id юнитов в инвинтаре игрока, звыисит от того, как они будут передаваться из бд. enemy_units -
        # список id юнитов врага, который даётся на вход при начале абсолютно любого боя
        for hero_unit in args:
            pass
        for enemy_unit in enemy_units:
            pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Сражение')
    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    board = Thebattlefield(16, 8)
    board.set_view(80, 90, 90)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
