# coding: utf-8
# Created on 9/07/17
# 1st attempt to code PyGame
# By Nathoune

import numpy as np
import math
import pygame as pg
from pygame.locals import *
import time
import sys

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

################################################
################################################

class Speed():
    y=0
    x=0

    def init(self):
        self.y=0
        self.x=0

    def edit(self,newX,newY):
        self.x=newX
        self.y=newY

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
position=Position()
speed=Speed()

screen = pg.display.set_mode((WINDOWS_SIZE_X,WINDOWS_SIZE_Y))
pikachu=pg.image.load('Pikachu-As-Ninja.png')
pikachu=pg.transform.scale(pikachu, (PIKACHU_SIZE_X, PIKACHU_SIZE_Y))

speed.init()
position.init()


screen.blit(pikachu, (position.x,position.y))
pg.display.flip()

################################################
################################################

while 1:

    for event in pg.event.get():        # liste des évenements utilisateurs
        #event=pg.event.poll()          # récupère le premier event
        if  hasattr(event, 'key'):      # Event clavier
            if event.type == KEYDOWN :  # appui touche
                if event.key == K_RIGHT: speed.edit(2,0)
                elif event.key == K_LEFT: speed.edit(-2,0)
                elif event.key == K_UP: speed.edit(0,-2)
                elif event.key == K_DOWN: speed.edit(0,2)
                elif event.key == K_ESCAPE: sys.exit(0)     # quit the game
            elif event.type == KEYUP :  # relachement touche
                speed.edit=(0,0)

    position.edit(speed)
    screen.fill(BACK_COLOR)
    screen.blit(pikachu, (position.x, position.y))
    pg.display.flip()
