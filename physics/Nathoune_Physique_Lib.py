# coding: utf-8
# 1st attempt to create a Physique engine in python
# Designed to be used with pygame
# Created on 12/07/2017
#
# By Nathoune


#if 'pygame' not in sys.modules
import pygame as pg
#
#if 'math' not in sys.modules
import math

#############################################
################ DEFINES ####################
#############################################


#############################################


#############################################
################# CLASSES ###################
#############################################

class Vector():
    norme=0
    angle=0
    dx=0
    dy=0

    def init(self, x, y):
        self.dx=x
        self.dy=y
        self.norme=math.sqrt(x*x+y*y)
        self.angle=math.acos(x/self.norme)


#
#    def initNA(self, n, a):
#        self.norme=n
#        self.angle=a
#
#
#
#    def calculPointRelatif(self):
#        relativPoint=[]
#        relativPoint[0]=math.cos(self.angle)*self.norme
#        relativPoint.append(math.sin(self.angle)*self.norme)
#        return (relativPoint)
#
#    def calculPointsAbsolu(self, origine):
#        absolutePoint=[]
#        absolutePoint[0].append(origine[0])
#        absolutePoint[0].append(origine[1])
#        absolutePoint.append([])
#        absolutePoint[1].append((math.cos(self.angle)*self.norme) + origine[0])
#        absolutePoint[1].append((math.sin(self.angle)*self.norme) + origine[1])
#
######################

class Force():
    data=Vector()

    def computeFromAcc(self, acceleration, masse):
        self.data.init(acceleration.data.dx*masse, acceleration.data.dy*masse)

######################

class Acceleration():
    data=Vector()


    def computeFromForces(self, masse, forces):
        sommeF=Vector()
        sommeF.init(0,0)
        for i in len(forces):
            sommeF.init(sommeF.dx+forces[i].data.dx, sommeF.dy+forces[i].data.dy)

        self.data.init(sommeF.dx/masse, sommeF.dy/masse)


######################

class Vitesse():
    data=Vector()
    maximum=1000

    def compute(self, acceleration):
        if self.data.norme!=maximum:
            self.data.init(self.data.dx+acceleration.data.dx, self.data.dy+acceleration.data.dy)

######################

class Position():
    x=0
    y=0

    def compute(self, vitesse):
        self.x+=vitesse.data.dx
        self.y+=vitesse.data.dy


######################

class HitBox():
    sizeX=0
    sizeY=0


######################

class Item():
    hitbox=HitBox()
    #image=pg.image()
    masse=0
    gravityCenterX=0      # coordonnée relative du centre de gravité par rapport au coin supérieur gauche (origine spread)
    gravityCenterY=0
    acceleration=Acceleration()
    vitesse=Vitesse()



    def init(self, importMasse, importImage, importForces): #TODO check Hitbox management
        #self.image.load(importImage, (0,0))
        self.masse=importMasse
        self.acceleration.init()
        #self.hitbox.sizeX=
        #self.hitbox.sizeY=
        #self.gravityCenterX= usefull ?
        #self.gravityCenterY= usefull ?
