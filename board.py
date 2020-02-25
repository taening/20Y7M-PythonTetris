from block import *
import pygame as pg


class GameBoard(object):
    def __init__(self):
        self.__width = 10   # col=width=10
        self.__height = 20  # row=height=20
        self.__channel = 3  # RGB Channel
        self.__board = np.zeros((self.__height, self.__width, self.__channel))
        self.__block = None
        self.__pre_coordinates = list()
        self.__pos_x, self.__pos_y = self.__width//2, 0
        self.__bottom = False
        pg.time.set_timer(pg.USEREVENT, 1000)

    def get_board(self):
        return self.__board

    def is_bottom(self):
        if self.__bottom is True:
            self.__bottom = False
            return True
        else:
            return False

    def __is_collision(self, offset, direction=0):
        for b in self.__block.get_pattern(direction):
            y, x = self.__pos_y + b[1] + offset[1], self.__pos_x + b[0] + offset[0]
            if (x < 0 or x > self.__width - 1) or y < 0 or y > self.__height - 1:
                return True
        return False

    def __settle(self):
        for b in self.__block.get_pattern():
            y, x = self.__pos_y + b[1], self.__pos_x + b[0]
            self.__board[y][x] = self.__block.get_color()

        self.__bottom = True
        self.__pos_x, self.__pos_y = self.__width // 2, 0
        self.__block = None
        self.__pre_coordinates.clear()

    def register(self, block):
        if not isinstance(block, Block):
            raise TypeError
        self.__block = block

        # Delete previous coordinates on GameBoard
        if len(self.__pre_coordinates) != 0:
            for p in self.__pre_coordinates:
                self.__board[p[1]][p[0]] = (0, 0, 0)
            self.__pre_coordinates.clear()

        # Update current coordinates on GameBoard
        for b in self.__block.get_pattern():
            y, x = self.__pos_y + b[1], self.__pos_x + b[0]
            self.__board[y][x] = self.__block.get_color()
            self.__pre_coordinates.append([x, y])

    def movement(self):
        # Move block to next coordinates

        if pg.key.get_pressed()[pg.K_LEFT] == 1 and not self.__is_collision((-1, 0)):
            self.__pos_x -= 1
        if pg.key.get_pressed()[pg.K_RIGHT] == 1 and not self.__is_collision((1, 0)):
            self.__pos_x += 1
        if pg.key.get_pressed()[pg.K_DOWN] == 1 and not self.__is_collision((0, 1)):
            self.__pos_y += 1

        for evt in pg.event.get():
            if evt.type == pg.KEYDOWN:
                if evt.key == pg.K_UP and not self.__is_collision((0, 0), 1):
                    self.__block.rotate()
                if evt.key == pg.K_SPACE:
                    while not self.__is_collision((0, 1)):
                        self.__pos_y += 1
            elif evt.type == pg.USEREVENT and not self.__is_collision((0, 1)):
                self.__pos_y += 1


if __name__ == '__main__':
    pass
