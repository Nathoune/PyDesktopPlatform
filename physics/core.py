'''
Created on 20 juil. 2017

Defines objects to be used in the physics engine.
So far :
    - Position
    - Speed

@author: dubusster
'''

import pygame as pg


class Entity(object):
    '''
    Super class that will be used to create objects in space

    '''

    def __init__(self, name, image, x=0, y=0, size=(100, 100)):
        self.name = name
        self.size = size
        self.image = pg.image.load(image).convert()
        self.image = pg.transform.scale(self.image,
                                        size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.position = Position(x, y)

        self.speed = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value


class Block(Entity):
    def __init__(self, image, **kwargs):
        super(Block, self).__init__("Block", image, **kwargs)

    def move(self):
        '''
        Overriding method to prevent block from moving
        '''
        pass


class Character(Entity):
    def __init__(self, name, **kwargs):
        super(Character, self).__init__(name, **kwargs)

    def move(self, dx, dy):
        self.x += self.speed * dx
        self.y += self.speed * dy

    def update(self):
        self.rect.topleft = self.x, self.y


class Speed(object):

    def __init__(self, x=0, y=0):
        self.init(x, y)

    def init(self, x, y):
        self.x = x
        self.y = y

    def edit(self, newX, newY):
        self.x += newX
        self.y += newY

#######################


class Position(object):

    def __init__(self, x=0, y=0):
        self.init(x, y)

    def init(self, x, y):
        self.x = x
        self.y = y

    def edit(self, speed, win_x, win_y, obj_x, obj_y):
        if self.x + speed.x < win_x - obj_x and self.x + speed.x > 0:
            self.x += speed.x
        if self.y + speed.y < win_y - obj_y and self.y + speed.y > 0:
            self.y += speed.y
