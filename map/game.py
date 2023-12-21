import pygame
from pygame.locals import *
from pygame import Color
#  from map import Map    
from map import Map

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


class Game():
    """game Main entry point. handles intialization of game and graphics.    
    members:
        map : map.Map() instance
    """
    done = False

    def __init__(self, width=640, height=480):
        """Initialize PyGame"""
        pygame.init()
        self.width, self.height = width, height

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(GAME_TITLE)

        self.map = Map(self)
        self.draw_hero()

        print(GAME_TITLE)
        print(GAME_ABOUT)
        print(GAME_HOTKEYS)

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

        pygame.display.update()

    def player(self):
        # Все переменные, которые будут использоваться не только в этой функции, объявляем как глобальные

        if self.x != self.x_new or self.y != self.y_new:
            '''Условие, если координата x игрока не равна координате x курсора 
            или координата y игрока не равна координате y курсора'''
            if self.x != self.x_new and self.y != self.y_new:
                '''Повторяется это условие, для того, чтобы под каждое перемещение персонажа 
                (вверх, вниз, влево, вправо) сделать анимацию'''
                if self.x > self.x_new and self.y > self.y_new:
                    '''Условие, если координата x игрока больше координаты x курсора 
                или координата y игрока больше координаты y курсора'''
                    self.left = True  # Отрисовываем анимацию перемещения влево
                    self.right = False
                    self.down = False
                    self.up = False
                    self.x -= self.speed  # Перемещаем персонажа влево
                    self.y -= self.speed  # И одновременно перемещаем его вверх
                    self.map.scroll([self.speed, 0])
                elif self.x < self.x_new and self.y < self.y_new:
                    self.left = False
                    self.right = True  # Отрисовываем анимацию перемещения вправо
                    self.down = False
                    self.up = False
                    self.x += self.speed  # Перемещаем персонажа вправо
                    self.y += self.speed  # И одновременно перемещаем его вниз
                    self.map.scroll([self.speed, 0])
                elif self.x < self.x_new and self.y > self.y_new:
                    self.left = False
                    self.right = True  # Отрисовываем анимацию перемещения вправо
                    self.down = False
                    self.up = False
                    self.x += self.speed  # Перемещаем персонажа вправо
                    self.y -= self.speed  # И одновременно перемещаем его вверх
                    self.map.scroll([self.speed, 0])
                elif self.x > self.x_new and self.y < self.y_new:
                    self.left = True  # Отрисовываем анимацию перемещения влево
                    self.right = False
                    self.down = False
                    self.up = False
                    self.x -= self.speed  # Перемещаем персонажа влево
                    self.y += self.speed  # И одновременно перемещаем его вниз
                    self.map.scroll([self.speed, 0])
            elif self.y != self.y_new:
                if self.y < self.y_new:
                    self.left = False
                    self.right = False
                    self.down = True  # Отрисовываем анимацию перемещения вниз
                    self.up = False
                    self.y += self.speed  # Перемещаем персонажа вниз
                    self.map.scroll([self.speed, 0])
                elif self.y > self.y_new:
                    self.left = False
                    self.right = False
                    self.down = False
                    self.up = True  # Отрисовываем анимацию перемещения вверх
                    self.y -= self.speed  # Перемещаем персонажа вверх
                    self.map.scroll([self.speed, 0])
            elif self.x != self.x_new:
                if self.x < self.x_new:
                    self.x += self.speed  # Перемещаем персонажа вправо
                    self.left = False
                    self.right = True  # Отрисовываем анимацию перемещения вправо
                    self.down = False
                    self.up = False
                    self.map.scroll([self.speed, 0])
                elif self.x > self.x_new:
                    self.x -= self.speed  # Перемещаем персонажа влево
                    self.left = True  # Отрисовываем анимацию перемещения влево
                    self.right = False
                    self.down = False
                    self.up = False
                    self.map.scroll([0, self.speed])
        else:
            self.left = False
            self.right = False
            self.down = False
            self.up = False

    def draw_hero(self):

        self.player_stand = pygame.image.load('hero_image//Hero_forward2.png')
        self.player_right = [pygame.image.load(f'hero_image//Hero_right{i}.png') for i in range(1, 4)]
        self.player_left = [pygame.image.load(f'hero_image//Hero_left{i}.png') for i in range(1, 4)]
        self.player_up = [pygame.image.load(f'hero_image//Hero_top{i}.png') for i in range(1, 4)]
        self.player_down = [pygame.image.load(f'hero_image//Hero_forward{i}.png') for i in range(1, 4)]

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
        """handle events."""
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

            elif event.type == MOUSEMOTION:
                self.map.scroll(event.rel)
        if self.button_pressed:
            '''Если левая кнопка мыши нажата, то вызываем функцию и персонаж начинает перемещаться в точку,
                где находился курсор при нажатии'''
            self.player()  # Вызываем функциию игрока

    def draw(self):
        """render screen"""
        self.screen.fill(Color("black"))
        self.map.draw()
        pygame.display.flip()
