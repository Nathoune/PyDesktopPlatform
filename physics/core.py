'''
Created on 20 juil. 2017

Defines objects to be used in the physics engine.
So far :
    - Position
    - Speed

@author: dubusster
'''


class Entity(object):
    '''
    Super class that will be used to create objects in space

    '''

    def __init__(self, name, pos_x=0, pos_y=0, win_x=1024, win_y=600):
        self.name = name
        self.position = Position()
        self.position.init(pos_x, pos_y)
        self.speed = Speed()
        self.win_size = (win_x, win_y)

    def move(self):
        win_x, win_y = self.win_size
        self.position.edit(self.speed, win_x, win_y, self.x, self.y)


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
