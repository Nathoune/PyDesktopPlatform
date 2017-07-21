'''
Created on 21 juil. 2017

@author: dubusster
'''

import pygame
from pygame.locals import (K_RIGHT,
                           K_LEFT,
                           K_UP,
                           K_DOWN,
                           K_ESCAPE,
                           )
from path import Path
from physics.core import Block, Character
import random

DATA_FOLDER = Path("data")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# from https://stackoverflow.com/questions/19963271/pygame-display-multiple-images-randomly
##########################################################################


class Game(object):

    def __init__(self, size=(1024, 600)):

        pygame.init()

        self.screen = pygame.display.set_mode(size)

        self.background = pygame.image.load(
            DATA_FOLDER / "background.jpg").convert()

        self.acceleration = 1

        self.player = Character("pikachu",
                                speed=10,
                                image=DATA_FOLDER / "pikachu.png",
                                x=(1024 - 100) / 2,
                                y=(600 - 100) / 2)
        self.blocks = []

        # create 3 blocks randomly disposed

        for i in range(3):
            randx = random.randint(0, size[0])
            randy = random.randint(0, size[1])
            block = Block(DATA_FOLDER / "folder-icon.jpg", x=randx, y=randy)
            self.blocks.append(block)

    #####################

    def run(self):

        clock = pygame.time.Clock()
        RUNNING = True

        while RUNNING:
            # prevents from falling underground
            if self.player.rect.bottom <= self.screen.get_height():
                self.player.move(0, self.acceleration)
            pygame.event.get()
            # --- events ---

            keys = pygame.key.get_pressed()  # Etat du clavier au moment t
            if keys[K_RIGHT]:
                self.player.move(2, 0)
            if keys[K_LEFT]:
                self.player.move(-2, 0)
            if keys[K_UP]:
                self.player.move(0, -2)
            if keys[K_DOWN]:
                self.player.move(0, 2)
            if keys[K_ESCAPE]:
                RUNNING = False
                # changes position when key is pressed

            self.player.update()

            # --- updates ----

            # place for updates

            # --- draws ---
            self.screen.fill(BLACK)
            self.screen.blit(self.background, self.background.get_rect())
            self.player.draw(self.screen)
            for block in self.blocks:
                block.draw(self.screen)

            pygame.display.flip()

            # --- FPS ---

            clock.tick(30)

        # --- quit ---

        pygame.quit()


if __name__ == '__main__':
    g = Game()
    g.run()
