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

from physics.core import Position, Speed

################################################ 
################################################

DATA_FOLDER = Path("data")


################################################
################################################

WINDOWS_SIZE_X=1024
WINDOWS_SIZE_Y=600

PIKACHU_SIZE_X=100
PIKACHU_SIZE_Y=100

INITIAL_X_POS=(WINDOWS_SIZE_X-PIKACHU_SIZE_X)/2
INITIAL_Y_POS=(WINDOWS_SIZE_Y-PIKACHU_SIZE_Y)/2

MAX_X_SPEED=20
MAX_Y_SPEED=20

BACK_COLOR=(0,0,0)  # 0,0,0 = Black

FPS=30

################################################
################################################


################################################
################################################
# Time Handler
clock = pg.time.Clock()


position=Position()
speed=Speed()

screen = pg.display.set_mode((WINDOWS_SIZE_X,WINDOWS_SIZE_Y))
pikachu=pg.image.load(DATA_FOLDER / 'Pikachu-As-Ninja.png')
pikachu=pg.transform.scale(pikachu, (PIKACHU_SIZE_X, PIKACHU_SIZE_Y))

speed.init(0,0)
position.init(INITIAL_X_POS, INITIAL_X_POS)

# Refresh screen
screen.blit(pikachu, (position.x,position.y))
pg.display.flip()

################################################
################################################
run=True

while run:

    clock.tick(30)

    pg.event.get()

    keys = pg.key.get_pressed()             # Etat du clavier au moment t
    if keys[K_RIGHT]: speed.edit(2,0)
    if keys[K_LEFT]: speed.edit(-2,0)
    if keys[K_UP]: speed.edit(0,-2)
    if keys[K_DOWN]: speed.edit(0,2)
    if keys[K_ESCAPE] : run=False


    position.edit(speed,
                  WINDOWS_SIZE_X,
                  WINDOWS_SIZE_Y,
                  PIKACHU_SIZE_X,
                  PIKACHU_SIZE_Y)
    # Clean sreen
    screen.fill(BACK_COLOR)
    #Refresh screen
    screen.blit(pikachu, (position.x, position.y))
    pg.display.flip()
    speed.init(0,0)
