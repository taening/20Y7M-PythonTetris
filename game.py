from view import *
from music import *


class Game(object):
    def __init__(self):
        self.__run_game = True
        self.__fps = 100
        self.__music = Music()
        self.__idx = -1

    def run(self):
        # If this loop is end then all game is over.
        while self.__run_game:
            # Initial view is menu(idx=-1), menu return Index(-1~3)
            if self.__idx == -1:
                menu = MenuView()
                self.__idx = menu.run()
            elif self.__idx == 0:
                starter = GameStarterView()
                starter.run()
            elif self.__idx == 1:
                description = DescriptionView()
                self.__idx = description.run()
            elif self.__idx == 2:
                setting = SettingView()
                self.__idx = setting.run()
            elif self.__idx == 3:
                end = EndView()
                self.__idx = end.run()
            else:
                raise IndexError


if __name__ == '__main__':
    game = Game()
    game.run()
