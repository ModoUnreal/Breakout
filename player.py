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

        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()

        self.can_shoot = False
        self.shoot_var = 0

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -7

        if keystate[pg.K_RIGHT]:
            self.speedx = 7
        if keystate[pg.K_SPACE] and self.can_shoot:
            self.lasers()
        if self.shoot_var == 6:
            self.can_shoot = False
            self.shoot_var = 0

        self.rect.x += self.speedx

    def lasers(self):
        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.shoot_var += 1
            self.last_shot = now
            bullet = Bullet(self.rect.x + 10, self.rect.y)
            constants.bullet_sprites.add(bullet)
            bullet = Bullet(self.rect.x + 150, self.rect.y)
            constants.bullet_sprites.add(bullet)


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 50))
        self.image.fill(constants.ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedy = -5

    def update(self):
        self.check_bricks()
        if self.rect.y < 0:
            self.kill()
        self.rect.y += self.speedy

    def check_bricks(self):
        if pg.sprite.spritecollide(self, constants.brick_sprites, True, collided=None):
            self.kill()
        if pg.sprite.spritecollide(self, constants.laser_bricks, True, collided=None):
            self.kill()
