import pygame as pg
import constants


class Ball(pg.sprite.Sprite):
    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(constants.BALL_DIR).convert()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (constants.WIDTH / 2, constants.HEIGHT / 2)
        self.speedx = 5
        self.speedy = 5
        self.score = 0

        self.player = player

    def update(self):
        self.check_walls()
        self.check_bricks()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def check_walls(self):
        if self.rect.x >= 790 or self.rect.x <= 0:
            self.speedx *= -1

        if pg.sprite.collide_rect(self, self.player):
            self.speedy *= -1

        if self.rect.y < 0:
            self.speedy *= -1

        if self.rect.y > 600:
            self.player.is_dead = True
            self.rect.x = 400
            self.rect.y = 300

    def check_bricks(self):
        if pg.sprite.spritecollide(self, constants.brick_sprites, True, collided=None):
            self.speedy *= -1

        if pg.sprite.spritecollide(self, constants.laser_bricks, True, collided=None):
            self.speedy *= -1
            self.player.can_shoot = True
