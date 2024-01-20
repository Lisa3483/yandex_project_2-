import pygame
import sys
from pygame.locals import *
from pygame import Color
from map.Map import Map, FLAG_ENEMY_1, FLAG_ENEMY_2

TILE = 8


class Game:
    done = False

    def __init__(self, width=700, height=500):

        pygame.init()
        self.width, self.height = width, height

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.enemy1_x = 200
        self.enemy1_y = 400
        self.enemy2_x = 800
        self.enemy2_y = 50
        self.map = Map(self)
        self.draw_hero()

        pygame.display.update()

        self.main_loop()

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.draw_window()  # Вызываем метод для отображения персонажа
            pygame.display.flip()  # Обновляем экран
            self.clock.tick(60)

    def draw_window(self):

        if self.animation_count + 1 >= 40:
            self.animation_count = 0
        if self.left:  # Анимация перемещения влево
            self.screen.blit(self.player_left[self.animation_count // 4], (self.x, self.y))
            self.animation_count += 1
            if self.animation_count == 8:
                self.animation_count = 0
        elif self.right:  # Анимация перемещения вправо
            self.screen.blit(self.player_right[self.animation_count // 4], (self.x, self.y))
            self.animation_count += 1
            if self.animation_count == 8:
                self.animation_count = 0
        elif self.up:  # Анимация перемещения вверх
            self.screen.blit(self.player_up[self.animation_count // 4], (self.x, self.y))
            self.animation_count += 1
            if self.animation_count == 8:
                self.animation_count = 0
        elif self.down:  # Анимация перемещения вниз
            self.screen.blit(self.player_down[self.animation_count // 4], (self.x, self.y))
            self.animation_count += 1
            if self.animation_count == 8:
                self.animation_count = 0
        else:
            self.screen.blit(self.player_stand,
                             (self.x, self.y))  # Всегда отрисовываем персонажа, когда он не перемещается
        if FLAG_ENEMY_1:
            self.screen.blit(self.enemy1, (self.enemy1_x, self.enemy1_y))
        if FLAG_ENEMY_2:
            self.screen.blit(self.enemy2, (self.enemy2_x, self.enemy2_y))
        pygame.display.update()

    def player(self):

        if self.x != self.x_new or self.y != self.y_new:
            '''Условие, если координата x игрока не равна координате x курсора 
            или координата y игрока не равна координате y курсора'''
            if self.x != self.x_new and self.y != self.y_new:
                '''Повторяется это условие, для того, чтобы под каждое перемещение персонажа 
                (вверх, вниз, влево, вправо) сделать анимацию'''
                if self.x > self.x_new and self.y > self.y_new:
                    '''Условие, если координата x игрока больше координаты x курсора 
                или координата y игрока больше координаты y курсора'''
                    if self.map.collision_map[(self.x - self.speed) * (-1) // TILE][
                        (self.y - self.speed) * (-1) // TILE] == 0:
                        self.enemy1_x += self.speed
                        self.enemy1_y += self.speed
                        self.enemy2_x += self.speed
                        self.enemy2_y += self.speed
                        self.left = True  # Отрисовываем анимацию перемещения влево
                        self.right = False
                        self.down = False
                        self.up = False
                        self.x -= self.speed  # Перемещаем персонажа влево
                        self.y -= self.speed  # И одновременно перемещаем его вверх
                        self.map.scroll([self.speed, self.speed])
                elif self.x < self.x_new and self.y < self.y_new:
                    if self.map.collision_map[(self.x + self.speed) * (-1) // TILE][
                        (self.y + self.speed) * (-1) // TILE] == 0:
                        self.enemy1_x -= self.speed
                        self.enemy1_y -= self.speed
                        self.enemy2_x -= self.speed
                        self.enemy2_y -= self.speed
                        self.left = False
                        self.right = True  # Отрисовываем анимацию перемещения вправо
                        self.down = False
                        self.up = False
                        self.x += self.speed  # Перемещаем персонажа вправо
                        self.y += self.speed  # И одновременно перемещаем его вниз
                        self.map.scroll([self.speed * (-1), self.speed * (-1)])
                elif self.x < self.x_new and self.y > self.y_new:
                    if self.map.collision_map[(self.x + self.speed) * (-1) // TILE][
                        (self.y - self.speed) * (-1) // TILE] == 0:
                        self.enemy1_x -= self.speed
                        self.enemy1_y += self.speed
                        self.enemy2_x -= self.speed
                        self.enemy2_y += self.speed
                        self.left = False
                        self.right = True  # Отрисовываем анимацию перемещения вправо
                        self.down = False
                        self.up = False
                        self.x += self.speed  # Перемещаем персонажа вправо
                        self.y -= self.speed  # И одновременно перемещаем его вверх
                        self.map.scroll([self.speed * (-1), self.speed])
                elif self.x > self.x_new and self.y < self.y_new:
                    if self.map.collision_map[(self.x - self.speed) * (-1) // TILE][
                        (self.y + self.speed) * (-1) // TILE] == 0:
                        self.enemy1_x += self.speed
                        self.enemy1_y -= self.speed
                        self.enemy2_x += self.speed
                        self.enemy2_y -= self.speed
                        self.left = True  # Отрисовываем анимацию перемещения влево
                        self.right = False
                        self.down = False
                        self.up = False
                        self.x -= self.speed  # Перемещаем персонажа влево
                        self.y += self.speed  # И одновременно перемещаем его вниз
                        self.map.scroll([self.speed, self.speed * (-1)])
            elif self.y != self.y_new:
                if self.y < self.y_new:
                    if self.map.collision_map[(self.x) * (-1) // TILE][(self.y + self.speed) * (-1) // TILE] == 0:
                        self.enemy1_y -= self.speed
                        self.enemy2_y -= self.speed
                        self.left = False
                        self.right = False
                        self.down = True  # Отрисовываем анимацию перемещения вниз
                        self.up = False
                        self.y += self.speed  # Перемещаем персонажа вниз
                        self.map.scroll([0, self.speed * (-1)])
                elif self.y > self.y_new:
                    if self.map.collision_map[(self.x) * (-1) // TILE][(self.y - self.speed) * (-1) // TILE] == 0:
                        self.enemy1_y += self.speed
                        self.enemy2_y += self.speed
                        self.left = False
                        self.right = False
                        self.down = False
                        self.up = True  # Отрисовываем анимацию перемещения вверх
                        self.y -= self.speed  # Перемещаем персонажа вверх
                        self.map.scroll([0, self.speed])
            elif self.x != self.x_new:
                if self.x < self.x_new:
                    if self.map.collision_map[(self.x + self.speed) * (-1) // TILE][(self.y) * (-1) // TILE] == 0:
                        self.enemy1_x -= self.speed
                        self.enemy2_x -= self.speed
                        self.x += self.speed  # Перемещаем персонажа вправо
                        self.left = False
                        self.right = True  # Отрисовываем анимацию перемещения вправо
                        self.down = False
                        self.up = False
                        self.map.scroll([self.speed * (-1), 0])
                elif self.x > self.x_new:
                    if self.map.collision_map[(self.x - self.speed) * (-1) // TILE][(self.y) * (-1) // TILE] == 0:
                        self.enemy1_x += self.speed
                        self.enemy2_x += self.speed
                        self.x -= self.speed  # Перемещаем персонажа влево
                        self.left = True  # Отрисовываем анимацию перемещения влево
                        self.right = False
                        self.down = False
                        self.up = False
                        self.map.scroll([self.speed, 0])
        else:
            self.left = False
            self.right = False
            self.down = False
            self.up = False

    def draw_hero(self):

        self.player_stand = pygame.image.load('map//hero_image//Hero_forward2.png')
        self.player_right = [pygame.image.load(f'map//hero_image//Hero_right{i}.png') for i in range(1, 4)]
        self.player_left = [pygame.image.load(f'map//hero_image//Hero_left{i}.png') for i in range(1, 4)]
        self.player_up = [pygame.image.load(f'map//hero_image//Hero_top{i}.png') for i in range(1, 4)]
        self.player_down = [pygame.image.load(f'map//hero_image//Hero_forward{i}.png') for i in range(1, 4)]
        self.enemy1 = pygame.image.load('map//images//img_of_skeleton-wariorr.png')
        self.enemy2 = pygame.image.load('map//images//img_of_sword.png')
        self.clock = pygame.time.Clock()

        self.x = 50  # Начальные координаты игрока
        self.y = 190

        self.x_new = self.x  # Будущие координаты курсора мыши пока равны координатам игрока
        self.y_new = self.y

        self.speed = 1  # Скорость перемещения персонажа

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.button_pressed = False

        self.animation_count = 0

        self.game = True
        self.screen.blit(self.player_stand, (self.x, self.y))

    def handle_events(self):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            # event: keydown
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 - означает левую кнопку мыши
                    self.x_new, self.y_new = event.pos  # Координаты точки, где находиться курсор
                    self.button_pressed = True  # Левая кнопка мыши нажата
            elif event.type == KEYDOWN:
                # exit on Escape
                if event.key == K_ESCAPE:
                    self.done = True
                # toggle bool
                elif event.key == K_s:
                    self.map.scrolling = not self.map.scrolling
                elif event.key == K_SPACE:
                    # random map
                    self.map.randomize()

            # elif event.type == MOUSEMOTION:
            # self.map.scroll(event.rel)
        if self.button_pressed:
            '''Если левая кнопка мыши нажата, то вызываем функцию и персонаж начинает перемещаться в точку,
                где находился курсор при нажатии'''
            self.player()  # Вызываем функциию игрока

    def draw(self):

        self.screen.fill(Color("black"))
        self.map.draw()
        pygame.display.flip()

    def okno(self):
        global warning
        global color, text
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        font = pygame.font.Font(None, 33)
        text_1 = font.render('Введите имя вашего персонажа', True, (255, 255, 255))
        self.screen.blit(text_1, (220, 200))
        pygame.draw.rect(self.screen, (153, 102, 5),
                         (self.x / 4, self.y / 4, self.x // 2, self.y // 2), 5)
        pygame.draw.rect(self.screen, color, self.rec, 0)
        pygame.draw.rect(self.screen, (153, 102, 5), (self.x // 2 - 80, self.y // 2 - 30, 160, 60))
        text_1 = font.render('Подтвердить', True, (255, 255, 255))
        self.screen.blit(text_1, (self.x // 2 - 75, self.y // 2 - 15))

        txt = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(txt, (self.rec.x + 5, self.rec.y + 5))

        font_0 = pygame.font.Font(None, 20)
        text_0 = font_0.render(warning, True, (255, 0, 0))
        self.screen.blit(text_0, (270, 2 * (self.y / 3) + 20))
