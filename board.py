from block import *
import pygame as pg


class GameBoard(object):
    def __init__(self):
        self.__board = np.zeros((20, 10))
        self.__bottom = False
        pg.time.set_timer(pg.USEREVENT, 1000)

    def is_bottom(self):
        return self.__bottom

    def register(self, block):
        if not isinstance(block, Block):
            raise TypeError

        if pg.key.get_pressed()[pg.K_LEFT] == 1:
            block.left()
        if pg.key.get_pressed()[pg.K_RIGHT] == 1:
            block.right()
        if pg.key.get_pressed()[pg.K_DOWN] == 1:
            block.down()

        for evt in pg.event.get():
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_SPACE:
                    block.drop()
                elif evt.key == pg.K_UP:
                    block.rotate()
                else:
                    pass
            elif evt.type == pg.USEREVENT:
                block.down()

        return self.__board


if __name__ == '__main__':
    pass
