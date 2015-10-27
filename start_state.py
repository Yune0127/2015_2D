import game_framework
import main_state

from pico2d import *


name = "StartState"
image = None

def enter():
    global image
    open_canvas(800,600)
    image = load_image('start_view.png')


def exit():
    global image
    #image = load_image('start_view.png')
    del(image)
    #close_canvas()
    game_framework.push_state(main_state)

def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
                close_canvas()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(main_state)


def pause():
    pass
def resume():
    pass



