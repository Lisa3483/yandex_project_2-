import pygame
import sys
from pygame.locals import *
from pygame import Color
#  from map import Map    
from map.Map import Map

GAME_ABOUT = """about:
    -using tileset and numpy 2D array for map data.
    -randomizes tiles, and creates roads

    -Howto set/get tile at loc=(x,y)
        tiles[x,y] = 2
        tileid = tiles[x,y]

"""
GAME_TITLE = "maptiles numpy {nin.example} "
GAME_HOTKEYS = """== Hotkeys! ===
    space = randomize tiles
    ESC    = quit
    s = toggle scrolling
"""

first_time = True

animation_count, speed, x, y, x_new, y_new = 0, 1, 50, 190, 0, 0
right, left, up, down = False, False, False, False
button_pressed = False
player_down, player_right, player_up, player_left, player_stand = '', '', '', '', ''


class Game:
    """game Main entry point. handles intialization of game and graphics.
    members:
        map : map.Map() instance
    """
    done = False

    def __init__(self, screen):
        """Initialize PyGame"""
        self.width, self.height = 800, 600

        self.clock = pygame.time.Clock()
        self.screen = screen
        pygame.display.set_caption(GAME_TITLE)
        self.flag = 7

        self.map = Map(self)
        self.draw_hero()

        self.main_loop()

    def okno(self):
        pass

    def all_events(self):
        pass

    def flagg(self):
        return self.flag

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw_window()  # Вызываем метод для отображения персонажа
            pygame.display.flip()  # Обновляем экран
            self.clock.tick(60)

    def draw_window(self):
        self.draw()
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

        pygame.display.update()

    def player(self):

        # Все переменные, которые будут использоваться не только в этой функции, объявляем как глобальные
        global animation_count, right, left, up, down, x, y, speed, x_new, y_new
        if x != x_new or y != y_new:
            '''Условие, если координата x игрока не равна координате x курсора 
            или координата y игрока не равна координате y курсора'''
            if x != x_new and y != y_new:
                '''Повторяется это условие, для того, чтобы под каждое перемещение персонажа 
                (вверх, вниз, влево, вправо) сделать анимацию'''
                if x > x_new and y > y_new:
                    '''Условие, если координата x игрока больше координаты x курсора 
                или координата y игрока больше координаты y курсора'''
                    left = True  # Отрисовываем анимацию перемещения влево
                    right = False
                    down = False
                    up = False
                    x -= speed  # Перемещаем персонажа влево
                    y -= speed  # И одновременно перемещаем его вверх
                    self.map.scroll([speed, speed])
                elif x < x_new and y < y_new:
                    left = False
                    right = True  # Отрисовываем анимацию перемещения вправо
                    down = False
                    up = False
                    x += speed  # Перемещаем персонажа вправо
                    y += speed  # И одновременно перемещаем его вниз
                    self.map.scroll([speed * (-1), speed * (-1)])
                elif x < x_new and y > y_new:
                    left = False
                    right = True  # Отрисовываем анимацию перемещения вправо
                    down = False
                    up = False
                    x += speed  # Перемещаем персонажа вправо
                    y -= speed  # И одновременно перемещаем его вверх
                    self.map.scroll([speed * (-1), speed])
                elif x > x_new and y < y_new:
                    left = True  # Отрисовываем анимацию перемещения влево
                    right = False
                    down = False
                    up = False
                    x -= speed  # Перемещаем персонажа влево
                    y += speed  # И одновременно перемещаем его вниз
                    self.map.scroll([speed, speed * (-1)])
            elif y != y_new:
                if y < y_new:
                    left = False
                    right = False
                    down = True  # Отрисовываем анимацию перемещения вниз
                    up = False
                    y += speed  # Перемещаем персонажа вниз
                    self.map.scroll([0, speed * (-1)])
                elif y > y_new:
                    left = False
                    right = False
                    down = False
                    up = True  # Отрисовываем анимацию перемещения вверх
                    y -= speed  # Перемещаем персонажа вверх
                    self.map.scroll([0, speed])
            elif x != x_new:
                if x < x_new:
                    x += speed  # Перемещаем персонажа вправо
                    left = False
                    right = True  # Отрисовываем анимацию перемещения вправо
                    down = False
                    up = False
                    self.map.scroll([speed * (-1), 0])
                elif x > x_new:
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

        global animation_count, right, left, up, down, x, y, x_new, y_new, speed, button_pressed, \
        player_down, player_right, player_up, player_left, player_stand
        player_stand = pygame.image.load('map//hero_image//Hero_forward2.png')
        player_right = [pygame.image.load(f'map//hero_image//Hero_right{i}.png') for i in range(1, 4)]
        player_left = [pygame.image.load(f'map//hero_image//Hero_left{i}.png') for i in range(1, 4)]
        player_up = [pygame.image.load(f'map//hero_image//Hero_top{i}.png') for i in range(1, 4)]
        player_down = [pygame.image.load(f'map//hero_image//Hero_forward{i}.png') for i in range(1, 4)]

        self.clock = pygame.time.Clock()

        x = 50  # Начальные координаты игрока
        y = 190

        x_new = x  # Будущие координаты курсора мыши пока равны координатам игрока
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
        """handle events."""
        global animation_count, right, left, up, down, x, y, speed, x_new, y_new, button_pressed
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            # event: keydown
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 - означает левую кнопку мыши
                    x_new, y_new = event.pos  # Координаты точки, где находиться курсор
                    button_pressed = True  # Левая кнопка мыши нажата
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
                elif event.key == K_f:
                    self.flag = 10
                    self.done = True

            # elif event.type == MOUSEMOTION:
            # self.map.scroll(event.rel)
        if button_pressed:
            '''Если левая кнопка мыши нажата, то вызываем функцию и персонаж начинает перемещаться в точку,
                где находился курсор при нажатии'''
            self.player()  # Вызываем функциию игрока

    def draw(self):
        """render screen"""
        self.screen.fill(Color("black"))
        self.map.draw()
        pygame.display.flip()

