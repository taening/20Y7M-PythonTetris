from view import *
from music import *


class Game(object):
    def __init__(self):
        self.__run_game = True
        self.__fps = 100
        self.__music = Music()
        self.__idx = -1

    def run(self):
        # Resource File Directory Path
        ws = os.path.join(os.getcwd(), "resource")

        # If this loop is end then all game is over.
        while self.__run_game:
            # Initial view is menu(idx=-1), menu return Index(-1~3)
            if self.__idx == -1:
                menu = MenuView()
                self.__music.play(ws + "/music/BGM_MENU.wav")
                self.__idx = menu.run()
                self.__music.stop()
            elif self.__idx == 0:
                starter = GameStarterView()
                self.__music.play(ws + "/music/BGM_GAME.wav")
                starter.run()
                self.__music.stop()
            elif self.__idx == 1:
                description = DescriptionView()
                self.__music.play(ws + "/music/BGM_MENU.wav")
                self.__idx = description.run()
                self.__music.stop()
            elif self.__idx == 2:
                setting = SettingView()
                self.__music.play(ws + "/music/BGM_MENU.wav")
                self.__idx = setting.run()
                self.__music.stop()
            elif self.__idx == 3:
                end = EndView()
                self.__music.play(ws + "/music/BGM_EXIT.wav")
                self.__idx = end.run()
                self.__music.stop()
            else:
                raise IndexError


if __name__ == '__main__':
    game = Game()
    game.run()
