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
        self.__idx = 0

    def __visualize(self):
        w, h, lst = self._width, self._height, list()
        _ = self._image_to_screen(self.MENU, w, h, (w // 2, h // 2))
        _ = self._text_to_screen(self.LARGE, "TETRIS", self.MINT, (w // 2, h * 0.25))
        lst.append(self._text_to_screen(self.SMALL, "START", self.RED, (w // 2, h * 0.45)))
        lst.append(self._text_to_screen(self.SMALL, "DESCRIPTION", self.GREEN, (w // 2, h * 0.55)))
        lst.append(self._text_to_screen(self.SMALL, "SETTING", self.BLUE, (w // 2, h * 0.65)))
        lst.append(self._text_to_screen(self.SMALL, "EXIT", self.PURPLE, (w // 2, h * 0.75)))
        self._image_to_screen(self.ARROW, 30, 30, (lst[self.__idx].midleft[0] * 0.93, lst[self.__idx].midleft[1]))

    def run(self):
        # If this loop is end then one frame is over.
        while self._run_game:
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    exit()
                elif evt.type == pg.KEYDOWN:
                    if evt.key == pg.K_UP:
                        if self.__idx <= 0:
                            self.__idx = 3
                        else:
                            self.__idx -= 1
                    elif evt.key == pg.K_DOWN:
                        if self.__idx >= 3:
                            self.__idx = 0
                        else:
                            self.__idx += 1
                    elif evt.key == pg.K_RETURN:
                        return self.__idx
                else:
                    continue
            self.__visualize()
            pg.display.update()
            self._clock.tick(60)


class GameStarterView(View):
    def __init__(self):
        super().__init__()
        self.__game_board = GameBoard()
        self.__block_generator = BlockGenerator()

    def __visualize(self, block, board):
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
        _ = pg.draw.rect(self._display, self.PURPLE, (265, 50, 10, 500))
        _ = pg.draw.rect(self._display, self.PURPLE, (525, 50, 10, 500))
        _ = pg.draw.rect(self._display, self.PURPLE, (265, 550, 270, 10))

        # Game Board Guide Line Design
        for row in range(21):
            pg.draw.line(self._display, self.GRAY, (275, 50 + row * 25), (525, 50 + row * 25), 1)
            for col in range(11):
                pg.draw.line(self._display, self.GRAY, (275 + col * 25, 50), (275 + col * 25, 550), 1)

        # Draw Active Block
        for pt in block.get_pattern():
            pg.draw.rect(self._display, block.get_color(), (275 + pt[1] * 25, 50 + pt[0] * 25, 25, 25))

        # Draw Inactive Block
        for bd in np.argwhere(board == 1):
            pg.draw.rect(self._display, self.GRAY, (275 + bd[1] * 25, 50 + bd[0] * 25, 25, 25))

    def run(self):
        # If this loop is end then one frame is over.
        while self._run_game:
            # Generate Random Block (return Block)
            block = self.__block_generator.generate()

            # Register and Visualize New Block To Board (return Board)
            while not self.__game_board.is_bottom():
                board = self.__game_board.register(block)
                self.__visualize(block, board)
                pg.display.update()
                self._clock.tick(30)


class DescriptionView(View):
    def __init__(self):
        super().__init__()

    def __visualize(self):
        w, h = self._width, self._height
        # Background Design
        self._display.fill(self.WHITE)
        self.DESCRIPTION.set_alpha(100)
        _ = self._image_to_screen(self.DESCRIPTION, w, h, (w // 2, h // 2))

        # Description Design
        _ = self._text_to_screen(self.MEDIUM, "게임 설명", self.BLACK, (w // 2, h // 2 - 250))
        _ = pg.draw.rect(self._display, (0, 0, 0), (w // 2 - 250, h // 2 - 220, 500, 3))

        # Arrow Keyboard Design
        _ = self._image_to_screen(self.KEYBOARD, 200, 100, (w // 2, h // 2 - 80))
        _ = self._text_to_screen(self.SMALL, "왼쪽 이동", self.BLACK, (w // 2 - 170, h // 2 - 50))
        _ = self._text_to_screen(self.SMALL, "오른쪽 이동", self.BLACK, (w // 2 + 170, h // 2 - 50))
        _ = self._text_to_screen(self.SMALL, "블록 회전", self.BLACK, (w // 2, h // 2 - 150))
        _ = self._text_to_screen(self.SMALL, "빠르게 떨어짐", self.BLACK, (w // 2, h // 2 + 10))

        # Space Keyboard Design
        _ = pg.draw.rect(self._display, (230, 230, 230), (w // 2 - 100, h // 2 + 90, 200, 45))
        _ = pg.draw.rect(self._display, self.BLACK, (w // 2 - 100, h // 2 + 90, 200, 45), 1)
        _ = self._text_to_screen(self.SMALL, "Spacebar", self.BLACK, (w // 2, h // 2 + 115))
        _ = self._text_to_screen(self.SMALL, "바로 떨어짐", self.BLACK, (w // 2, h // 2 + 180))

    def run(self):
        while self._run_game:
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    exit()
                elif evt.type == pg.KEYDOWN:
                    return -1
            self.__visualize()
            pg.display.update()
            self._clock.tick(60)


class SettingView(View):
    def __init__(self):
        super().__init__()

    def __visualize(self):
        w, h = self._width, self._height
        self._display.fill(self.BLACK)
        _ = self._text_to_screen(self.MEDIUM, "시스템 설정", self.WHITE, (w // 2, h // 2 - 250))
        _ = self._text_to_screen(self.MEDIUM, "해상도", self.WHITE, (w // 2 - 300, h // 2 - 150))
        _ = self._text_to_screen(self.SMALL, "배경음", self.WHITE, (w // 2 - 300, h // 2 - 100))
        _ = pg.draw.rect(self._display, self.WHITE, (w // 2 - 200, h // 2 - 120, 400, 40), 3)

    def run(self):
        while self._run_game:
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    exit()
            self.__visualize()
            pg.display.update()
            self._clock.tick(60)


class EndView(View):
    def __init__(self):
        super().__init__()
        self.__idx = 0

    def __visualize(self):
        w, h, lst = self._width, self._height, list()
        self._display.fill(self.BLACK)
        _ = self._text_to_screen(self.MEDIUM, "게임을 종료하시겠습니까?", self.RED, (w // 2, h // 2 - 100))
        lst.append(self._text_to_screen(self.SMALL, "YES", self.RED, (w // 2 - 80, h // 2 + 40)))
        lst.append(self._text_to_screen(self.SMALL, "NO", self.BLUE, (w // 2 + 80, h // 2 + 40)))
        self._image_to_screen(self.ARROW, 30, 30, (lst[self.__idx].midleft[0] * 0.95, lst[self.__idx].midleft[1]))

    def run(self):
        while self._run_game:
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    exit()
                elif evt.type == pg.KEYDOWN:
                    if evt.key == pg.K_LEFT:
                        if self.__idx <= 0:
                            self.__idx = 1
                        else:
                            self.__idx -= 1
                    elif evt.key == pg.K_RIGHT:
                        if self.__idx >= 1:
                            self.__idx = 0
                        else:
                            self.__idx += 1
                    elif evt.key == pg.K_RETURN:
                        if self.__idx == 0:
                            exit()
                        else:
                            return -1
                else:
                    continue
            self.__visualize()
            pg.display.update()
            self._clock.tick(60)
