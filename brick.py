import pygame as pg
import constants


class Brick(pg.sprite.Sprite):
    def __init__(self, x, y, img_path):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(img_path).convert()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
