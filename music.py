import pygame as pg


class Music(object):
    def __init__(self):
        pg.mixer.pre_init(44100, 16, 1, 4096)
        pg.mixer.init()
        self.__vol = 0.1
        self.__bgm = None

    def set_volume(self, volume):
        if isinstance(self.__bgm, pg.mixer.Sound):
            if volume > 1:
                self.__vol = 1
            else:
                self.__vol = volume
            self.__bgm.set_volume(volume)

    def play(self, path):
        self.__bgm = pg.mixer.Sound(path)
        self.__bgm.set_volume(self.__vol)
        self.__bgm.play(-1)

    def stop(self):
        if isinstance(self.__bgm, pg.mixer.Sound):
            self.__bgm.stop()