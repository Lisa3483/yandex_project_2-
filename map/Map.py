import pygame
from pygame.locals import *
from pygame import Rect
from F_draw_map import read_tiles
import numpy as np

from random import randint
import os

debug = False  # display map as text

TILE_W = 16
TILE_H = 16


class Map:
    """stores map info, and draws tiles.
    Map is stored as an array of int's which correspond to the tile id."""

    def __init__(self, game):
        """set default map"""
        self.game = game
        self.screen = game.screen

        self.scrolling = True

        self.load_tileset("tileset2.bmp")

        self.reset()
        self.randomize()

    def scroll(self, rel):
        """scroll map using relative coordinates"""
        if not self.scrolling: return

        self.offset = (
            self.offset[0] + rel[0],
            self.offset[1] + rel[1])

        print(self.offset)
        print(1)

    def load_tileset(self, image="tileset2.bmp"):
        """load tileset image"""
        self.tileset = pygame.image.load('images/tileset2.bmp')
        self.rect = self.tileset.get_rect()

        # def load_tileset_plants(self, image="plants.bmp"):
        """load tileset image"""

    # self.tileset_plants = pygame.image.load(os.path.join("images", image)).convert()
    # self.rect_plants = self.tileset.get_rect()

    def reset(self):
        """clear map, reset to defaults."""
        # calculate number of tiles to fill the screen

        """screen size:
        self.tiles_x = self.game.width / TILE_W
        self.tiles_y = self.game.height / TILE_H
        """
        # or fixed size
        self.tiles_x, self.tiles_y = 60, 60

        # create empty array, fill with zeros.                  array[tiles_x, tiles_y]
        self.tiles = np.zeros((self.tiles_x, self.tiles_y), dtype=int)
        if debug:
            print("\n-- self.tiles = --\n", self.tiles)

    def randomize(self):
        """sets tiles to random values"""
        self.offset = (-50, -200)
        # randomize all tiles
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                self.tiles[x, y] = 1

        # example of 2d array slicing, ex: slicing whole column or row
        # set a couple roads: one horizontal, one vertical.
        # self.tiles[1, :] = TILE_ID_ROAD
        # self.tiles[:, 2] = TILE_ID_ROAD

        self.tiles = read_tiles('output.txt')
        if debug:
            print("\n-- self.tiles = --\n", self.tiles)

    def draw(self):
        '''# loop all tiles, and draw
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                # draw tile at (x,y)


                # get rect() to draw only tile from the tileset that we want

                dest = Rect(x * TILE_W, y * TILE_H, TILE_W, TILE_H)
                src = Rect(tile * TILE_W, 0, TILE_W, TILE_H)
                # note, for scrolling tiles, uncomment:
                if self.scrolling:
                    dest.left += self.offset[0]
                    dest.top += self.offset[1]


                tile_rect = pygame.Rect(x * TILE_W, y * TILE_H, TILE_W, TILE_H)
                self.screen.blit(self.tiles, tile_rect, area=(tile * TILE_W, 0, TILE_W, TILE_H))'''
        tile_width = 16
        tile_height = 16

        level_map = [
            [95, 96, 96, 96, 96, 96, 96, 96, 100],
            [85, 88, 88, 88, 88, 88, 88, 88, 92],
            [85, 88, 92, 79, 80, 78, 85, 88, 92],
            [85, 88, 92, 69, 70, 68, 85, 88, 92],
            [85, 88, 92, 59, 60, 58, 85, 88, 92],
            [85, 88, 92, 51, 52, 50, 85, 88, 92]
        ]

        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                dest = Rect(x * TILE_W, y * TILE_H, TILE_W, TILE_H)

                if self.scrolling:
                    dest.left += self.offset[0]
                    dest.top += self.offset[1]

                # tile_rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)
                self.screen.blit(self.tileset, dest, area=(tile * tile_width, 0, tile_width, tile_height))
