import numpy as np


class Block(object):
    def __init__(self, color, pattern):
        self.__color = color
        self.__pattern = pattern
        self.__idx = 0
        self.__len = len(pattern)

    def get_pattern(self):
        return self.__pattern[self.__idx]

    def get_color(self):
        return self.__color

    def left(self):
        for pt in self.__pattern:
            if pt[np.argmin(pt[:, 1])][1] > 0:
                pt[:, 1] -= 1

    def right(self):
        for pt in self.__pattern:
            if pt[np.argmax(pt[:, 1])][1] < 9:
                pt[:, 1] += 1

    def down(self):
        for pt in self.__pattern:
            if pt[np.argmax(pt[:, 0])][0] < 19:
                pt[:, 0] += 1
            # TODO: 경우 2 - 블록이 다른 블록 위에 올라오는 경우

    def drop(self):
        for pt in self.__pattern:
            while pt[np.argmax(pt[:, 0])][0] < 19:
                pt[:, 0] += 1

    def rotate(self):
        if self.__idx >= self.__len - 1:
            self.__idx = 0
        else:
            self.__idx += 1


class OBlock(Block):
    def __init__(self):
        super().__init__((255, 0, 0), np.array([
            [[0, 4], [0, 5], [1, 4], [1, 5]]
        ]))


class IBlock(Block):
    def __init__(self):
        super().__init__((0, 255, 0), np.array([
            [[0, 3], [0, 4], [0, 5], [0, 6]],
            [[0, 6], [1, 6], [2, 6], [3, 6]]
        ]))


class SBlock(Block):
    def __init__(self):
        super().__init__((0, 0, 255), np.array([
            [[0, 4], [0, 5], [1, 3], [1, 4]],
            [[0, 3], [1, 3], [1, 4], [2, 4]]
        ]))


class ZBlock(Block):
    def __init__(self):
        super().__init__((255, 255, 0), np.array([
            [[0, 3], [0, 4], [1, 4], [1, 5]],
            [[0, 4], [1, 3], [1, 4], [2, 3]]
        ]))


class LBlock(Block):
    def __init__(self):
        super().__init__((255, 0, 255), np.array([
            [[0, 3], [1, 3], [1, 4], [1, 5]],
            [[0, 3], [0, 4], [1, 3], [2, 3]],
            [[0, 3], [0, 4], [0, 5], [1, 5]],
            [[0, 5], [1, 5], [2, 4], [2, 5]],
        ]))


class JBlock(Block):
    def __init__(self):
        super().__init__((0, 255, 255), np.array([
            [[0, 5], [1, 3], [1, 4], [1, 5]],
            [[0, 3], [1, 3], [2, 3], [2, 4]],
            [[0, 3], [0, 4], [0, 5], [1, 3]],
            [[0, 4], [0, 5], [1, 5], [2, 5]]
        ]))


class TBlock(Block):
    def __init__(self):
        super().__init__((255, 20, 147), np.array([
            [[0, 3], [0, 4], [0, 5], [1, 4]],
            [[0, 5], [1, 4], [1, 5], [2, 5]],
            [[1, 4], [2, 3], [2, 4], [2, 5]],
            [[0, 3], [1, 3], [1, 4], [2, 3]]
        ]))
