import pygame as pg
import constants


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(constants.PLAYER_DIR).convert()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (constants.WIDTH / 2, constants.HEIGHT - 20)
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5

        if keystate[pg.K_RIGHT]:
            self.speedx = 5

        self.rect.x += self.speedx
