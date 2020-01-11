from abc import *
from pygame import image, font
import pygame as pg
import os

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
GRAY = (128, 128, 128)

# Resoucre Image
ws = os.path.join(os.getcwd(), "resource")
MENU = image.load(ws + "/img/menu_bg.jpg")
GAME = image.load(ws + "/img/start_bg.jpg")
DESCRIPTION = image.load(ws + "/img/description_bg.jpg")
ARROW = image.load(ws + "/img/arrow.jpg")
ICON = image.load(ws + "/img/icon.png")
KEYBOARD = image.load(ws + "/img/방향키.png")

# Font Setup
SMALL = font.Font(ws + "/font/tetris_ft.TTF", 45)
MEDIUM = font.Font(ws + "/font/tetris_ft.TTF", 70)
LARGE = font.Font(ws + "/font/tetris_ft.TTF", 120)


# 게임에 필요한 기본적인 셋팅을 할 책임이 있는 객체
class Game(object):
    def __init__(self, fps=100):
        # 상태
        self.__fps = fps
        self.__clock = pg.time.Clock()

    # 메시지 - 게임을 실행하라
    def run(self, page):
        if not isinstance(page, Page):
            raise TypeError

        run = False
        while not run:
            # Event Handle
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    run = True
                else:
                    page.control(evt)
            page.show()
            self.__clock.tick(self.__fps)


# 게임에 필요한 UI를 만들고 조작할 책임이 있는 객체
class Page(metaclass=ABCMeta):
    pg.display.set_icon(ICON)
    pg.display.set_caption("Tetris Game")

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._display = pg.display.set_mode((width, height))
        self._rectangles = dict()

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
    def show(self):
        pass

    @abstractmethod
    def control(self, event):
        pass


