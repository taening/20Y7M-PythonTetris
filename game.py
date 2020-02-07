from view import *
from music import *


class Game(object):
    def __init__(self):
        self.__run_game = True
        self.__fps = 100
        self.__music = Music()

    def run(self):
        # If this loop is end then all game is over.
        while self.__run_game:
            # TODO: Show View of Menu (return NextPage) (Set GameStarter because of early stage)
            menu = MenuView()
            nxt = menu.run()

            # Run each page selected by Menu
            if isinstance(nxt, GameStarterView):
                starter = GameStarterView()
                starter.run()
            elif isinstance(nxt, DescriptionView):
                description = DescriptionView()
                description.run()
            elif isinstance(nxt, SettingView):
                setting = SettingView()
                setting.run()
            elif isinstance(nxt, EndView):
                end = EndView()
                end.run()
            else:
                raise TypeError


if __name__ == '__main__':
    game = Game()
    game.run()
