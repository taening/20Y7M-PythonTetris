from block import *
from copy import deepcopy
import random as rd
import time as t


class BlockGenerator(object):
    def __init__(self):
        rd.seed(t.time())
        self.__queue = list()
        self.__block_info = [OBlock(), IBlock(), SBlock(), ZBlock(), LBlock(), JBlock(), TBlock()]

    def generate(self):
        if len(self.__queue) == 0:
            now = rd.randint(0, len(self.__block_info) - 1)
            self.__queue.append(deepcopy(self.__block_info[now]))
            nxt = rd.randint(0, len(self.__block_info) - 1)
            self.__queue.append(deepcopy(self.__block_info[nxt]))
        else:
            nxt = rd.randint(0, len(self.__block_info) - 1)
            self.__queue.append(deepcopy(self.__block_info[nxt]))
        return self.__queue.pop(0)

