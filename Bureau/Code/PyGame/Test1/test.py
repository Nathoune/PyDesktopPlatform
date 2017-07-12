# coding: utf-8
# Created on 9/07/17
# 1st attempt to code PyGame
# VI ADVENTURE
# on 11/07/2017 : Masses modifs...

# By Nathoune

import numpy as np
import math
import pygame as pg
from pygame.locals import *
import time

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

class Speed():
    x=0
    y=0

    def init(self):
        self.x=0
        self.y=0

    def edit(self,newX,newY):
        self.x+=newX
        self.y+=newY

#######################

class Position():
    y=0
    x=0

    def init(self):
        self.y=INITIAL_Y_POS
        self.x=INITIAL_X_POS

    def edit(self, speed):
        if self.x+speed.x<WINDOWS_SIZE_X-PIKACHU_SIZE_X and self.x+speed.x>0 :
            self.x+=speed.x
        if self.y+speed.y<WINDOWS_SIZE_Y-PIKACHU_SIZE_Y and self.y+speed.y>0 :
            self.y+=speed.y

################################################
################################################
# Time Handler
clock = pg.time.Clock()


position=Position()
speed=Speed()

screen = pg.display.set_mode((WINDOWS_SIZE_X,WINDOWS_SIZE_Y))
pikachu=pg.image.load('Pikachu-As-Ninja.png')
pikachu=pg.transform.scale(pikachu, (PIKACHU_SIZE_X, PIKACHU_SIZE_Y))

speed.init()
position.init()

# Refresh screen
screen.blit(pikachu, (position.x,position.y))
pg.display.flip()

################################################
################################################
run=1

while run:

    clock.tick(30)

    pg.event.get()

    keys = pg.key.get_pressed()             # Etat du clavier au moment t
    if keys[K_RIGHT]: speed.edit(2,0)
    if keys[K_LEFT]: speed.edit(-2,0)
    if keys[K_UP]: speed.edit(0,-2)
    if keys[K_DOWN]: speed.edit(0,2)
    if keys[K_ESCAPE] : run=0


    position.edit(speed)
    # Clean sreen
    screen.fill(BACK_COLOR)
    #Refresh screen
    screen.blit(pikachu, (position.x, position.y))
    pg.display.flip()
    speed.init()
