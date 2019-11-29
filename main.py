from pygame import *

init()
# Image Setup
bg = image.load("C:/Users/pc/PycharmProjects/Tetris/resource/img/menu_bg.jpg")
arrow = image.load("C:/Users/pc/PycharmProjects/Tetris/resource/img/arrow.jpg")
icon = image.load("C:/Users/pc/PycharmProjects/Tetris/resource/img/icon.png")
keyboard = image.load("C:/Users/pc/PycharmProjects/Tetris/resource/img/방향키.png")
bg_description = image.load("C:/Users/pc/PycharmProjects/Tetris/resource/img/description_bg.jpg")

# Font Setup
smallFont = font.Font("C:/Users/pc/PycharmProjects/Tetris/resource/font/tetris_ft.TTF", 45)
medFont = font.Font("C:/Users/pc/PycharmProjects/Tetris/resource/font/tetris_ft.TTF", 70)
largeFont = font.Font("C:/Users/pc/PycharmProjects/Tetris/resource/font/tetris_ft.TTF", 120)

# Basic Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MINT = (0, 255, 255)
PURPLE = (255, 0, 255)

FPS = 200
width = 800
height = 600

gameDisplay = display.set_mode((width, height))
display.set_caption("Tetris Game")
display.set_icon(icon)


def menu_to_screen(index):
    _ = image_to_screen(bg, width, height, (width//2, height//2))
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


def start_to_screen():
    gameDisplay.fill(BLACK)
    _ = text_to_screen(smallFont, "NEXT", WHITE, (100, 100))
    _ = text_to_screen(smallFont, "LEVEL", WHITE, (150, 150))
    _ = text_to_screen(smallFont, "LINES", WHITE, (200, 200))
    _ = text_to_screen(smallFont, "SCORE", WHITE, (250, 250))


def description_to_screen():
    # 배경 디자인
    gameDisplay.fill(WHITE)
    bg_description.set_alpha(100)
    _ = image_to_screen(bg_description, width, height, (width//2, height//2))

    # 게임 설명 디자인
    _ = text_to_screen(medFont, "게임 설명", BLACK, (width//2, height//2 - 250))
    _ = draw.rect(gameDisplay, (0, 0, 0), (width//2 - 250, height//2 - 220, 500, 3))

    # 방향 키보드 디자인
    _ = image_to_screen(keyboard, 200, 100, (width // 2, height // 2 - 80))
    _ = text_to_screen(smallFont, "왼쪽 이동", BLACK, (width//2 - 170, height//2 - 50))
    _ = text_to_screen(smallFont, "오른쪽 이동", BLACK, (width//2 + 170, height//2 - 50))
    _ = text_to_screen(smallFont, "블록 회전", BLACK, (width//2, height//2 - 150))
    _ = text_to_screen(smallFont, "빠르게 떨어짐", BLACK, (width//2, height//2 + 10))

    # 스페이스바 디자인
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


def exit_to_screen(index):
    gameDisplay.fill(BLACK)
    _ = text_to_screen(medFont, "게임을 종료하시겠습니까?", RED, (width//2, height//2 - 100))
    yes = text_to_screen(smallFont, "YES", RED, (width//2 - 80, height//2 + 40))
    no = text_to_screen(smallFont, "NO", BLUE, (width//2 + 80, height//2 + 40))

    if index == 0:
        _ = image_to_screen(arrow, 30, 30, (yes.left - 20, yes.centery))
    elif index == 1:
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


def gameLoop():
    clock = time.Clock()
    volume = 0.5

    gameExit = False
    menuExit = False
    loopExit = False
    music_start = False

    menu_idx = 0
    while not gameExit:
        # Menu Loop
        while not menuExit:
            if music_start is False:
                music_start = True
                mixer.music.load("C:/Users/pc/PycharmProjects/Tetris/resource/music/BGM_MENU.mp3")
                mixer.music.set_volume(volume)
                mixer.music.play(-1, 0.0)

            menu_to_screen(menu_idx)
            for evt in event.get():
                if evt.type == QUIT:
                    menuExit = loopExit = gameExit = True
                if evt.type == KEYDOWN:
                    if evt.key == K_UP:
                        if menu_idx <= 0:
                            menu_idx = 3
                        else:
                            menu_idx -= 1
                    elif evt.key == K_DOWN:
                        if menu_idx >= 3:
                            menu_idx = 0
                        else:
                            menu_idx += 1
                    elif evt.key == K_RETURN:
                        menuExit = True
                        loopExit = False
                        music_start = False
                    else:
                        pass
            display.update()
            clock.tick(FPS)

        # Others Loop
        exit_idx = 0
        while not loopExit:
            if menu_idx == 0:
                if music_start is False:
                    music_start = True
                    mixer.music.load("C:/Users/pc/PycharmProjects/Tetris/resource/music/BGM_GAME.mp3")
                    mixer.music.play(-1, 0.0)

                start_to_screen()
                for evt in event.get():
                    if evt.type == QUIT:
                        menuExit = loopExit = gameExit = True
            elif menu_idx == 1:
                description_to_screen()
                for evt in event.get():
                    if evt.type == QUIT:
                        menuExit = loopExit = gameExit = True
                    if evt.type == KEYDOWN:
                        if evt.key == K_RETURN:
                            loopExit = True
                            menuExit = False
                            music_start = True
            elif menu_idx == 2:
                setting_to_screen(volume*10)
                for evt in event.get():
                    if evt.type == QUIT:
                        menuExit = loopExit = gameExit = True
                    if evt.type == KEYDOWN:
                        if evt.key == K_RETURN:
                            mixer.music.set_volume(volume)
                            loopExit = True
                            menuExit = False
                            music_start = True
                        elif evt.key == K_LEFT:
                            if round(volume*10) <= 0:
                                volume = 0
                            else:
                                volume -= 0.1
                        elif evt.key == K_RIGHT:
                            if round(volume*10) >= 10:
                                volume = 1
                            else:
                                volume += 0.1
                        else:
                            pass
            elif menu_idx == 3:
                if music_start is False:
                    music_start = True
                    mixer.music.load("C:/Users/pc/PycharmProjects/Tetris/resource/music/BGM_Gameover.mp3")
                    mixer.music.play(-1, 0.0)

                exit_to_screen(exit_idx)
                for evt in event.get():
                    if evt.type == QUIT:
                        menuExit = loopExit = gameExit = True
                    if evt.type == KEYDOWN:
                        if evt.key == K_LEFT:
                            if exit_idx <= 0:
                                exit_idx = 1
                            else:
                                exit_idx -= 1
                        elif evt.key == K_RIGHT:
                            if exit_idx >= 1:
                                exit_idx = 0
                            else:
                                exit_idx += 1
                        elif evt.key == K_RETURN:
                            if exit_idx == 0:
                                menuExit = loopExit = gameExit = True
                            elif exit_idx == 1:
                                loopExit = True
                                menuExit = False
                                music_start = False
                        else:
                            pass
            else:
                raise IndexError
            display.update()
            clock.tick(FPS)
    quit()


if __name__ == '__main__':
    gameLoop()
