import pygame
from pygame.locals import *
from pygame import Rect
from map.F_draw_map import read_tiles, read_col_tiles
import numpy as np
from Battle.The_battlefield import battle_window

debug = False

TILE_W = 16
TILE_H = 16
FLAG_ENEMY_1 = True
FLAG_ENEMY_2 = True


class Map:
    def __init__(self, game):

        self.game = game
        self.screen = game.screen

        self.scrolling = True
        self.collision_map = read_col_tiles("map/col_map.txt")

        self.load_tileset()
        self.reset()
        self.randomize()

    def flgs_1(self):
        FLAG_ENEMY_1 = False
        return FLAG_ENEMY_1

    def flgs_2(self):
        FLAG_ENEMY_2 = False
        return FLAG_ENEMY_2

    def scroll(self, rel):
        global FLAG_ENEMY_1, FLAG_ENEMY_2
        if not self.scrolling: return
        self.offset = (
            self.offset[0] + rel[0],
            self.offset[1] + rel[1])

        print(self.offset)
        if FLAG_ENEMY_1:
            if ((self.offset[0] * (-1) > 110) and (self.offset[0] * (-1) < 160)) and (self.offset[1] * (-1) > 300) and \
                    (self.offset[1] * (-1) < 350):
                print("на вас напали")
                battle_window(2)
                FLAG_ENEMY_1 = False

        if FLAG_ENEMY_2:
            if ((self.offset[0] * (-1) > 425) and (self.offset[0] * (-1) < 475)) and (self.offset[1] * (-1) > 125) and \
                    (self.offset[1] * (-1) < 175):
                print("на вас напали")
                battle_window(1)
                FLAG_ENEMY_2 = False

    def load_tileset(self):

        self.tileset = pygame.image.load('map/images/tileset2.bmp')
        self.rect = self.tileset.get_rect()

    def reset(self):
        self.tiles_x, self.tiles_y = 60, 60
        self.tiles = np.zeros((self.tiles_x, self.tiles_y), dtype=int)
        if debug:
            print("\n-- self.tiles = --\n", self.tiles)

    def randomize(self):
        self.offset = (-50, -200)
        # randomize all tiles
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                self.tiles[x, y] = 1

        self.tiles = read_tiles('map/map.txt')
        if debug:
            print("\n-- self.tiles = --\n", self.tiles)

    def draw(self):

        tile_width = 16
        tile_height = 16

        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                dest = Rect(x * TILE_W, y * TILE_H, TILE_W, TILE_H)

                if self.scrolling:
                    dest.left += self.offset[0]
                    dest.top += self.offset[1]

                self.screen.blit(self.tileset, dest, area=(tile * tile_width, 0, tile_width, tile_height))
