from abc import *
from board import *
from generator import *
from pygame import image, font
import pygame as pg
import os


class View(metaclass=ABCMeta):
    pg.init()

    # Basic Color
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    SKY_BLUE = (135, 206, 235)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    MINT = (0, 255, 255)
    PINK = (255, 20, 147)
    GRAY = (128, 128, 128)

    # Basic Value
    _width = 800
    _height = 600

    # Resource Image
    ws = os.path.join(os.getcwd(), "resource")
    MENU = image.load(ws + "/img/menu_bg.jpg")
    GAME = image.load(ws + "/img/start_bg.jpg")
    DESCRIPTION = image.load(ws + "/img/description_bg.jpg")
    ICON = image.load(ws + "/img/icon.png")
    KEYBOARD = image.load(ws + "/img/방향키.png")
    ARROW = image.load(ws + "/img/arrow.jpg")

    # Font Setup
    SMALL = font.Font(ws + "/font/tetris_ft.TTF", 45)
    MEDIUM = font.Font(ws + "/font/tetris_ft.TTF", 70)
    LARGE = font.Font(ws + "/font/tetris_ft.TTF", 120)

    def __init__(self):
        pg.display.set_icon(self.ICON)
        pg.display.set_caption("Tetris Game")
        self._display = pg.display.set_mode((self._width, self._height))
        self._run_game = True
        self._clock = pg.time.Clock()
        self._fps = 30

    # 구현 - 이미지를 화면에 추가하는 메소드
    def _image_to_screen(self, img, w, h, pos):
        scaled_img = pg.transform.scale(img, (w, h))
        rect = scaled_img.get_rect()
        rect.center = pos
        return self._display.blit(scaled_img, rect)

    # 구현 - 텍스트를 화면에 추가하는 메소드
    def _text_to_screen(self, ft, text, color, pos):
        rendered_txt = ft.render(text, True, color)
        rect = rendered_txt.get_rect()
        rect.center = pos
        return self._display.blit(rendered_txt, rect)

    @abstractmethod
    def run(self):
        pass


class MenuView(View):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        return GameStarterView()

    def __visualize(self):
        pass


class GameStarterView(View):
    def __init__(self):
        super().__init__()
        self.__game_board = GameBoard()
        self.__block_generator = BlockGenerator()

    def run(self):
        # If this loop is end then one frame is over.
        while self._run_game:
            # Generate Random Block (return Block)
            block = self.__block_generator.generate()

            # Register and Visualize New Block To Board (return Board)
            while not self.__game_board.is_bottom():
                self.__game_board.register(block)
                self.__game_board.movement()
                self.__visualize()
                pg.display.update()
                self._clock.tick(self._fps)

    def __visualize(self):
        w, h = self._width, self._height
        self._display.fill(self.BLACK)
        self.GAME.set_alpha(50)
        _ = self._image_to_screen(self.GAME, w, h, (w // 2, h // 2))

        # Next Block Info Design
        _ = self._text_to_screen(self.SMALL, "NEXT", self.WHITE, (690, 100))
        _ = pg.draw.rect(self._display, self.WHITE, (590, 120, 200, 150), 3)

        # Score Info Design
        _ = self._text_to_screen(self.SMALL, "SCORE", self.WHITE, (110, 100))
        _ = self._text_to_screen(self.SMALL, str(0), self.YELLOW, (110, 150))
        _ = pg.draw.rect(self._display, self.WHITE, (10, 120, 200, 50), 3)

        # Level Info Design
        _ = self._text_to_screen(self.SMALL, "LEVEL", self.WHITE, (110, 250))
        _ = self._text_to_screen(self.SMALL, str(0), self.RED, (110, 300))
        _ = pg.draw.rect(self._display, self.WHITE, (10, 270, 200, 50), 3)

        # Lines Info Design
        _ = self._text_to_screen(self.SMALL, "LINES", self.WHITE, (110, 400))
        _ = self._text_to_screen(self.SMALL, str(0), self.PURPLE, (110, 450))
        _ = pg.draw.rect(self._display, self.WHITE, (10, 420, 200, 50), 3)

        # Game Board Design
        _ = pg.draw.rect(self._display, self.SKY_BLUE, (265, 50, 10, 500))
        _ = pg.draw.rect(self._display, self.SKY_BLUE, (525, 50, 10, 500))
        _ = pg.draw.rect(self._display, self.SKY_BLUE, (265, 550, 270, 10))

        # Game Board Guide Line Design
        for row in range(21):
            pg.draw.line(self._display, self.GRAY, (275, 50 + row * 25), (525, 50 + row * 25), 1)
            for col in range(11):
                pg.draw.line(self._display, self.GRAY, (275 + col * 25, 50), (275 + col * 25, 550), 1)

        # Draw Block
        for r, row in enumerate(self.__game_board.get_board()):
            for c, col in enumerate(row):
                if any(col) is True:
                    pg.draw.rect(self._display, (10, 10, 10), (275 + c * 25, 50 + r * 25, 25, 25))
                    pg.draw.rect(self._display, col, (275 + c * 25 + 1, 50 + r * 25 + 1, 24, 24))


class DescriptionView(View):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        pass

    def __visualize(self):
        pass


class SettingView(View):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        pass

    def __visualize(self):
        pass


class EndView(View):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        pass

    def __visualize(self):
        pass
