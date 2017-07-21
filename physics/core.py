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

        self.speed = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.topleft = self.x, self.y

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
