from pygame import *
from block import Block
import os
import random as rd
import time as t

# Initialize pygame modules
init()
rd.seed(t.time())

# Image Setup
ws = os.path.join(os.getcwd(), "resource")
bg_menu = image.load(ws + "/img/menu_bg.jpg")
bg_start = image.load(ws + "/img/start_bg.jpg")
arrow = image.load(ws + "/img/arrow.jpg")
icon = image.load(ws + "/img/icon.png")
keyboard = image.load(ws + "/img/방향키.png")
bg_description = image.load(ws + "/img/description_bg.jpg")

# Font Setup
smallFont = font.Font(ws + "/font/tetris_ft.TTF", 45)
medFont = font.Font(ws + "/font/tetris_ft.TTF", 70)
largeFont = font.Font(ws + "/font/tetris_ft.TTF", 120)

# Display Setup
FPS = 100
width = 800
height = 600

# FLAG Setup
FLAG_RUN = False
FLAG_MENU = False
FLAG_GAME = False
FLAG_DESCRIPTION = False
FLAG_SETTING = False
FLAG_EXIT = False
FLAG_BGM = False
FLAG_BLOCK = False

# INDEX Setup
IDX_MENU = 0
IDX_EXIT = 0
IDX_BLOCK_NOW = rd.randint(0, 6)
IDX_BLOCK_NEXT = rd.randint(0, 6)

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

# Block Setup
block = [
    [[[0, 0], [0, 1], [0, 2], [1, 2]], [[2, 1], [2, 2], [1, 2], [0, 2]], [[1, 0], [2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0], [0, 1]]],
    [[[0, 0], [1, 0], [0, 1], [0, 2]], [[0, 1], [0, 2], [1, 2], [2, 2]], [[1, 2], [2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0], [2, 1]]],
    [[[0, 0], [0, 1], [1, 1], [1, 2]], [[0, 2], [1, 1], [1, 2], [2, 1]], [[0, 0], [0, 1], [1, 1], [1, 2]], [[0, 2], [1, 1], [1, 2], [2, 1]]],
    [[[0, 1], [0, 2], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 1], [0, 2], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, 1], [2, 1]]],
    [[[0, 0], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]]],
    [[[0, 1], [1, 0], [1, 1], [1, 2]], [[0, 1], [1, 1], [2, 1], [1, 2]], [[1, 0], [1, 1], [1, 2], [2, 1]], [[0, 1], [1, 0], [1, 1], [2, 1]]],
    [[[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 3], [1, 3], [2, 3], [3, 3]], [[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 3], [1, 3], [2, 3], [3, 3]]]
]

# Window Setup
gameDisplay = display.set_mode((width, height))
display.set_caption("Tetris Game")
display.set_icon(icon)
board = [[draw.rect(gameDisplay, WHITE, (row * 25 + 275, col * 25 + 50, 25, 25), 1) for row in range(10)]
         for col in range(20)]

# USEREVENT Setup
time.set_timer(USEREVENT, 1000)


