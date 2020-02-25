import numpy as np


class Block(object):
    def __init__(self, color, pattern):
        self.__color = color
        self.__pattern = pattern

    def get_color(self):
        return self.__color

    def get_pattern(self, direction=0):
        if direction != 0:
            return [[-b[1]*direction, b[0]*direction] for b in self.__pattern]
        return self.__pattern

    def rotate(self):
        self.__pattern = self.get_pattern(-1)    # direction=1 : Clockwise && direction=-1 : Counterclockwise


class OBlock(Block):
    def __init__(self):
        super().__init__((255, 0, 0), np.array([[0, 0], [1, 0], [0, 1], [1, 1]]))


class IBlock(Block):
    def __init__(self):
        super().__init__((0, 255, 0), np.array([[-1, 0], [0, 0], [1, 0], [2, 0]]))


class SBlock(Block):
    def __init__(self):
        super().__init__((0, 0, 255), np.array([[-1, 0], [0, 0], [0, 1], [1, 1]]))


class ZBlock(Block):
    def __init__(self):
        super().__init__((255, 255, 0), np.array([[0, 0], [1, 0], [0, 1], [-1, 1]]))


class LBlock(Block):
    def __init__(self):
        super().__init__((255, 0, 255), np.array([[-1, 0], [0, 0], [1, 0], [-1, 1]]))


class JBlock(Block):
    def __init__(self):
        super().__init__((0, 255, 255), np.array([[-1, 0], [0, 0], [1, 0], [1, 1]]))


class TBlock(Block):
    def __init__(self):
        super().__init__((255, 20, 147), np.array([[-1, 0], [0, 0], [1, 0], [0, 1]]))
