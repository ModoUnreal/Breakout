import pygame as pg

"""CONSTANTS"""
WIDTH = 800
HEIGHT = 600
FPS = 60

"""COLORS"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

"""Initialises pygame and creates a window"""
pg.init()
pg.mixer.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Breakout")
CLOCK = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((70, 35))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 20)
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5

        if keystate[pg.K_RIGHT]:
            self.speedx = 5

        self.rect.x += self.speedx


class Brick(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

brick_sprites = pg.sprite.Group()


def level_1():
    for i in range(16):
        brick = Brick(i * 50, 95)
        brick_sprites.add(brick)

player = Player()
all_sprites = pg.sprite.Group()
all_sprites.add(player)

game_loop = True
while game_loop:

    """This will keep the loop running at 60 FPS"""
    CLOCK.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_loop = False

    level_1()

    all_sprites.update()
    brick_sprites.update()

    SCREEN.fill(GREEN)
    all_sprites.draw(SCREEN)
    brick_sprites.draw(SCREEN)
    pg.display.flip()

pg.quit()