def menu_to_screen(index):
    _ = image_to_screen(bg_menu, width, height, (width//2, height//2))
    _ = text_to_screen(largeFont, "TETRIS", MINT, (width//2, height*0.25))
    start = text_to_screen(smallFont, "START", RED, (width//2, height * 0.45))
    description = text_to_screen(smallFont, "DESCRIPTION", GREEN, (width//2, height * 0.55))
    setting = text_to_screen(smallFont, "SETTING", BLUE, (width//2, height * 0.65))
    exit = text_to_screen(smallFont, "EXIT", PURPLE, (width//2, height * 0.75))

    if index == 0:
        _ = image_to_screen(arrow, 30, 30, (start.left - 20, start.centery))
    elif index == 1:
        _ = image_to_screen(arrow, 30, 30, (description.left - 20, description.centery))
    elif index == 2:
        _ = image_to_screen(arrow, 30, 30, (setting.left - 20, setting.centery))
    elif index == 3:
        _ = image_to_screen(arrow, 30, 30, (exit.left - 20, exit.centery))
    else:
        pass


def start_to_screen(score=0, level=1, lines=0):
    gameDisplay.fill(BLACK)
    bg_start.set_alpha(50)
    _ = image_to_screen(bg_start, width, height, (width//2, height//2))

    # Next Block Info Design
    _ = text_to_screen(smallFont, "NEXT", WHITE, (690, 100))
    nxt = draw.rect(gameDisplay, WHITE, (590, 120, 200, 150), 3)

    # Score Info Design
    _ = text_to_screen(smallFont, "SCORE", WHITE, (110, 100))
    _ = text_to_screen(smallFont, str(score), YELLOW, (110, 150))
    _ = draw.rect(gameDisplay, WHITE, (10, 120, 200, 50), 3)

    # Level Info Design
    _ = text_to_screen(smallFont, "LEVEL", WHITE, (110, 250))
    _ = text_to_screen(smallFont, str(level), RED, (110, 300))
    _ = draw.rect(gameDisplay, WHITE, (10, 270, 200, 50), 3)

    # Lines Info Design
    _ = text_to_screen(smallFont, "LINES", WHITE, (110, 400))
    _ = text_to_screen(smallFont, str(lines), PURPLE, (110, 450))
    _ = draw.rect(gameDisplay, WHITE, (10, 420, 200, 50), 3)

    # Game Board Design
    _ = draw.rect(gameDisplay, PURPLE, (265, 50, 10, 500))
    _ = draw.rect(gameDisplay, PURPLE, (525, 50, 10, 500))
    _ = draw.rect(gameDisplay, PURPLE, (265, 550, 270, 10))
    for row in range(21):
        draw.line(gameDisplay, GRAY, (275, 50 + row * 25), (525, 50 + row * 25), 1)
        for col in range(11):
            draw.line(gameDisplay, GRAY, (275 + col * 25, 50), (275 + col * 25, 550), 1)


def description_to_screen():
    # Background Design
    gameDisplay.fill(WHITE)
    bg_description.set_alpha(100)
    _ = image_to_screen(bg_description, width, height, (width//2, height//2))

    # Description Design
    _ = text_to_screen(medFont, "게임 설명", BLACK, (width//2, height//2 - 250))
    _ = draw.rect(gameDisplay, (0, 0, 0), (width//2 - 250, height//2 - 220, 500, 3))

    # Arrow Keyboard Design
    _ = image_to_screen(keyboard, 200, 100, (width // 2, height // 2 - 80))
    _ = text_to_screen(smallFont, "왼쪽 이동", BLACK, (width//2 - 170, height//2 - 50))
    _ = text_to_screen(smallFont, "오른쪽 이동", BLACK, (width//2 + 170, height//2 - 50))
    _ = text_to_screen(smallFont, "블록 회전", BLACK, (width//2, height//2 - 150))
    _ = text_to_screen(smallFont, "빠르게 떨어짐", BLACK, (width//2, height//2 + 10))

    # Space Keyboard Design
    _ = draw.rect(gameDisplay, (230, 230, 230), (width // 2 - 100, height // 2 + 90, 200, 45))
    _ = draw.rect(gameDisplay, BLACK, (width // 2 - 100, height // 2 + 90, 200, 45), 1)
    _ = text_to_screen(smallFont, "Spacebar", BLACK, (width // 2, height // 2 + 115))
    _ = text_to_screen(smallFont, "바로 떨어짐", BLACK, (width // 2, height // 2 + 180))


def setting_to_screen(vol):
    gameDisplay.fill(BLACK)
    _ = text_to_screen(medFont, "시스템 설정", WHITE, (width//2, height//2 - 250))
    _ = text_to_screen(smallFont, "해상도", WHITE, (width//2 - 300, height//2 - 150))
    _ = text_to_screen(smallFont, "배경음", WHITE, (width//2 - 300, height//2 - 100))
    _ = draw.rect(gameDisplay, WHITE, (width//2 - 200, height//2 - 120, 400, 40), 3)
    _ = draw.rect(gameDisplay, WHITE, (width//2 - 200, height//2 - 120, 40*vol, 40))


def exit_to_screen(idx):
    gameDisplay.fill(BLACK)
    _ = text_to_screen(medFont, "게임을 종료하시겠습니까?", RED, (width//2, height//2 - 100))
    yes = text_to_screen(smallFont, "YES", RED, (width//2 - 80, height//2 + 40))
    no = text_to_screen(smallFont, "NO", BLUE, (width//2 + 80, height//2 + 40))

    if idx == 0:
        _ = image_to_screen(arrow, 30, 30, (yes.left - 20, yes.centery))
    elif idx == 1:
        _ = image_to_screen(arrow, 30, 30, (no.left - 20, no.centery))
    else:
        pass


def image_to_screen(img, w, h, pos):
    screen_image = transform.scale(img, (w, h))
    image_rect = screen_image.get_rect()
    image_rect.center = pos
    result_rect = gameDisplay.blit(screen_image, image_rect)
    return result_rect


def text_to_screen(ft, text, color, pos):
    screen_text = ft.render(text, True, color)
    text_rect = screen_text.get_rect()
    text_rect.center = pos
    result_rect = gameDisplay.blit(screen_text, text_rect)
    return result_rect


def button_to_screen(text, x, y, w, h, inactive_color, active_color):
    cur = mouse.get_pos()
    if (x < cur[0] < x+w) and (y < cur[1] < y+h):
        button_rect = draw.rect(gameDisplay, active_color, (x, y, w, h))
    else:
        button_rect = draw.rect(gameDisplay, inactive_color, (x, y, w, h))

    _ = text_to_screen(smallFont, text, BLACK, button_rect.center)


def block_to_screen(board, block_now, block_next):
    try:
        for row, col in block_now:
            draw.rect(gameDisplay, RED, board[row][col])
    except IndexError as e:
        pass


def run():
    clock = time.Clock()

    global board
    global FLAG_RUN, FLAG_MENU, FLAG_GAME, FLAG_DESCRIPTION, FLAG_SETTING, FLAG_EXIT
    global FLAG_BGM, FLAG_BLOCK
    global IDX_MENU, IDX_EXIT, IDX_BLOCK_NOW, IDX_BLOCK_NEXT
    volume = 0.1

    cnt = 0
    while not FLAG_RUN:
        # Menu Loop
        while not FLAG_MENU:
            # BGM Setting
            if FLAG_BGM is False:
                FLAG_BGM = True
                mixer.music.load(ws + "/music/BGM_MENU.mp3")
                mixer.music.set_volume(volume)
                mixer.music.play(-1, 0.0)

            # Background Setting
            menu_to_screen(IDX_MENU)

            # Event Handle
            for evt in event.get():
                if evt.type == QUIT:
                    FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                elif evt.type == KEYDOWN:
                    if evt.key == K_UP:
                        if IDX_MENU <= 0:
                            IDX_MENU = 3
                        else:
                            IDX_MENU -= 1
                    elif evt.key == K_DOWN:
                        if IDX_MENU >= 3:
                            IDX_MENU = 0
                        else:
                            IDX_MENU += 1
                    elif evt.key == K_RETURN:
                        FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                        FLAG_RUN = False
                        if IDX_MENU == 0:
                            FLAG_GAME = False
                            FLAG_BGM = False
                        elif IDX_MENU == 1:
                            FLAG_DESCRIPTION = False
                            FLAG_BGM = True
                        elif IDX_MENU == 2:
                            FLAG_SETTING = False
                            FLAG_BGM = True
                        elif IDX_MENU == 3:
                            FLAG_EXIT = False
                            FLAG_BGM = False
                        else:
                            raise ValueError
                    else:
                        pass
                else:
                    pass
            display.update()
            clock.tick(FPS)

        # Start Loop
        rot = 0
        move_x = 0
        move_y = 0
        while not FLAG_GAME:
            # BGM Setting
            if FLAG_BGM is False:
                FLAG_BGM = True
                mixer.music.load(ws + "/music/BGM_GAME.mp3")
                mixer.music.set_volume(volume)
                mixer.music.play(-1, 0.0)

            # Background Setting
            start_to_screen()

            # Event Handle
            if FLAG_BLOCK is False:
                FLAG_BLOCK = True
                IDX_BLOCK_NOW = IDX_BLOCK_NEXT
                IDX_BLOCK_NEXT = rd.randint(0, 6)
                block_to_screen(board, block[IDX_BLOCK_NOW][rot], block[IDX_BLOCK_NEXT][rot])
            else:
                block_to_screen(board, block[IDX_BLOCK_NOW][rot], block[IDX_BLOCK_NEXT][rot])
                if cnt == 50:
                    cnt = 0
                    rot = 0
                    FLAG_BLOCK = False
                cnt += 1
            for i, tmp in enumerate(block[IDX_BLOCK_NOW]):
                for j, _ in enumerate(tmp):
                    block[IDX_BLOCK_NOW][i][j][1] += move_x
                    block[IDX_BLOCK_NOW][i][j][0] += move_y

            for evt in event.get():
                if evt.type == QUIT:
                    FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                elif evt.type == KEYDOWN:
                    if evt.key == K_RIGHT:
                        move_x = 1
                    elif evt.key == K_LEFT:
                        move_x = -1
                    elif evt.key == K_DOWN:
                        move_y = 1
                    elif evt.key == K_UP:
                        if rot >= 3:
                            rot = 0
                        else:
                            rot += 1
                    elif evt.key == K_SPACE:
                        pass
                    else:
                        pass
                elif evt.type == KEYUP:
                    if evt.key == K_RIGHT:
                        move_x = 0
                    elif evt.key == K_LEFT:
                        move_x = 0
                    elif evt.key == K_DOWN:
                        move_y = 0
                    else:
                        pass
                elif evt.type == USEREVENT:
                    for i, tmp in enumerate(block[IDX_BLOCK_NOW]):
                        for j, _ in enumerate(tmp):
                            block[IDX_BLOCK_NOW][i][j][0] += 1
                else:
                    pass
            display.update()
            clock.tick(FPS//10)

        # Description Loop
        while not FLAG_DESCRIPTION:
            # Background Setting
            description_to_screen()

            # Event Handle
            for evt in event.get():
                if evt.type == QUIT:
                    FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                elif evt.type == KEYDOWN:
                    if evt.key == K_RETURN:
                        FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                        FLAG_RUN = FLAG_MENU = False
                else:
                    pass
            display.update()
            clock.tick(FPS)

        # Setting Loop
        while not FLAG_SETTING:
            # Background Setting
            setting_to_screen(volume * 10)

            # Event Handle
            for evt in event.get():
                if evt.type == QUIT:
                    FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                elif evt.type == KEYDOWN:
                    if evt.key == K_RETURN:
                        FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                        FLAG_RUN = FLAG_MENU = False
                    elif evt.key == K_LEFT:
                        if round(volume * 10) <= 0:
                            volume = 0
                        else:
                            volume -= 0.1
                        mixer.music.set_volume(volume)
                    elif evt.key == K_RIGHT:
                        if round(volume * 10) >= 10:
                            volume = 1
                        else:
                            volume += 0.1
                        mixer.music.set_volume(volume)
                    else:
                        pass
                elif evt.type == MOUSEBUTTONDOWN:
                    if evt.button == BUTTON_WHEELDOWN:
                        if round(volume * 10) <= 0:
                            volume = 0
                        else:
                            volume -= 0.1
                        mixer.music.set_volume(volume)
                    elif evt.button == BUTTON_WHEELUP:
                        if round(volume * 10) >= 10:
                            volume = 1
                        else:
                            volume += 0.1
                        mixer.music.set_volume(volume)
                    else:
                        pass
                else:
                    pass
            display.update()
            clock.tick(FPS)

        # Exit Loop
        while not FLAG_EXIT:
            # BGM Setting
            if FLAG_BGM is False:
                FLAG_BGM = True
                mixer.music.load(ws + "/music/BGM_GAMEOVER.mp3")
                mixer.music.set_volume(volume)
                mixer.music.play(-1, 0.0)

            # Background Setting
            exit_to_screen(IDX_EXIT)

            # Event Handle
            for evt in event.get():
                if evt.type == QUIT:
                    FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                elif evt.type == KEYDOWN:
                    if evt.key == K_LEFT:
                        if IDX_EXIT <= 0:
                            IDX_EXIT = 1
                        else:
                            IDX_EXIT -= 1
                    elif evt.key == K_RIGHT:
                        if IDX_EXIT >= 1:
                            IDX_EXIT = 0
                        else:
                            IDX_EXIT += 1
                    elif evt.key == K_RETURN:
                        if IDX_EXIT == 0:
                            FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                        elif IDX_EXIT == 1:
                            FLAG_RUN = FLAG_MENU = FLAG_GAME = FLAG_DESCRIPTION = FLAG_SETTING = FLAG_EXIT = True
                            FLAG_RUN = FLAG_MENU = FLAG_BGM = False
                    else:
                        pass
                else:
                    pass
            display.update()
            clock.tick(FPS)
    quit()


if __name__ == '__main__':
    run()
