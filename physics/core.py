'''
Created on 20 juil. 2017

Defines objects to be used in the phics engine.
So far :
    - Position
    - Speed

@author: dubusster
'''

class Speed(object):
    x=0
    y=0

    def init(self,x,y):
        self.x=0
        self.y=0

    def edit(self,newX,newY):
        self.x+=newX
        self.y+=newY

#######################

class Position(object):
    y=0
    x=0
    

    def init(self, x, y):
        self.y=y
        self.x=x

    def edit(self, speed, win_x, win_y, obj_x, obj_y):
        if self.x+speed.x<win_x-obj_x and self.x+speed.x>0 :
            self.x+=speed.x
        if self.y+speed.y<win_y-obj_y and self.y+speed.y>0 :
            self.y+=speed.y
