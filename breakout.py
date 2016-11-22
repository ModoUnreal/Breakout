import pygame as pg
import random

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

color_list = [WHITE, BLACK, RED, BLUE]

"""Initialises pygame and creates a window"""
pg.init()
pg.font.init()
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
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((25, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 2.5
        self.speedy = 2.5
        self.score = 0

    def update(self):
        self.check_walls()
        self.check_bricks()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def check_walls(self):
        if self.rect.x >= 790 or self.rect.x <= 0:
            self.speedx *= -1

        if pg.sprite.collide_rect(self, player):
            self.speedy *= -1

        if self.rect.y > 600 or self.rect.y < 0:
            self.rect.x = 400
            self.rect.y = 300
            self.speedy *= -1

    def check_bricks(self):
        if pg.sprite.spritecollide(self, brick_sprites, True, collided=None):
            self.speedy *= -1
            self.score += 1

brick_sprites = pg.sprite.Group()


for i in range(16):
    brick = Brick(i * 50, 95, color=color_list[random.randint(0, 3)])
    brick_sprites.add(brick)

player = Player()
ball = Ball()
all_sprites = pg.sprite.Group()
ball_sprite = pg.sprite.Group()
all_sprites.add(player)
ball_sprite.add(ball)

score_font = pg.font.Font("vgafix.fon", 50)
score_text = score_font.render("Score: " + str(ball.score), 0, (50, 50, 25))

game_loop = True
while game_loop:

    """This will keep the loop running at 60 FPS"""
    CLOCK.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_loop = False

    all_sprites.update()
    brick_sprites.update()
    ball_sprite.update()
    score_text = score_font.render("Score: " + str(ball.score), 0, (50, 50, 25))

    SCREEN.fill(GREEN)
    all_sprites.draw(SCREEN)
    brick_sprites.draw(SCREEN)
    ball_sprite.draw(SCREEN)
    SCREEN.blit(score_text, (5, 10))
    pg.display.flip()

pg.font.quit()
pg.quit()