class Menu(Page):
    # 메시지 - 메뉴창을 보여라
    def show(self):
        w, h, r = self._width, self._height, self._rectangles
        r.update({"bg": self._image_to_screen(MENU, w, h, (w//2, h//2))})
        r.update({"title": self._text_to_screen(LARGE, "TETRIS", MINT, (w//2, h*0.25))})
        r.update({"m1": self._text_to_screen(SMALL, "START", RED, (w//2, h*0.45))})
        r.update({"m2": self._text_to_screen(SMALL, "DESCRIPTION", GREEN, (w//2, h*0.55))})
        r.update({"m3": self._text_to_screen(SMALL, "SETTING", BLUE, (w//2, h*0.65))})
        r.update({"m4": self._text_to_screen(SMALL, "EXIT", PURPLE, (w//2, h*0.75))})
        pg.display.update()

    def control(self, event):
        e = event
        if e.type == pg.KEYUP:
            pass
        elif e.type == pg.MOUSEBUTTONUP:
            pass
        elif e.type == pg.KEYDOWN:
            pass
        elif e.type == pg.MOUSEBUTTONDOWN:
            pass


class Start(Page):
    def show(self):
        w, h, r = self._width, self._height, self._rectangles
        self._display.fill(BLACK)
        GAME.set_alpha(50)
        r.update({"bg": self._image_to_screen(GAME, w, h, (w//2, h//2))})

        # Next Block Info Design
        r.update({"next": self._text_to_screen(SMALL, "NEXT", WHITE, (690, 100))})
        r.update({"rect1": pg.draw.rect(self._display, WHITE, (590, 120, 200, 150), 3)})

        # Score Info Design
        r.update({"score": self._text_to_screen(SMALL, "SCORE", WHITE, (110, 100))})
        r.update({"value1": self._text_to_screen(SMALL, str(0), YELLOW, (110, 150))})
        r.update({"rect2": pg.draw.rect(self._display, WHITE, (10, 120, 200, 50), 3)})

        # Level Info Design
        r.update({"level": self._text_to_screen(SMALL, "LEVEL", WHITE, (110, 250))})
        r.update({"value2": self._text_to_screen(SMALL, str(0), RED, (110, 300))})
        r.update({"rect3": pg.draw.rect(self._display, WHITE, (10, 270, 200, 50), 3)})

        # Lines Info Design
        r.update({"lines": self._text_to_screen(SMALL, "LINES", WHITE, (110, 400))})
        r.update({"value3": self._text_to_screen(SMALL, str(0), PURPLE, (110, 450))})
        r.update({"rect4": pg.draw.rect(self._display, WHITE, (10, 420, 200, 50), 3)})

        # Game Board Design
        _ = pg.draw.rect(self._display, PURPLE, (265, 50, 10, 500))
        _ = pg.draw.rect(self._display, PURPLE, (525, 50, 10, 500))
        _ = pg.draw.rect(self._display, PURPLE, (265, 550, 270, 10))
        for row in range(21):
            pg.draw.line(self._display, GRAY, (275, 50 + row * 25), (525, 50 + row * 25), 1)
            for col in range(11):
                pg.draw.line(self._display, GRAY, (275 + col * 25, 50), (275 + col * 25, 550), 1)
        pg.display.update()

    def control(self, event):
        pass


class Description(Page):
    # 메시지 - 게임설명창을 보여라
    def show(self):
        w, h, r = self._width, self._height, self._rectangles
        # Background Design
        self._display.fill(WHITE)
        DESCRIPTION.set_alpha(100)
        r.update({"bg": self._image_to_screen(DESCRIPTION, w, h, (w//2, h//2))})

        # Description Design
        r.update({"title": self._text_to_screen(MEDIUM, "게임 설명", BLACK, (w//2, h//2 - 250))})
        r.update({"rect1": pg.draw.rect(self._display, (0, 0, 0), (w//2 - 250, h//2 - 220, 500, 3))})

        # Arrow Keyboard Design
        r.update({"kb": self._image_to_screen(KEYBOARD, 200, 100, (w//2, h//2 - 80))})
        r.update({"left": self._text_to_screen(SMALL, "왼쪽 이동", BLACK, (w//2 - 170, h//2 - 50))})
        r.update({"right": self._text_to_screen(SMALL, "오른쪽 이동", BLACK, (w//2 + 170, h//2 - 50))})
        r.update({"rotate": self._text_to_screen(SMALL, "블록 회전", BLACK, (w//2, h//2 - 150))})
        r.update({"falling1": self._text_to_screen(SMALL, "빠르게 떨어짐", BLACK, (w//2, h//2 + 10))})

        # Space Keyboard Design
        r.update({"rect2": pg.draw.rect(self._display, (230, 230, 230), (w//2 - 100, h//2 + 90, 200, 45))})
        r.update({"rect3": pg.draw.rect(self._display, BLACK, (w//2 - 100, h//2 + 90, 200, 45), 1)})
        r.update({"space": self._text_to_screen(SMALL, "Spacebar", BLACK, (w//2, h//2 + 115))})
        r.update({"falling2": self._text_to_screen(SMALL, "바로 떨어짐", BLACK, (w//2, h//2 + 180))})
        pg.display.update()

    def control(self, event):
        pass


class Setting(Page):
    # 메시지 - 게임설정창을 보여라
    def show(self):
        w, h, r = self._width, self._height, self._rectangles
        self._display.fill(BLACK)
        r.update({"title": self._text_to_screen(MEDIUM, "시스템 설정", WHITE, (w//2, h//2 - 250))})
        r.update({"m1": self._text_to_screen(MEDIUM, "해상도", WHITE, (w//2 - 300, h//2 - 150))})
        r.update({"m2": self._text_to_screen(SMALL, "배경음", WHITE, (w//2 - 300, h//2 - 100))})
        r.update({"rect1": pg.draw.rect(self._display, WHITE, (w//2 - 200, h//2 - 120, 400, 40), 3)})
        pg.display.update()

    def control(self, event):
        pass


class Exit(Page):
    # 메시지 - 게임종료창을 보여라
    def show(self):
        w, h, r = self._width, self._height, self._rectangles
        self._display.fill(BLACK)
        r.update({"title": self._text_to_screen(MEDIUM, "게임을 종료하시겠습니까?", RED, (w//2, h//2 - 100))})
        r.update({"yes": self._text_to_screen(SMALL, "YES", RED, (w//2 - 80, h//2 + 40))})
        r.update({"no": self._text_to_screen(SMALL, "NO", BLUE, (w//2 + 80, h//2 + 40))})
        pg.display.update()

    def control(self, event):
        pass


class GameBoard(object):
    def __init__(self):
        pass


class Block(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    g = Game()
    g.run(Menu(1000, 600))
    g.run(Start(1000, 600))
    g.run(Description(1000, 600))
    g.run(Setting(1000, 600))
    g.run(Exit(1000, 600))


