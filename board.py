from block import *
from copy import deepcopy
import pygame as pg


class GameBoard(object):
    def __init__(self):
        self.__board = np.zeros((20, 10))
        self.__block = None
        self.__bottom = False
        self.__pre_coordinate = None
        pg.time.set_timer(pg.USEREVENT, 1000)

    def get_board(self):
        return self.__board

    def is_bottom(self):
        if self.__bottom is True:
            self.__bottom = False
            return True
        else:
            return False

    def register(self, block):
        if not isinstance(block, Block):
            raise TypeError
        self.__block = block

        # Delete previous coordinates
        if self.__pre_coordinate is not None:
            for row, col in self.__pre_coordinate:
                self.__board[row][col] = 0

        # Register new coordinates
        for row, col in self.__block.get_pattern():
            self.__board[row][col] = 1
        self.__pre_coordinate = deepcopy(self.__block.get_pattern())

    def movement(self):
        if pg.key.get_pressed()[pg.K_LEFT] == 1:
            self.__block.left()
        if pg.key.get_pressed()[pg.K_RIGHT] == 1:
            self.__block.right()
        if pg.key.get_pressed()[pg.K_DOWN] == 1:
            self.__block.down()

        for evt in pg.event.get():
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_SPACE:
                    self.__block.drop()
                elif evt.key == pg.K_UP:
                    self.__block.rotate()
                else:
                    pass
            elif evt.type == pg.USEREVENT:
                self.__block.down()


if __name__ == '__main__':
    pass
