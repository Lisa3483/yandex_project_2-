import pygame

from The_battlefield import Thebattlefield


class Image(pygame.sprite.Sprite):
    bfelld = Thebattlefield(8, 16)
    image = bfelld.load_image("1705599505984pe8jdtcn.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Image.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        pass
