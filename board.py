from block import *
import pygame as pg


class GameBoard(object):
    def __init__(self):
        self.__board = np.zeros((20, 10))
        self.__bottom = False

    def is_bottom(self):
        return self.__bottom

    def __row_checker(self):
        pass

    def register(self, block):
        if not isinstance(block, Block):
            raise TypeError

        # TODO : Moving and Locking Code
        for evt in pg.event.get():
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_LEFT:
                    block.left()
                elif evt.key == pg.K_RIGHT:
                    block.right()
                elif evt.key == pg.K_DOWN:
                    block.down()
                elif evt.key == pg.K_SPACE:
                    block.drop()
                elif evt.key == pg.K_UP:
                    block.rotate()
                else:
                    continue
            elif evt.type == pg.KEYUP:
                pass
            else:
                continue

            # TODO: 블록이 밑에까지 내려오면, board에 등록하고, self.__bottom = True로 바꿔주어 register() 종료
        return self.__board


if __name__ == '__main__':
    pass
