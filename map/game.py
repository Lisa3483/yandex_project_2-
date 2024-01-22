import pygame
import sys
from pygame.locals import *
from pygame import Color
from map.Map_1 import Map, FLAG_ENEMY_1, FLAG_ENEMY_2

TILE = 8

animation_count, speed, x, y, x_new, y_new = 0, 1, 50, 190, 0, 0
right, left, up, down = False, False, False, False
button_pressed = False
player_down, player_right, player_up, player_left, player_stand = '', '', '', '', ''


class Game:
    done = False

    def __init__(self, screen, first_time):
        self.first_time = first_time
        self.screen = screen
        self.width, self.height = 800, 600
        self.flag = 7

        self.clock = pygame.time.Clock()
        self.enemy1 = pygame.image.load('map//images//img_of_skeleton-wariorr.png')
        self.enemy2 = pygame.image.load('map//images//img_of_sword.png')

        self.enemy1_x = 200
        self.enemy1_y = 400
        self.enemy2_x = 800
        self.enemy2_y = 50
        self.map = Map(self)
        if self.first_time:
            self.draw_hero()

        pygame.display.update()

    def flagg(self):
        return self.flag

    def okno(self):
        pass

    def get_clock(self):
        return self.clock

    def all_events(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.draw_window()
            pygame.display.flip()
            self.clock.tick(60)

    def draw_window(self):
        global animation_count, right, left, up, down, x, y, speed, x_new, y_new, \
            player_down, player_right, player_up, player_left, player_stand
        if animation_count + 1 >= 40:
            animation_count = 0
        if left:  # Анимация перемещения влево
            self.screen.blit(player_left[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif right:  # Анимация перемещения вправо
            self.screen.blit(player_right[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif up:  # Анимация перемещения вверх
            self.screen.blit(player_up[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        elif down:  # Анимация перемещения вниз
            self.screen.blit(player_down[animation_count // 4], (x, y))
            animation_count += 1
            if animation_count == 8:
                animation_count = 0
        else:
            self.screen.blit(player_stand,
                             (x, y))  # Всегда отрисовываем персонажа, когда он не перемещается
        if FLAG_ENEMY_1:
            self.screen.blit(self.enemy1, (self.enemy1_x, self.enemy1_y))
        if FLAG_ENEMY_2:
            self.screen.blit(self.enemy2, (self.enemy2_x, self.enemy2_y))
        pygame.display.update()

    def player(self):
        global animation_count, right, left, up, down, x, y, speed, x_new, y_new, \
            player_down, player_right, player_up, player_left, player_stand
        if x != x_new or y != y_new:
            if x != x_new and y != y_new:
                if x > x_new and y > y_new:
                    if self.map.collision_map[(x - speed) * (-1) // TILE][
                        (y - speed) * (-1) // TILE] == 0:
                        self.enemy1_x += speed
                        self.enemy1_y += speed
                        self.enemy2_x += speed
                        self.enemy2_y += speed
                        left = True  # Отрисовываем анимацию перемещения влево
                        right = False
                        down = False
                        up = False
                        x -= speed  # Перемещаем персонажа влево
                        y -= speed  # И одновременно перемещаем его вверх
                        self.map.scroll([speed, speed])
                elif x < x_new and y < y_new:
                    if self.map.collision_map[(x + speed) * (-1) // TILE][
                        (y + speed) * (-1) // TILE] == 0:
                        self.enemy1_x -= speed
                        self.enemy1_y -= speed
                        self.enemy2_x -= speed
                        self.enemy2_y -= speed
                        left = False
                        right = True  # Отрисовываем анимацию перемещения вправо
                        down = False
                        up = False
                        x += speed  # Перемещаем персонажа вправо
                        y += speed  # И одновременно перемещаем его вниз
                        self.map.scroll([speed * (-1), speed * (-1)])
                elif x < x_new and y > y_new:
                    if self.map.collision_map[(x + speed) * (-1) // TILE][
                        (y - speed) * (-1) // TILE] == 0:
                        self.enemy1_x -= speed
                        self.enemy1_y += speed
                        self.enemy2_x -= speed
                        self.enemy2_y += speed
                        left = False
                        right = True  # Отрисовываем анимацию перемещения вправо
                        down = False
                        up = False
                        x += speed  # Перемещаем персонажа вправо
                        y -= speed  # И одновременно перемещаем его вверх
                        self.map.scroll([speed * (-1), speed])
                elif x > x_new and y < y_new:
                    if self.map.collision_map[(x - speed) * (-1) // TILE][
                        (y + speed) * (-1) // TILE] == 0:
                        self.enemy1_x += speed
                        self.enemy1_y -= speed
                        self.enemy2_x += speed
                        self.enemy2_y -= speed
                        left = True  # Отрисовываем анимацию перемещения влево
                        right = False
                        down = False
                        up = False
                        x -= speed  # Перемещаем персонажа влево
                        y += speed  # И одновременно перемещаем его вниз
                        self.map.scroll([speed, speed * (-1)])
            elif y != y_new:
                if y < y_new:
                    if self.map.collision_map[(x) * (-1) // TILE][(y + speed) * (-1) // TILE] == 0:
                        self.enemy1_y -= speed
                        self.enemy2_y -= speed
                        left = False
                        right = False
                        down = True  # Отрисовываем анимацию перемещения вниз
                        up = False
                        y += speed  # Перемещаем персонажа вниз
                        self.map.scroll([0, speed * (-1)])
                elif y > y_new:
                    if self.map.collision_map[(x) * (-1) // TILE][(y - speed) * (-1) // TILE] == 0:
                        self.enemy1_y += speed
                        self.enemy2_y += speed
                        left = False
                        right = False
                        down = False
                        up = True  # Отрисовываем анимацию перемещения вверх
                        y -= speed  # Перемещаем персонажа вверх
                        self.map.scroll([0, speed])
            elif x != x_new:
                if x < x_new:
                    if self.map.collision_map[(x + speed) * (-1) // TILE][(y) * (-1) // TILE] == 0:
                        self.enemy1_x -= speed
                        self.enemy2_x -= speed
                        x += speed  # Перемещаем персонажа вправо
                        left = False
                        right = True  # Отрисовываем анимацию перемещения вправо
                        down = False
                        up = False
                        self.map.scroll([speed * (-1), 0])
                elif x > x_new:
                    if self.map.collision_map[(x - speed) * (-1) // TILE][(y) * (-1) // TILE] == 0:
                        self.enemy1_x += speed
                        self.enemy2_x += speed
                        x -= speed  # Перемещаем персонажа влево
                        left = True  # Отрисовываем анимацию перемещения влево
                        right = False
                        down = False
                        up = False
                        self.map.scroll([speed, 0])
        else:
            left = False
            right = False
            down = False
            up = False

    def draw_hero(self):
        global animation_count, right, left, up, down, x, y, speed, x_new, y_new, \
            player_down, player_right, player_up, player_left, player_stand
        player_stand = pygame.image.load('map//hero_image//Hero_forward2.png')
        player_right = [pygame.image.load(f'map//hero_image//Hero_right{i}.png') for i in range(1, 4)]
        player_left = [pygame.image.load(f'map//hero_image//Hero_left{i}.png') for i in range(1, 4)]
        player_up = [pygame.image.load(f'map//hero_image//Hero_top{i}.png') for i in range(1, 4)]
        player_down = [pygame.image.load(f'map//hero_image//Hero_forward{i}.png') for i in range(1, 4)]
        enemy1 = pygame.image.load('map//images//img_of_skeleton-wariorr.png')
        enemy2 = pygame.image.load('map//images//img_of_sword.png')
        clock = pygame.time.Clock()

        x = 50  # Начальные координаты игрока
        y = 190

        x_new = x
        y_new = y

        speed = 1  # Скорость перемещения персонажа

        left = False
        right = False
        up = False
        down = False

        button_pressed = False

        animation_count = 0

        self.game = True
        self.screen.blit(player_stand, (x, y))

    def handle_events(self):
        global animation_count, right, left, up, down, x, y, speed, x_new, y_new, \
            player_down, player_right, player_up, player_left, player_stand, button_pressed
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 - означает левую кнопку мыши
                    x_new, y_new = event.pos  # Координаты точки, где находиться курсор
                    button_pressed = True
            elif event.type == KEYDOWN:
                # exit on Escape
                if event.key == K_ESCAPE:
                    self.done = True

                elif event.key == K_s:
                    self.map.scrolling = not self.map.scrolling
                elif event.key == K_SPACE:

                    self.map.randomize()

                elif event.key == K_f:
                    self.done = True
                    self.flag = 10

        if button_pressed:
            self.player()

    def draw(self):

        self.screen.fill(Color("black"))
        self.map.draw()
        pygame.display.flip()
