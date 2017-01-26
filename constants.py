import pygame as pg
import os

"""HARDCODED CONSTANTS"""
WIDTH = 800
HEIGHT = 600
FPS = 60
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

"""COLORS"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


"""IMG DIRECTORY"""
BLUE_DIR = os.path.join("images", "blue.png")
GREEN_DIR = os.path.join("images", "green.png")
LIGHT_BLUE_DIR = os.path.join("images", "light_blue.png")
ORANGE_DIR = os.path.join("images", "orange.png")
PINK_DIR = os.path.join("images", "pink.png")
PURPLE_DIR = os.path.join("images", "purple.png")
RED_DIR = os.path.join("images", "red.png")
YELLOW_DIR = os.path.join("images", "yellow.png")
PLAYER_DIR = os.path.join("images", "player.png")
BALL_DIR = os.path.join("images", "ball.png")
"""SPRITE LISTS"""
all_sprites = pg.sprite.Group()
brick_sprites = pg.sprite.Group()
laser_bricks = pg.sprite.Group()
bullet_sprites = pg.sprite.Group()
# Bullet_sprites is found inside the player.py file
