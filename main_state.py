
import random
import json
import os

from pico2d import *

import game_framework
import start_state



name = "MainState"
boy1 = None
boy2 = None
boy3 = None
hero = None
main = None
back = None


class Back:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400,300)


class Boy1:
    def __init__(self):
        self.image = load_image('uncle_one.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(280, 375)


class Boy2:
    def __init__(self):
        self.image = load_image('uncle_two.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(500, 375)


def enter():
    global boy1, boy2, back
    boy1 = Boy1()
    boy2 = Boy2()
    back = Back()


def exit():
    global boy1, boy2, back
    del(boy1)
    del(boy2)
    del(back)
    close_canvas()

def pause():
    pass

def resume():
    pass



def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state (start_state)



def update():
    boy1.update()


def draw():
    clear_canvas()
    back.draw()
    boy1.draw()
    update_canvas()