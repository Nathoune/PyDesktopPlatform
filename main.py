# coding: utf-8
# Created on 9/07/17
# 1st attempt to code PyGame
# By Nathoune

import pygame as pg
from pygame.locals import (K_RIGHT,
                           K_LEFT,
                           K_UP,
                           K_DOWN,
                           K_ESCAPE,
                           )
from path import Path

from physics.core import Character, Block

################################################
################################################

DATA_FOLDER = Path("data")


################################################
################################################

WINDOWS_SIZE_X = 1024
WINDOWS_SIZE_Y = 600

PIKACHU_SIZE_X = 100
PIKACHU_SIZE_Y = 100

INITIAL_X_POS = (WINDOWS_SIZE_X - PIKACHU_SIZE_X) / 2
INITIAL_Y_POS = (WINDOWS_SIZE_Y - PIKACHU_SIZE_Y) / 2

MAX_X_SPEED = 20
MAX_Y_SPEED = 20

BACK_COLOR = (0, 0, 0)  # 0,0,0 = Black

FPS = 30

################################################
################################################


################################################
################################################
# Time Handler
clock = pg.time.Clock()

screen = pg.display.set_mode((WINDOWS_SIZE_X, WINDOWS_SIZE_Y))


pikachu = Character('Pikachu',
                    image=DATA_FOLDER / 'Pikachu-As-Ninja.png',
                    pos_x=INITIAL_X_POS,
                    pos_y=INITIAL_Y_POS)

block = Block(image=DATA_FOLDER / "folder-icon.jpg",
              pos_x=300,
              pos_y=300)

entities = [pikachu, block]

# Refresh screen
for entity in entities:
    screen.blit(entity.image, entity.size)

pg.display.flip()

################################################
################################################
run = True

while run:

    clock.tick(30)

    pg.event.get()

    keys = pg.key.get_pressed()  # Etat du clavier au moment t
    if keys[K_RIGHT]:
        pikachu.speed.edit(2, 0)
    if keys[K_LEFT]:
        pikachu.speed.edit(-2, 0)
    if keys[K_UP]:
        pikachu.speed.edit(0, -2)
    if keys[K_DOWN]:
        pikachu.speed.edit(0, 2)
    if keys[K_ESCAPE]:
        run = False

    pikachu.move()

    # Clean sreen
    screen.fill(BACK_COLOR)
    # Refresh screen
    for entity in entities:
        screen.blit(entity.image, entity.size)
    pg.display.flip()
    pikachu.speed.init(0, 0)
